import pandas as pd 
import numpy as np 
import streamlit as st 
import joblib 

st.header('email spam detection model ')
model = joblib.load('spam_ham_model.pkl')
vectroizer = joblib.load('vectorizer1.pkl')
email=st.text_input('enter ythe email content here ')
if st.button('predict'):
    if email.strip()=="":
        st.warning('please enter email text')
    else:
        vector_email = vectroizer.transform([email])

        prediction=model.predict(vector_email)

        if prediction[0] == 'spam':
          st.error('your email is a spam email')
        else:
          st.success("your email is ham email")
