import streamlit as st

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button(state=False):
    st.session_state.clicked = state

myCont = st.container(horizontal=True, horizontal_alignment="center")

#st.button('Click me', on_click=click_button)
if st.button(f'Coucou'):
  st.write("Comment était la course?")
  with myCont:
    st.button(f':+1:', on_click=click_button(True))
    st.button(f':-1:', on_click=click_button(False))

if st.session_state.clicked:
    # The message and nested widget will remain on the page
    'Super' if st.session_state.clicked else 'bof'

if 1 == 2:
  test=False
  if st.button(f'Coucou 🚗'):
    st.write("Comment était la course?")
    myCont = st.container(horizontal=True, horizontal_alignment="center")
    with myCont:
      if st.button(f':+1: a'):
        st.write="Super!"
        test=True
      if st.button(f':-1: a'):
        st.write="Bof"
        test=True
  if test:
    st.write("Yeah")
  
  

    
  
  
