# Stroke Risk Prediction System

A web-based application that predicts the likelihood of a stroke based on patient health parameters using a **Balanced Random Forest Classifier**. Built with **Python**, **Streamlit**, and **scikit-learn**, this tool allows healthcare professionals and individuals to assess stroke risk interactively.

## Features

* **Interactive UI**: Enter patient details such as age, gender, BMI, glucose level, medical history, and lifestyle factors.
* **End-to-End ML Pipeline**: Includes data preprocessing, feature encoding, and model prediction.
* **Balanced Random Forest**: Handles imbalanced datasets effectively for accurate stroke predictions.
* **Probability Output**: Displays the probability of stroke risk along with the prediction.
* **Custom UI Styling**: Beautiful background, font, and interactive input fields for enhanced user experience.
* **Header Image Support**: Add a custom image to make the app visually appealing.

## Technologies Used

* Python 3.x
* Streamlit
* pandas & numpy
* scikit-learn
* imbalanced-learn (for BalancedRandomForestClassifier)
* pickle (for saving/loading trained models)

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Place the dataset (`stroke.csv`) and optional header image (`header.jpg`) in the project folder.

## How to Run

1. Train the model

2. Launch the Streamlit app:

   ```bash
   streamlit run streamlit_app.py
   ```

3. The app will open in your default browser. Enter the patient details and click **Predict Stroke Risk** to see the results.


## Input Parameters

* **Age**: Patient’s age in years
* **Gender**: Male / Female
* **Hypertension**: Yes / No
* **Heart Disease**: Yes / No
* **Ever Married**: Yes / No
* **Work Type**: children / Govt_job / Never_worked / Private / Self-employed
* **Residence Type**: Urban / Rural
* **Average Glucose Level**: Blood glucose level
* **BMI**: Body Mass Index
* **Smoking Status**: never smoked / formerly smoked / smokes / Unknown

## Output

* **Prediction Result**: High Risk / Low Risk
* **Probability**: Likelihood of stroke as a percentage

## ⚠️ Disclaimer

This tool is designed for **educational and demonstration purposes only**. It is **not a substitute for professional medical advice**. Always consult a healthcare professional for accurate diagnosis and treatment.

## Screenshot

<img width="745" height="811" alt="image" src="https://github.com/user-attachments/assets/25c2e45c-7912-431c-b7f3-60a12b0ce57c" />

<img width="696" height="807" alt="image" src="https://github.com/user-attachments/assets/0299b005-b8dd-4784-b469-fac348edf4e3" />

