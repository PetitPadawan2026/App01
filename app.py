import streamlit as st

answer=None
if 'answer' not in st.session_state:
    st.session_state.answer=""
if st.button(f'Coucou 🚗'):
  st.write("Comment était la course?")
  myCont = st.container(horizontal=True, horizontal_alignment="center")
  with myCont:
    if st.button(f':+1:'):
      st.session_state.answer="Super!"
    if st.button(f':-1:'):
      st.session_state.answer="Bof"
    st.toast(st.session_state.answer)
st.write(st.session_state.answer)
  
    
  
  
