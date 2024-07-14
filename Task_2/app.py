import os
import pickle
import warnings
import streamlit as st
import time
import random
import streamlit_lottie
import json


warnings.filterwarnings("ignore")

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

working_dir = os.path.dirname(os.path.abspath(__file__))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

st.sidebar.header(":heart: Heart Disease Prediction App")
st.sidebar.write("───────── ⋆⋅:heart:⋅⋆ ───────────")

healthy_heart_tips = [
    "Maintain a Healthy Diet: Eat a variety of nutrient-rich foods, including fruits, vegetables, whole grains, and lean proteins.",
    "Stay Physically Active: Aim for at least 30 minutes of moderate exercise most days of the week.",
    "Avoid Smoking: Smoking is a major risk factor for heart disease. Seek help to quit if necessary.",
    "Limit Alcohol Intake: Drink alcohol in moderation, if at all. Excessive drinking can lead to heart problems.",
    "Monitor Blood Pressure: Keep track of your blood pressure and seek medical advice if it's consistently high.",
    "Maintain a Healthy Weight: Being overweight can increase your risk of heart disease. Aim for a healthy weight through diet and exercise.",
    "Manage Stress: Practice relaxation techniques like yoga, meditation, or deep breathing to manage stress.",
    "Get Regular Health Screenings: Regular check-ups can help detect risk factors early.",
    "Stay Hydrated: Drink plenty of water throughout the day to stay hydrated and support overall health.",
    "Get Enough Sleep: Aim for 7-9 hours of quality sleep per night to support heart health."
]

def choice_tip():
            random_tip = random.choice(healthy_heart_tips)
            st.write(random_tip)
                     
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

bg_file = load_lottiefile('video/bg.json')
healthy_heart =load_lottiefile("video/healthy.json")
diseased_heart = load_lottiefile("video/diseased.json")


with st.sidebar:
    streamlit_lottie.st_lottie(bg_file,speed=5, loop=True,quality='medium',reverse=False)
    st.header('Tip of the Day', divider='rainbow')
    with st.container(border=True):
        choice_tip()
        st.sidebar.button("New Tip")
        
        
        
     
        
st.header('Heart Disease Prediction using ML', divider='rainbow')

with st.form(key="my_form", clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.slider('Age', 1, 100, 30, help='Select your age')
    with col2:
        sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Male' if x == 0 else 'Female', help='Select your sex')
    with col3:
        choice = st.selectbox('Chest Pain Types (CP)', options=["Asymptomatic", "Atypical Angina", "Typical Angina", "Non-Angina"], help='0: Asymptomatic, 1: Atypical Angina, 2: Typical Angina, 3: Non-Angina')
        
        if choice == "Asymptomatic":
            cp = 0
        elif choice == "Atypical Angina":
            cp = 1
        elif choice == "Typical Angina":
            cp = 2
        elif choice == "Non-Angina":
            cp = 3

    with col1:
        trestbps = st.number_input('Resting Blood Pressure (TRTBPS)', min_value=0, help='Enter your resting blood pressure in mmHg')

    with col2:
        chol = st.number_input('Serum Cholesterol in mg/dl (Chol)', min_value=0, help='Enter your serum cholesterol level')

    with col3:
        choice = st.selectbox('Fasting Blood Sugar (FBS)', options=["FBS > 120 mg/dl", "FBS <= 120 mg/dl"], help='Select Your BP')
        
        if choice == "FBS > 120 mg/dl":
            fbs = 0
        elif choice == "FBS <= 120 mg/dl":
            fbs = 1
            
    with col1:
        choice = st.selectbox('Resting Electrocardiographic Results (Rest ECG)', options=["Normal", "ST Elevation","Others" ], help='0: Normal, 1: ST Elevation, 2: Others')
        
        if choice == "Normal":
            restecg = 0
        elif choice == "ST Elevation":
            restecg = 1
        elif choice == "Others":
            restecg = 2
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved (Thalachh)', min_value=0, help='Enter your maximum heart rate achieved')

            
    with col3:
        choice = st.selectbox('Exercise Induced Angina (Exng)', options=["Yes", "No"], help='1: Yes, 0: No')
        
        if choice == "Yes":
            exang = 1
        elif choice =='No':
            exang = 0
        
    with col1:
        oldpeak = st.number_input('ST Depression Induced by Exercise (Oldpeak)', min_value=0.0, format="%.2f", help='Enter the ST depression value')

            
    with col2:
        choice = st.selectbox('Slope of the Peak Exercise ST Segment (Slope)', options=["Flat", "Up Sloping", "Down Sloping"], help='0: Flat, 1: Up Sloping, 2: Down Sloping')
        
        if choice == "Flat":
            slope = 0
        elif choice =="Up Sloping":
            slope = 1
        elif choice == "Down Sloping":
            slope = 2
            
    with col3:
        ca = st.selectbox('Number of Major Vessels (CA)', options=[0, 1, 2, 3], help='Number of major vessels colored by fluoroscopy')

    with col1:
        choice = st.selectbox('Thalassemia (thal)', options=["Normal", "Fixed Defect", "Reversible Defect"], help='1: Normal, 2: Fixed Defect, 3: Reversible Defect')
        
        if choice =="Normal":
            thal = 1
        elif choice =="Fixed Defect":
            thal = 2
        elif choice =="Reversible Defect":
            thal = 3

    # Prediction
    heart_diagnosis = "☝️ Results will be displayed here...."

    # Prediction button
    if st.form_submit_button("Results", type='primary'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        if any(x is None or x == '' for x in user_input):
            st.error("Please fill in all the details....", icon="🥲")
        else:
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_disease_model.predict([user_input])
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
                streamlit_lottie.st_lottie(diseased_heart,speed=1, loop=True,quality='medium',reverse=False,height=300)
            else:
                heart_diagnosis = 'The person does not have any heart disease'
                streamlit_lottie.st_lottie(healthy_heart,speed=1, loop=True,quality='medium',reverse=False,height=300)
    
    st.success(heart_diagnosis)
