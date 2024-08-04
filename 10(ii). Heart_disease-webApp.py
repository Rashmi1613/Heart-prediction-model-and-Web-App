# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 11:09:10 2023

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/DELL/Desktop/Heart-disease Prediction system/trained_model.sav', 'rb'))

def heart_prediction(input_data):
    
    input_data_as_numpy_array= np.asarray(input_data)

    # reshape the numpy array as we are predicting for only on instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0]== 0):
      return 'The Person does not have a Heart Disease'
    else:
      return 'The Person has Heart Disease'
  
def main():
    
    
    # giving a title
    st.title('Heart Disease Prediction Web App')
    
    
    # getting the input data from the user
        
    Age = st.text_input('Age of the person')
    Sex = st.text_input('Sex of the person')
    CP = st.text_input('Chest pain type')
    Trestbps = st.text_input('Blood Pressure')
    chol = st.text_input('Cholesterol Measure')
    fbs = st.text_input('Fasting glucose level')
    restecg = st.text_input('Resting electrocardiographic measurement')
    thalach = st.text_input('Max Heart rate')
    exang = st.text_input('Exercise induced angina')
    oldpeak = st.text_input('Oldpeak')
    slope = st.text_input('Slope')
    ca = st.text_input('Calcium')
    thal = st.text_input('Iron Score')
    
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        diagnosis = heart_prediction([Age,Sex, CP, Trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
        
        
    st.success(diagnosis)
    
      
    
if __name__ == '__main__':
    main()
    
    