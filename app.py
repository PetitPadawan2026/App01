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

cars = ["Ferrari", "Mclaren", "Porsche", "Aston Martin","Alpine", "Cadillac" , "Peugeot" , "Toyota" ]
action = st.menu_button("Quel est ta voiture préféré", options=cars)
try:
  if action is not None:
    st.write(f"Ta voiture préféré est {action}")
except:
  pass

demo = build_slider("Vroums",cars)
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(cars)


agree = st.checkbox("I agree")

def page_1():
  st.title("***Page 1***")

  genre = st.radio(
    ":rainbow[Are you sure ?]",
    ["I'm sure", "I'm not sure"],
  )
  
  if genre == "I'm sure":
    st.write("Great!")
    st.balloons()
  else:
    st.write("Please select", "I'm sure")
    st.snow()

def page_2():
  st.title("Page 2")

pg = st.navigation([page_1, page_2])
pg.run()





