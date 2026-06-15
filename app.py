import streamlit as st

answer=None
if 'answer' not in st.session_state:
    st.session_state.answer="init"
if st.button(f'Coucou 🚗'):
  st.write("Comment était la course?")
  myCont = st.container(horizontal=True, horizontal_alignment="center")
  with myCont:
    if st.button(f':+1:'):
      st.session_state.answer="Super!"
      st.toast(f'Answer={st.session_state.answer}', icon="😍")
    if st.button(f':-1:'):
      st.session_state.answer="Bof"
      st.toast(f'Answer={st.session_state.answer}', icon="😍")
st.write(st.session_state.answer)
  
    
  
  
