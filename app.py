import streamlit as st
test=False
if st.button(f'Coucou 🚗'):
  st.write("Comment était la course?")
  myCont = st.container(horizontal=True, horizontal_alignment="center")
  with myCont:
    if st.button(f':+1:'):
      st.write="Super!"
      test=True
    if st.button(f':-1:'):
      st.write="Bof"
      test=True
st.write()
  
  

    
  
  
