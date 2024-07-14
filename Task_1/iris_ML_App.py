import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier


# -----> Sidebar 
st.sidebar.header("🪻Iris-Flower Classification")
st.sidebar.write("──────── ⋆⋅☆⋅⋆ ─────────")
st.sidebar.header('User Input Parameters')

# -----> User inputs 
def user_input_features():
    sepal_len = st.sidebar.slider(label='sepal length (cm)', min_value=4.3, max_value=7.9, value=5.4)
    sepal_wid = st.sidebar.slider(label='sepal width (cm)', min_value=2.0, max_value=4.4, value=3.4)
    petal_len = st.sidebar.slider(label='petal length (cm)', min_value=1.0, max_value=6.9, value=1.3)
    petal_wid = st.sidebar.slider(label='petal width (cm)', min_value=0.1, max_value=2.5, value=0.2)
    
    data = {
        'sepal length (cm)': sepal_len,
        'sepal width (cm)': sepal_wid,
        'petal length (cm)': petal_len,
        'petal width (cm)': petal_wid
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()


iris = datasets.load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

clf = RandomForestClassifier()
clf.fit(x, y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)


st.sidebar.write("## 🪻🪻🪻🪻🪻🪻🪻🪻🪻🪻")
st.sidebar.subheader('Class labels with index numbers',divider='grey')
for index, name in enumerate(iris.target_names):
    st.sidebar.write(f"**:grey[{index} → {name}]**")


# -----> Main page 
st.write("""
         # 🪻 Iris Flower Prediction App
         ꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷
         ###### :grey[This app predicts the :red[***Iris Flower***] type]!     
         """)
"---"


st.subheader(':green[User Input Parameters]')
st.dataframe(df, width=700, use_container_width=False)


with st.container(border=True):
    st.subheader('Prediction',divider='rainbow')
    result = iris.target_names[prediction][0]
    if result == 'setosa':
        st.success('The flower is a Setosa')
        st.image("setosa_species.jpg")
    elif result == 'versicolor':
        st.success('The flower is a Versicolor')
        st.image("versicolor_species.jpg")
    else:
        st.success('The flower is a Virginica')
        st.image("virginica_species.jpg", width=650, use_column_width=False)

    st.subheader('Prediction Probability',divider='rainbow')
    st.dataframe(prediction_proba, width=700, use_container_width=False)
