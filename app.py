import streamlit as st
import numpy as np
import pickle

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# -------------------- LOAD FILES --------------------
model = pickle.load(open("model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

# -------------------- SIDEBAR --------------------
st.sidebar.title("⚙️ Settings")

theme = st.sidebar.selectbox("Select Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown(
        """
        <style>
        body {background-color: #0E1117; color: white;}
        </style>
        """,
        unsafe_allow_html=True
    )

st.sidebar.markdown("---")
st.sidebar.info("This app predicts house prices using Machine Learning.")

# -------------------- HEADER --------------------
st.markdown(
    """
    <h1 style='text-align: center;'>🏠 House Price Prediction</h1>
    <p style='text-align: center;'>Enter details below to estimate house price</p>
    """,
    unsafe_allow_html=True
)

# -------------------- INPUT SECTION --------------------
st.subheader("📊 Input Features")

cols = st.columns(2)
input_data = []

for i, feature in enumerate(features):
    with cols[i % 2]:

        # 🔥 SMART INPUT TYPES
        if "Area" in feature or "SF" in feature or "Lot" in feature:
            value = st.slider(f"{feature}", 0, 5000, 1000)

        elif "Year" in feature:
            value = st.slider(f"{feature}", 1900, 2025, 2000)

        elif "Bedroom" in feature or "Room" in feature:
            value = st.slider(f"{feature}", 0, 10, 3)

        elif "Bath" in feature:
            value = st.slider(f"{feature}", 0, 5, 2)

        elif "Garage" in feature:
            value = st.slider(f"{feature}", 0, 5, 1)

        elif "OverallQual" in feature:
            value = st.selectbox(f"{feature}", list(range(1, 11)))

        elif "Condition" in feature or "Quality" in feature:
            value = st.selectbox(f"{feature}", [1,2,3,4,5])

        else:
            # default fallback
            value = st.number_input(f"{feature}", value=0.0)

        input_data.append(value)

# -------------------- PREDICTION --------------------
st.markdown("---")

if st.button("🚀 Predict Price"):
    input_array = np.array(input_data).reshape(1, -1)

    prediction_log = model.predict(input_array)
    prediction = np.expm1(prediction_log)

    st.success(f"🏡 Estimated Price: {prediction[0]:,.2f}")

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown(
    """
    <p style='text-align: center;'>
    Built with ❤️ using Streamlit | By Umar
    </p>
    """,
    unsafe_allow_html=True
)
