# Janusha_Brahmadevuni_MajorProject1_UnloxAcademy
An end-to-end Machine Learning project for predicting Indian pre-owned car prices based on vehicle and market features, including data analysis, model training, evaluation, and an interactive Streamlit web application for real-time and batch predictions.

# Indian Pre-Owned Car Price Prediction

An ML-based web application that predicts the resale price of pre-owned cars in India.

# Live Demo
 Try the Live Streamlit App :
https://major-project-car-price-prediction.streamlit.app/

## PROJECT OVERVIEW

This project focuses on predicting the resale price of pre-owned cars in the Indian market using Machine Learning.

The project is divided into two main components:

Component 1A: Machine Learning model development and analysis

Component 1B: Streamlit web application for price prediction

The system predicts the estimated price of a used car based on its vehicle specifications, usage details, and market-related features.

## OBJECTIVE

The main objective of this project is to develop an end-to-end Machine Learning system that can:

Analyze and understand used-car data
Perform data cleaning and preprocessing
Build and compare regression models
Evaluate model performance
Select the best-performing model
Predict prices for unseen cars
Deploy the trained model using Streamlit

The project requirements specify EDA, preprocessing, model building, evaluation, and Streamlit deployment as the main deliverables.

# COMPONENT 1A - MACHINE LEARNING NOTEBOOK
## EXPLORATORY DATA ANALYSIS

The training dataset was analyzed to understand the structure and important patterns in the data.

The analysis includes:

Dataset structure and data types
Missing value analysis
Duplicate record analysis
Numerical feature distributions
Categorical feature analysis
Target variable analysis
Relationships between features and car price
Correlation analysis
Outlier detection

Meaningful visualizations were used to understand important patterns and relationships in the dataset.

## DATA PREPROCESSING

The following preprocessing steps were performed:

Removed unnecessary spaces from column names
Handled missing values
Filled missing body type values as 'Unknown'
Removed ID from model training
Removed manufacture_year because the Age of car feature provides the same information
Applied median imputation to numerical features
Applied categorical imputation
Applied One-Hot Encoding to categorical features

## MODEL BUILDING

Different regression models were trained and compared:

Mean Baseline
Linear Regression
Random Forest Regressor
XGBoost Regressor

Cross-validation was performed to check model performance across different data splits, followed by hyperparameter tuning to improve the selected model.
The project requirements specifically recommend baseline and advanced regression techniques such as Random Forest and XGBoost, along with cross-validation and hyperparameter tuning.

## MODEL EVALUATION

The models were evaluated using:

RMSE (Root Mean Squared Error)
MAE (Mean Absolute Error)
R² Score

The tuned XGBoost model was selected as the final model based on its validation performance.

# COMPONENT 1B - STREAMLIT APPLICATION

The trained Machine Learning model was deployed using Streamlit as an interactive web application.
The application allows users to enter car details and obtain an estimated resale price.

SINGLE CAR PRICE PREDICTION

Users can provide details such as:

Maker and Model
Location
Distance
Age of Car
Engine Displacement
Engine Power
Owner Type
Body Type
Transmission
Fuel Type
Door Count
Seat Count
Vroom Audit Rating

After entering the details, the application generates an estimated car price in real time.

FAIR PRICE RANGE

Along with the predicted price, the application provides a dynamic fair price range using a ±5% valuation band.
This gives the user an approximate price range around the predicted value instead of displaying only a single prediction. This follows the project's valuation banding requirement.

## BATCH PREDICTION

The application supports batch prediction using a Test CSV file.
Users can:

Upload the test CSV file
Generate predictions for multiple cars
View the predicted results
Download the prediction results as a CSV file

The output contains the required ID and Price columns.

## VISUAL INSIGHTS

The application provides simple visual insights using Streamlit charts:
Age vs Predicted Price
Distance vs Predicted Price
These charts help users understand how important vehicle factors are related to predicted prices. The project requirements also include a visual insights dashboard as an enhancement.

## TECHNOLOGIES USED

Python
Pandas
NumPy
Scikit-learn
XGBoost
Matplotlib
Streamlit
Joblib
Jupyter Notebook

## Future Enhancements

The project can be further improved by adding:

More vehicle-related features.
Additional Machine Learning models for comparison.
Hyperparameter tuning.
Advanced model optimization.
Feature importance analysis.
Improved price visualization.
Prediction confidence or prediction intervals.
Deployment with a custom domain.
Integration with real-time used-car listings.



# CONCLUSION

The Indian Pre-Owned Car Price Prediction project demonstrates how Machine Learning can be applied to a real-world problem in the automobile resale market.
By preprocessing vehicle data, analyzing important features, training a regression model, and integrating the model into a Streamlit application, the project provides an interactive way to estimate the resale price of pre-owned cars.
The application goes beyond a basic prediction model by supporting individual predictions, batch predictions, and visual data insights. This makes the project a practical demonstration of the complete Machine Learning workflow, from data analysis and model development to deployment.

Overall, the project provides a foundation for developing more advanced vehicle price prediction systems using larger datasets, improved models, and real-time market information.
The final Streamlit application provides an easy-to-use interface for obtaining individual and batch car price predictions.
