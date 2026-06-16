import streamlit as st

test=False
notes=["1","2","3","4","5"]
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

def build_slider(label="Demo",values=[]):
  return st.select_slider(
    label,
    options=values,
  )


color = build_slider("Rate the Race",notes)

st.write("My favorite number is", color)  

cars = ["Ferrari", "Mclaren", "Porsche"]
action = st.menu_button("Quel est ta voiture préféré", options=cars)
try:
  if action is not None:
    st.write(f"Ta voiture préféré est {action}")
except:
  pass

demo = build_slider("Vroums",cars)
tab1, tab2, tab3 = st.tabs(cars)



agree = st.checkbox("I agree")

if agree:
 st.write ("Great")







