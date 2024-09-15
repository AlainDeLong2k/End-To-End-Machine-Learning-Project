import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Application title
st.set_page_config(page_title="Math Score Predictor")
st.title("Student Math Score Predictor")
st.write("This application predicts math scores based on student data.")

# Input form
with st.form(key="student_form"):
    gender = st.selectbox("Gender", options=["male", "female"])
    ethnicity = st.selectbox(
        "Race or Ethnicity",
        options=["group A", "group B", "group C", "group D", "group E"],
    )
    parental_education = st.selectbox(
        "Parental Level of Education",
        options=[
            "associate's degree",
            "bachelor's degree",
            "high school",
            "master's degree",
            "some college",
            "some high school",
        ],
    )
    lunch = st.selectbox("Lunch Type", options=["free/reduced", "standard"])
    test_preparation_course = st.selectbox(
        "Test Preparation Course", options=["none", "completed"]
    )

    reading_score = st.number_input(
        "Reading Score (out of 100)", min_value=0, max_value=100, step=1
    )
    writing_score = st.number_input(
        "Writing Score (out of 100)", min_value=0, max_value=100, step=1
    )

    # Submit button
    submit_button = st.form_submit_button("Predict Exam Scores")

# Process prediction when button is pressed
if submit_button:
    # Initialize data
    data = CustomData(
        gender=gender,
        race_ethnicity=ethnicity,
        parental_level_of_education=parental_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score,
    )

    # Get data as DataFrame
    pred_df = data.get_data_as_dataframe()

    # Make predictions
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)

    # Display prediction result
    st.success(f"The predicted Maths Score is {results[0]:.2f}")
