import os
import pickle
import warnings
import streamlit as st

warnings.filterwarnings("ignore")

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide",page_icon="🧑‍⚕️")

working_dir = os.path.dirname(os.path.abspath(__file__))

diabetics_model = pickle.load(open(f'{working_dir}/saved_models/diabetics_model.sav','rb'))


st.sidebar.header("Diabetes Prediction App")
st.sidebar.write("────── ⋆⋅:🌟:⋅⋆ ───────")       

st.title('Diabetes Prediction using Machine learning.')


with st.form(key="my_form",clear_on_submit=True):
    col1, col2, col3 = st.columns(3)
    with col1:
      Pregnancies = st.slider('Number of Pregnancies',0,30,3)
    with col2:
      Glucose = st.slider('Glucose Level',0,600,85,help='Normal fasting blood glucose level is between 70 and 100 mg/dL')
    with col3:
      BloodPressure = st.slider('Blood Pressure value',0,600,120,help='Normal bp is 120/80 or lower. 120 ')
    with col1:
      Insulin = st.number_input('Insulin Level')
    with col2:
      SkinThickness = st.number_input(label='Skin Thickness Value')
    with col3:
      BMI = st.number_input('BMI value')
    with col1:
      DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value')
    with col2:
      Age = st.slider("Age of the person",0,100,35)
    
    diab_diagnosis = "☝️ Results will displayed here...."
    if st.form_submit_button("Results", type='primary'):
      user_input =[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
      if "" in user_input:
            st.error("Please fill, all the details....",icon="😓")
            
      else:  
        user_input = [float(x) for x in user_input]    
        diab_prediction = diabetics_model.predict([user_input])
        
        if diab_prediction[0] == 1:
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
      # else:
        # st.error("Please fill, all the details correctly(must be in numbers)....",icon="😓")
    st.success(diab_diagnosis)
    
with st.expander("Want to know more about the parameters.",icon=":material/unfold_more:"):
  st.header("Overview", divider='rainbow')
  st.write("This model will predict the diabetes based on the parameters: :green[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]")
    
  with st.container(border=True):
    Pregnancies_tab, Glucose_tab, BloodPressure_tab, SkinThickness_tab, Insulin_tab, BMI_tab, DiabetesPedigreeFunction_tab, Age_tab = st.tabs(['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
        
    with Pregnancies_tab:
      st.subheader("Pregnancies", divider='green')
      st.write("The number of times a woman has been pregnant.")

      with st.container(border=True):
        st.subheader("Relationship Between Number of Pregnancies and Diabetes",divider='green')
        st.write("""
        This page provides detailed information on how the number of pregnancies relates to diabetes, including the impact on gestational diabetes, physiological changes during pregnancy, long-term risks, and the use of this parameter in diabetes prediction models.
        """)
        c1, c2, c3 = st.columns(3,vertical_alignment='top')
        with c1:
          # Gestational Diabetes Section
          st.write("##### Gestational Diabetes")
          st.write("""
          - **Definition:** Gestational diabetes is a type of diabetes that develops during pregnancy. It usually goes away after the baby is born, but it increases the mother's risk of developing type 2 diabetes later in life.
          - **Risk Factor:** Women with multiple pregnancies have a higher risk of developing gestational diabetes in subsequent pregnancies due to changes in the body's insulin response.""")
        with c2:
          # Physiological Changes During Pregnancy
          st.write("##### Physiological Changes During Pregnancy")
          st.write("""
          - **Hormonal Changes:** Pregnancy induces hormonal changes that can affect insulin sensitivity. Increased levels of hormones like estrogen, progesterone, and placental lactogen can interfere with insulin's ability to regulate blood sugar.
          - **Increased Insulin Resistance:** As pregnancy progresses, insulin resistance increases to ensure the growing fetus has enough glucose. In some women, the pancreas cannot produce enough insulin to overcome this resistance, leading to gestational diabetes.
          """)
        with c3:
          # Long-Term Impact on Diabetes Risk
          st.write("##### Long-Term Impact on Diabetes Risk")
          st.write("""
          - **Future Risk:** Women who have had gestational diabetes are more likely to develop type 2 diabetes later in life. The risk increases with each subsequent pregnancy where gestational diabetes occurs.
          - **Family History and Genetics:** A history of gestational diabetes may indicate a genetic predisposition to insulin resistance and diabetes, affecting multiple pregnancies.
          """)


    with Glucose_tab:
      st.subheader(body="Glucose Level",divider='green')
      st.write("""
      This page provides detailed information on glucose levels for diabetes prediction, including normal levels, diabetic levels, and precautions for managing diabetes.
      """)
      with st.container(border=True):
        # Glucose Levels Section
        st.subheader("Glucose Levels for Diabetes Prediction",divider='green')
        c1, c2 ,c3 = st.columns(3,vertical_alignment='center')
        with c1:
            # Normal Glucose Levels
            st.write("##### Normal Glucose Levels")
            st.write("""
            - **Fasting Blood Sugar (FBS):** 
              - **Normal Range:** 70-99 mg/dL (milligrams per deciliter)
            - **Postprandial Blood Sugar (PPBS) (2 hours after eating):** 
              - **Normal Range:** Less than 140 mg/dL
            - **HbA1c (Hemoglobin A1c):**
              - **Normal Range:** Less than 5.7%
            """)
        with c2:
            # Prediabetes Glucose Levels
            st.write("##### Prediabetes Glucose Levels")
            st.write("""
            - **Fasting Blood Sugar (FBS):** 
              - **Range:** 100-125 mg/dL
            - **Postprandial Blood Sugar (PPBS):** 
              - **Range:** 140-199 mg/dL
            - **HbA1c:**
              - **Range:** 5.7% to 6.4%
            """)
        with c3:
            # Diabetes Glucose Levels
            st.write("##### Diabetes Glucose Levels")
            st.write("""
            - **Fasting Blood Sugar (FBS):** 
              - **Range:** 126 mg/dL or higher on two separate tests
            - **Postprandial Blood Sugar (PPBS):** 
              - **Range:** 200 mg/dL or higher
            - **HbA1c:**
              - **Range:** 6.5% or higher
            """)
        
    with BloodPressure_tab:
      st.subheader("Blood Pressure", divider="green")
      
      st.write("""
      This page provides detailed information on how blood pressure relates to diabetes, including normal and high blood pressure levels, the impact of high blood pressure on diabetes, and tips for managing both conditions.
      """)
      with st.container(border=True):
        st.subheader("Relationship Between Blood Pressure and Diabetes",divider='green')
        
        c1, c2 =st.columns(2)
        with c1:
            # Normal Blood Pressure Levels
            st.write("##### Normal Blood Pressure Levels")
            st.write("""
            - **Systolic Blood Pressure (SBP):** 
              - **Normal Range:** Less than 120 mmHg
            - **Diastolic Blood Pressure (DBP):** 
              - **Normal Range:** Less than 80 mmHg
            """)
        with c2:
            # High Blood Pressure (Hypertension) Levels
            st.write("##### High Blood Pressure (Hypertension) Levels")
            st.write("""
            - **Stage 1 Hypertension:**
              - **Systolic:** 130-139 mmHg
              - **Diastolic:** 80-89 mmHg
            - **Stage 2 Hypertension:**
              - **Systolic:** 140 mmHg or higher
              - **Diastolic:** 90 mmHg or higher
            """)
        # Impact of High Blood Pressure on Diabetes
        st.subheader("Impact of High Blood Pressure on Diabetes",divider='green')
        st.write("""
        High blood pressure and diabetes often occur together and can significantly increase the risk of complications:
        - **Increased Cardiovascular Risk:** Both conditions independently raise the risk of heart disease, and their combination multiplies this risk.
        - **Kidney Damage:** High blood pressure can damage blood vessels in the kidneys, worsening diabetic nephropathy.
        - **Vision Problems:** Hypertension can aggravate diabetic retinopathy, leading to vision loss.
        - **Nerve Damage:** Both high blood pressure and diabetes can damage nerves, leading to neuropathy.
        """)
    with SkinThickness_tab:
      st.subheader("SkinThickness",divider = 'green')       
      # SkinThickness Section
      st.write("""
      Skin thickness is measured using the triceps skinfold thickness.
      - **Normal Range:** 10-50 mm
      """)
          
    with Insulin_tab:
      st.subheader("Insulin",divider='green')
      st.write("""
      Insulin levels measure the amount of insulin in the blood.
      - **Normal Range:** 16-166 µU/mL (microunits per milliliter)
      - **Postprandial (After Meal):** 60-180 µU/mL
      """)


    with BMI_tab:
      # BMI Section
      st.subheader("BMI (Body Mass Index)",divider='green')
      st.write("""
      BMI is a measure of body fat based on height and weight.
      - **Underweight:** BMI < 18.5
      - **Normal Weight:** BMI 18.5-24.9
      - **Overweight:** BMI 25-29.9
      - **Obesity:** BMI 30 or higher
      """)


    with DiabetesPedigreeFunction_tab:
      st.subheader("Diabetes Pedigree Function",divider='green')
      st.write("""
      The Diabetes Pedigree Function provides an estimate of diabetes risk based on family history.
      - **Typical Range:** 0-2.5
      - **Higher Values Indicate:** Greater risk of diabetes
      """)

    with Age_tab:
      # Age Section
      st.subheader("Age",divider='green')
      st.write("""
      Age of the individual in years.
      - **Typical Range in Studies:** 21-81 years
      - **Higher Age:** Associated with increased risk of diabetes
      """)
        


           