import streamlit as st

if st.button(f'Coucou 🚗'):
  st.write("Comment était la course?")
  if st.button(f':+1:'):
    st.write("Super!")
  if st.button(f':-1:'):
    st.write("Bof")
  
  
