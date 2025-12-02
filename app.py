# app.py
import streamlit as st
import api
import os

container = os.getenv("DOCKER_CONTAINER", False)



st.title("Hello World 🎈")
st.header("Am I inside a container?")
if container:
    st.write("I am!!! 🥳")
else:
    st.write("I don't think so... 😶‍🌫️")
c1, c2 = st.columns(2)
with c1:
    st.subheader("Machine info")
    st.markdown(f"""
    - **System:** {api.uname.system}
    - **Node Name:** {api.uname.node}
    - **Release:** {api.uname.release}
    - **Machine:** {api.uname.machine}
    - **Processor:** {api.uname.processor}
    """)


with c2:
    # Add a simple interactive element
    name = st.text_input("What's your name?")
    if name:
        st.write(f"Hello, {name}!")

    # Add a button
    if st.button("Some ballons!"):
        st.balloons()
