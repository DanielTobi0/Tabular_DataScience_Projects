# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:06:55 2022

@author: adeju
"""

#importing the required libraries
import numpy as np
import streamlit as st
import pickle
import math


# loading the saved model
loaded_model = pickle.load(open('prediction_model.sav','rb'))

st.info(
        f""" 
        This app predicts the price of a house based on it features.
        
        The underlying model was built in the Housing Price Prediction Regressor project and is based on the
        dataset used for that project. [see code]({'https://github.com/DanielTobi0/Housing-Price-Prediction'}). 
   
   """
   )


def housing_prediction(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,
                       sqft_basement,yr_built,sqft_living15,sqft_lot15):
    
    prediction = loaded_model.predict([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,
                                        grade,sqft_above,sqft_basement,yr_built,sqft_living15,sqft_lot15]])
    
    prediction = np.exp(prediction)
    prediction = math.floor(prediction)
    return str(prediction).lstrip('[').rstrip(']')


def main():
    
    # giving a title
    st.title('Housing Prediction')
    
    # getting the input from the user
    bedrooms = st.number_input("Enter numbers of bathrooms", min_value=0, max_value=10, step=1)
    bathrooms = st.number_input("Enter numbers of bedrooms", min_value=0, max_value=8, step=1)
    sqft_living = st.number_input("Enter size of the Square Living", min_value=0)
    sqft_lot = st.number_input("Enter size of the Square Lot", min_value=0)
    floors = st.number_input("Enter numbers of floors", min_value=0)
    waterfront = st.number_input("Enter numbers of waterfront", min_value=1, max_value=2, step=1)
    view = st.number_input("Enter numbers of view", min_value=0)
    condition = st.number_input("scale of 1-10, what the cond of the house", min_value=0)
    grade = st.number_input("Enter the grade of the house", min_value=0)
    sqft_above = st.number_input("Enter size of the Square above", min_value=0)
    sqft_basement = st.number_input("Enter size of the Square basement", min_value=0)
    yr_built = st.number_input("Enter year it was built", min_value=1900)
    sqft_living15 = st.number_input("Enter size of the Square feet living", min_value=0)
    sqft_lot15 = st.number_input("Enter size of the Square feet lot", min_value=0)
    
    
    # code for predicted price
    predicted_price = ""
    
    # code for button
    if st.button("Housing prediction test result"):
        predicted_price = housing_prediction(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,sqft_living15,sqft_lot15)
        st.success(f'The predicted house value is ¥{predicted_price}')
    
    
if __name__ == '__main__':
    main()
    
    
