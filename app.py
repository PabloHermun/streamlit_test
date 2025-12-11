import streamlit as st

st.header("Flip a coin")

number_of_trials = st.slider('¿Number of throws?', 1, 1000, 10)
start_button = st.button('Execute')

if start_button:
    st.write(f'Experiment with {number_of_trials} trials in progress')

st.write("This app is under construction.")
