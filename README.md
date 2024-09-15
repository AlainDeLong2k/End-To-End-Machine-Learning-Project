# End to End Machine Learning Project

## Overview  
The Student Math Score Predictor is a web application built using Streamlit that predicts students' exam scores based on various factors. By inputting demographic information and previous scores, users can receive predictions for their prospective Math scores.  

## Dataset and Model Training  

In this project, we utilize the dataset titled [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977) available on Kaggle. This dataset contains performance data from students across various subjects, which allows us to analyze factors that influence exam scores.  

### Models Used  

We have implemented several machine learning models to predict students' exam scores, including:  

1. **Linear Regression**:  
   - A simple yet effective approach for regression tasks that helps establish a linear relationship between the dependent and independent variables.  

2. **K-Nearest Neighbors (KNN)**:  
   - A non-parametric method that classifies cases based on the k training examples closest in distance.  

3. **Decision Tree**:  
   - A powerful model that uses a tree-like graph of decisions, making it easy to visualize and interpret the decisions being made.  

4. **XGBoost**:  
   - An optimized gradient boosting framework that increases the performance and speed of decision trees, typically leading to better predictive accuracy.  

In addition to these models, various other machine learning algorithms were considered to further enhance the prediction process.  

### Hyperparameter Tuning  

- To achieve optimal performance from our models, hyperparameter tuning was performed using techniques such as Grid Search and Random Search. This process involved evaluating different combinations of hyperparameters, allowing us to identify the best settings for each model. By fine-tuning these parameters, we are able to enhance our models' accuracy and generalizability on unseen data.  

- Overall, the effective combination of insightful data analysis and rigorous model training enables us to provide reliable predictions of students' performance in exams.

## Features  
- User-friendly interface for inputting student data.  
- Predicts the Math score based on:  
  - Gender  
  - Race or Ethnicity  
  - Parental Level of Education  
  - Lunch Type  
  - Test Preparation Course Status  
  - Reading Score  
  - Writing Score  
- Real-time predictions displayed after submission.

## Deploying
- End to End Machine Learning Project deployed website: https://alaindelong-end-to-end-machine-learning-project.hf.space/

## Usage
1. Open the application in your web browser.
2. Fill out the input form with the relevant student information.
3. Click the "Predict Exam Scores" button to see the predicted Math score.
