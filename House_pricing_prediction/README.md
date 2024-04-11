# Housing Price Prediction

### In this project I built a regressor model, capable of predicting house prices, using LightGBM machine learning model, based on the features of the house.

King County is located in the U.S. state of Washington. The population was 2,252,782 in the 2019 census estimate, making it the most populous county in Washington, and the 12th-most populous in the United States. The county seat is Seattle, also the state's most populous city.

Real estate plays an integral role in the U.S. economy. Purchasing and selling a house is among the biggest commitments and a great source of income for most people. Therefore, accurate prediction of prices based on other sale data can be a critical tool to assist the buyer/seller in making an informed decision.

Prototyping is done in the **price_prediction.ipynb** notebook file complete with a step-by-step walk through of model building logic, visualisations and model explainability. Deployment is done via the python script **prediction_app.py** culminating in a live [web application](https://danieltobi0-housing-price-prediction-prediction-app-micgmp.streamlitapp.com/).

# Defination of Attributes
1. id - Unique identified for a house
2. date - Date house was sold
3. price - Price is prediction target
4. bedrooms - Number of Bedrooms/House
5. bathrooms - Number of bathrooms/bedrooms
6. sqft_living - Square footage of the home
7. sqft_lot - Square footage of the lot
8. floors - Total floors (levels) in house
9. waterfront - House which has a view to a waterfront
10. view - Has been viewed
11. condition - How good the condition is ( Overall )
12. grade - overall grade given to the housing unit, based on King County grading system
13. sqft_above - Square footage of house apart from basement
14. sqft_basement - Square footage of the basement
15. yr_built - Built Year
16. yr_renovated - Year when house was renovated
17. zipcode - Zipcode
18. lat - Latitude coordinate
20. long - Longitude coordinate
21. sqft_living15 - Square footage of interior housing living space for the nearest 15 neighbors
22. sqft_lot15 - Square footage of the land lots of the nearest 15 neighbors
