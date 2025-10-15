# app.py
import streamlit as st

st.title("Hello World")
st.write("I'm inside a container!")

# Add a simple interactive element
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

# Add a button
if st.button("Click me!"):
    st.balloons()