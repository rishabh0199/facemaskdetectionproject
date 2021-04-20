import streamlit as st
from config import *
import webcam

st.sidebar.header(PROJECT_NAME)
st.sidebar.write(DONE_BY)

choice = st.sidebar.radio("select option",MENU_OPTION)

if choice == 'About project':
    st.title("About Our Project")
    st.info('''By developing a face mask detection technique,
through which we identify people weared mask 
or not. so we suggest people who not weared
 mask to wear  it to reduce the covid/ any viral
 disease spread''')


if choice == 'Instruction to use':
    st.title("how to use application")


if choice == 'Sample dataset':
    st.title("Datset sample")


if choice == 'Video based test':
    st.title("video based test")


if choice == 'Camera based test':
    btn = st.button('start realtime AI camera')
    if btn:
        webcam.load_camera(num=0)