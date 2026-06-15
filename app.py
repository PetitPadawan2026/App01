import streamlit as st

animal_shelter = ['cat', 'dog', 'rabbit', 'bird']

animal = st.text_input('Type an animal')

if st.button('Check availability'):
    have_it = animal.lower() in animal_shelter
    'We have that animal!' if have_it else 'We don\'t have that animal.'

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
  
  

    
  
  
