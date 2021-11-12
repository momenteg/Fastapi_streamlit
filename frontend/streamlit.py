import requests
import streamlit as st
import json

st.title("Iris classification Web App")


with st.form("key1"):
    col1, col2, col3, col4 = st.columns(4)
    # ask for input
    petal_l = col1.text_input("Petal length")
    petal_w = col2.text_input("Petal width")
    sepal_w = col3.text_input("Sepal width")
    sepal_l = col4.text_input("Sepal length")
    
    button_check = st.form_submit_button("Submit")

    if button_check:
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        payload = {"sepal_l": sepal_l, "sepal_w": sepal_w, "petal_l": petal_l , "petal_w": petal_w}
        response = requests.get('http://fastapi:8080/predict/', headers=headers, data=json.dumps(payload))


        if response.status_code == 200:
            json_data = json.loads(response.text)
            st.success("Match found")
            st.write('Iris Type is: ', json_data['type_class'])
            st.write('CL is: ', json_data['probability'])
        else: 
            st.error('Something went wrong!')





