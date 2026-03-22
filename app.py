import streamlit as st
import numpy as np
import pickle

# load model and features
model = pickle.load(open("model.pkl", "rb"))
features = pickle.load(open("features.pkl", "rb"))

st.set_page_config(page_title="House Price Predictor", page_icon="🏠")

st.title("🏠 House Price Prediction App")
st.write("Enter house details to predict price")

# dynamic inputs based on features
input_data = []

st.subheader("Input Features")

for feature in features:
    value = st.number_input(f"{feature}", value=0.0)
    input_data.append(value)

# prediction button
if st.button("Predict Price"):
    input_array = np.array(input_data).reshape(1, -1)
    
    prediction_log = model.predict(input_array)
    
    # reverse log transform
    prediction = np.expm1(prediction_log)

    st.success(f"🏡 Estimated House Price: {prediction[0]:,.2f}")
