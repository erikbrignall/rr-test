import pandas as pd
import streamlit as st

st.set_page_config(page_title='Risk Rating Estimation - DEMO')
st.title('RR Estimation - DEMO')
st.write('The following is a demo of using streamlit as an interface for a vehicle RR app.')
st.write('this is a test')

# Input Query
with st.form(key='my_form_to_submit'):
    st.write('Please fill the attributes for the vehicle for estimation')
    query_text = st.text_input('Vehicle Name')
    cc = st.number_input('Vehicle CCs', min_value=1, max_value=10000, value=1600)
    total_length = st.number_input('Total Length (cm)', min_value=1000, max_value=6000, value=4200)
    total_width = st.number_input('Total Width (cm)', min_value=120, max_value=2200, value=1800)
    kerb_weight = st.number_input('Kerb Weight (kg)', min_value=100, max_value=10000, value=1600)
    torque = st.number_input('Torque (Nm)', min_value=1, max_value=10000, value=200)
    max_speed = st.slider('Max Speed (mph)', min_value=28, max_value=220, value=125)
    acceleration = st.number_input('Acceleration 0-60', min_value=1, max_value=20, value=8)
    power = st.number_input('Power (hp)', min_value=1, max_value=1500, value=150)
    list_price = st.slider('List Price (£)', min_value=1000, max_value=10000000, value=30000)
    impact_parts_front = st.slider('Impact Parts Cost Front', min_value=1, max_value=10, value=5)
    submit_button = st.form_submit_button(label='Submit')

if submit_button: 
    inputs = ['cc','total_length','total_width','kerb_weight','torque','max_speed','acceleration','power','list_price','impact_parts_front']
    #inputs = ['cc','total_length','total_width','kerb_weight','torque','max_speed']
    st.write("your inputs are")
    st.write(inputs)
