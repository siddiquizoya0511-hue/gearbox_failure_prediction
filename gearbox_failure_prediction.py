

# import libraries
import numpy as np
import joblib
import streamlit as st

# gearbox_failure_prediction.pkl.

model = joblib.load('gearbox_failure_prediction.pkl')

st.set_page_config(page_title='Gearbox failure Classification', layout="centered")
st.title('Gearbox failure Classification App')
st.write("Predict the Faiure rate")

Load	= st.number_input("Value of Load_%", value=None)
Temperature_C = st.number_input("Value of Temperature_C,", value=None)
Vibration_mm_s	= st.number_input("Value of Vibration_mm_s,", value=None)
Oil_Level= st.number_input("Value of Oil_Level_%,", value=None)


if st.button('Predict'):
  input_data = np.array([[Load,
                          Temperature_C,
                          Vibration_mm_s,
                          Oil_Level
                          ]])
  prediction = model.predict(input_data)[0]
  if prediction == 0:
    st.success('Fail')
  else:
    st.success('Pass')







