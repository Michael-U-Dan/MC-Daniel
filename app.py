
import pickle
import streamlit as st
import pandas as pd

# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("Quantity Predictor")

# input widget for getting user value for X (feature matrix value)
total = st.slider("Total", min_value=0, max_value=100, value=20)

# After selesting Quantity, the user then submits the quantity value
if st.button("Predict"):
  # take the quantity value, and format the value the right way
  prediction = model.predict([[total]])[0].round(2)
  st.write("The predicted Quantity is", prediction, "pounce")
