import streamlit as st

if st.button(f'Coucou 🚗'):
  st.write("Comment était la course?")
  myCont = st.container(horizontal=True, horizontal_alignment="center")
  answer=""
  with myCont:
    if st.button(f':+1:'):
      answer="Super!"
    if st.button(f':-1:'):
      answer="Bof"
  st.write(f'{answer}')
  
    
  
  
