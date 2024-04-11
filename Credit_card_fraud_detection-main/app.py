import streamlit as st
import pandas as pd
import pickle
import warnings

# Suppressing warnings for cleaner output
warnings.filterwarnings('ignore')

# Load the scaler
# scale_name = 'C:/Users/Daniel/Desktop/Credit_Card_Fraud_Detection/scaler.sav'
scale_name = 'scaler.sav'
scaler = pickle.load(open(scale_name, 'rb'))

# Load the saved classification model
# filename = 'C:/Users/Daniel/Desktop/Credit_Card_Fraud_Detection/prediction_model.sav'
filename = 'prediction_model.sav'
model = pickle.load(open(filename, 'rb'))


# Function to collect user input features into a DataFrame
def user_input_features():
    distance_from_home = st.sidebar.number_input('distance_from_home: ', step=0.1, min_value=0.0, value=26.8)
    distance_from_last_transaction = st.sidebar.number_input('distance_from_last_transaction: ', step=0.01,
                                                             min_value=0.0, value=5.41)
    ratio_to_median_purchase_price = st.sidebar.number_input('ratio_to_median_purchase_price: ', step=0.01,
                                                             min_value=0.0, value=1.65)

    repeat_retailer = st.sidebar.selectbox('repeat_retailer: ', ('Yes', 'No'))
    repeat_retailer = 0 if repeat_retailer == 'No' else 1

    used_chip = st.sidebar.selectbox('used_chip: ', ('Yes', 'No'))
    used_chip = 0 if used_chip == 'No' else 1

    used_pin_number = st.sidebar.selectbox('used_pin_number: ', ('Yes', 'No'))
    used_pin_number = 0 if used_pin_number == 'No' else 1

    online_order = st.sidebar.selectbox('online_order: ', ('Yes', 'No'))
    online_order = 0 if online_order == 'No' else 1

    data = {'distance_from_home': distance_from_home, 'distance_from_last_transaction': distance_from_last_transaction,
            'ratio_to_median_purchase_price': ratio_to_median_purchase_price, 'repeat_retailer': repeat_retailer,
            'used_chip': used_chip, 'used_pin_number': used_pin_number, 'online_order': online_order}

    features = pd.DataFrame(data, index=[0])
    return features


# Welcome screen text
st.write("""
# Credit Card Fraud Prediction

This app predicts the likelihood of a credit card fraud happening, based on the various user inputs.
""")

# Display user input features
st.sidebar.header('User Input Features')
input_df = user_input_features()
st.write('### User Input Features')
st.write(input_df)

# Make predictions
input_df_scale = scaler.transform(input_df)
prediction = model.predict(input_df_scale)
prediction_proba = model.predict_proba(input_df_scale)[:, 1]

# Display results
st.subheader('Prediction')
st.write(':red[Card at risk fraud!!]' if prediction == 1 else ':green[Card not at risk]')

st.subheader('Prediction Probability')

st.write(f'The probability of being at risk: {round(prediction_proba[0], 2)}')
