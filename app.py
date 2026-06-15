import streamlit as st

test=False
st.write('Comment était la course?')
myCont = st.container(horizontal=True, horizontal_alignment="center")
with myCont:
  if st.button(f':+1:'):
    #st.write('Super!') 
    test=True
  if st.button(f':-1:'):
    #st.write('Bof')
    test=False
with st.container(horizontal=True, horizontal_alignment="center"):
    'Super' if test else 'bof'



color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
    ],
)
st.write("My favorite number is", color)  
  

    
  
  
