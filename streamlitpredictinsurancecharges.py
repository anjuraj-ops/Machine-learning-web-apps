#!/usr/bin/env python
# coding: utf-8

# # Predict insurance charges based on a person's attributes

# In[1]:


import pickle
import numpy as np


# In[2]:


# load the model from disk
loaded_model = pickle.load(open('streamlit_insurance_predictcharges.pkl', 'rb'))


# In[3]:


import streamlit as st


# In[4]:


# Creating the Titles and Image
st.title("Predict insurance charges")
st.header("Calculating the insurance charges that could be charged by an insurer based on a person's attributes")


# In[5]:


import pandas as pd
def load_data():
    df = pd.DataFrame({'sex': ['Male','Female'],
                       'smoker': ['Yes', 'No']}) 
    return df
df = load_data()


# In[6]:


import pandas as pd
def load_data():
    df1 = pd.DataFrame({'region' : ['southeast' ,'northwest' ,'southwest' ,'northeast']}) 
    return df1
df1 = load_data()


# In[7]:


# Take the users input

sex = st.selectbox("Select Sex", df['sex'].unique())
smoker = st.selectbox("Are you a smoker", df['smoker'].unique())
region = st.selectbox("Which region do you belong to?", df1['region'].unique())
age = st.slider("What is your age?", 18, 100)
bmi = st.slider("What is your bmi?", 10, 60)
children = st.slider("Number of children", 0, 10)

# converting text input to numeric to get back predictions from backend model.
if sex == 'male':
    gender = 1
else:
    gender = 0
    
if smoker == 'yes':
    smoke = 1
else:
    smoke = 0
    
if region == 'southeast':
    reg = 2
elif region == 'northwest':
    reg = 3
elif region == 'southwest':
    reg = 1
else:
    reg = 0
    

# store the inputs
features = [gender, smoke, reg, age, bmi, children]
# convert user inputs into an array fr the model

int_features = [int(x) for x in features]
final_features = [np.array(int_features)]


# In[8]:


if st.button('Predict'):           # when the submit button is pressed
    prediction =  loaded_model.predict(final_features)
    st.balloons()
    st.success(f'Your insurance charges would be: ${round(prediction[0],2)}')
    

