import streamlit as st
import pandas as pd
import numpy as np
import pickle
import streamlit as st

st.markdown('<h1 style="color: red;">Web Application for Credit Risk</h1>', unsafe_allow_html=True)
Credit_History = st.selectbox('Credit_History', (1, 0))
Gender=st.selectbox('Sexe',('Male','Female'))
Married=st.selectbox('Marié',('Yes','No'))
Dependents=st.selectbox('Enfants',('0','1','2','3'))
Education=st.selectbox('Education',('Graduate','Not Graduate'))
Self_Employed=st.selectbox('Salarié ou Entrepreneur',('Yes','No'))
ApplicantIncome=st.slider('Salaire du client',0,25000,200)
CoapplicantIncome=st.slider('Salaire du conjoint',0,25000,1000)
Property_Area=st.selectbox('Property_Area',('Urban','Rural'))

data={
    'Gender':Gender,
    'Married':Married,
    'Dependents':Dependents,
    'Education':Education,
    'Self_Employed':Self_Employed,
    'ApplicantIncome':ApplicantIncome,
    'CoapplicantIncome':CoapplicantIncome,
    'Credit_History':Credit_History,
    'Property_Area':Property_Area
    }

if data['Gender'] == 'Male':
        data['Gender'] = 1
else:
        data['Gender'] =0

if data['Married'] == 'No':
        data['Married'] = 0
else:
        data['Married'] = 1

if data['Education'] == 'Graduate':
        data['Education'] = 0
else:
        data['Education'] = 1

if data['Self_Employed'] == 'No':
        data['Self_Employed'] = 0
else:
        data['Self_Employed'] = 1

if data['Property_Area'] == 'Urban':
        data['Property_Area'] = 0
else:
        data['Property_Area'] = 1


profil_client=pd.DataFrame(data,index=[0])
input_df=profil_client


X=pickle.load(open('X.pkl','rb'))
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
X=min_max_scaler.fit_transform(X)
input_df1= min_max_scaler.transform(input_df)  


load_model=pickle.load(open('prevision_data.pkl','rb'))
prevision=load_model.predict(input_df)

if st.button('Checked Me'):
     if prevision==0:
             st.success("we can take the money")
             image="image/img1.png"
             st.image(image)
     else:
             st.error("we can't take you any money ")
             image="image/img2.png"
             st.image(image)
