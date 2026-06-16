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

your-repository/
├── pages/
│   ├── page_1.py
│   └── page_2.py
└── your_app.py

st.page_link("your_app.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")
    
  
  
