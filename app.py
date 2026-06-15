import streamlit as st

test=False
st.write('Comment était la course?')
myCont = st.container(horizontal=True, horizontal_alignment="center")
with myCont:
  if st.button(f':+1: a'):
    st.write('Super!')
    test=True
  if st.button(f':-1: a'):
    st.write('Bof')
    test=True
with st.container(horizontal=True, horizontal_alignment="center"):
    'Super' if test else 'bof'
  
  

    
  
  
