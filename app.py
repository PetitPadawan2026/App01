import streamlit as st

if st.button(f'Coucou 🚗'):
  st.write("Comment était la course?"):
    myCont = st.container(horizontal=True, horizontal_alignment="center")
  with myCont:
    if st.button(f':+1:'):
      st.write="Super!"
    if st.button(f':-1:'):
      st.write="Bof"
st.write("Super" or "Bof")
  

    
  
  
