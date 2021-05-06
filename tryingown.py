import streamlit as st
from configu import *
import webcam

st.sidebar.header(PROJECT_NAME)
st.sidebar.write(DONE_BY)


st.sidebar.header(PRESS1)
btn = st.sidebar.button('ABOUT')
if btn:
    st.title("ABOUT OUR PROJECT")
    st.info('''By developing a face mask detection technique,
through which we identify people weared mask 
or not. so we suggest people who not weared
 mask to wear  it to reduce the covid/ any viral
 disease spread''')




st.sidebar.header(PRESS2)
btn = st.sidebar.button('INSTRUCTION')
if btn:
    st.title("INSTRUCTION TO USE")




st.sidebar.header(PRESS3)
btn = st.sidebar.button('DATASET')
if btn:
    st.title("SAMPLE DATASET OF OUR PROJECT")



st.sidebar.header(PRESS4)
btn = st.sidebar.button('VIDEO BASED TEST')
if btn:
    st.title("VIDEO BASED TEST")




st.sidebar.header(PRESS5)
btn1 = st.sidebar.button('CAMERA BASED TEST')
if btn1:
    st.title("CAMERA BASED TEST")
    btn2 = st.button('start realtime AI camera')
    if btn2:
        webcam.load_camera(num=0)