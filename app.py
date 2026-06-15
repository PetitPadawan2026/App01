import streamlit as st

if st.button(f'Coucou 🚗'):
  st.write("Comment était la course?")
  myCont = st.container(horizontal=True, horizontal_alignment="center")
  with myCont:
    if st.button(f':+1:'):
      st.session_state.answer="Super!"
    if st.button(f':-1:'):
      st.session_state.answer="Bof"
st.write(st.session_state.answer)
  
    
  
  
