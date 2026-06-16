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
    "Rate the race",
    options=[
        "1",
        "2",
        "3",
        "4",
        "5",
    ],
)
st.write("My favorite number is", color)  

cars = ["Ferrari", "Mclaren", "Porsche"]
action = st.menu_button("Quel est ta voiture préféré", options=cars)
try:
  st.write(f"Ta voiture préféré est => {action}")
except:
  pass
  
if action == "Ferrari":
    st.write("Ta voiture préféré est Ferrari")
elif action == "Mclaren":
    st.write("Ta voiture préféré est Mclaren")
elif action == "Porsche":
    st.write("Ta voiture préféré est Porsche")

    
  
  
