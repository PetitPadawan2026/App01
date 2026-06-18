import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng


def page1_cont():
  st.write('Comment était la course?')
  myCont = st.container(horizontal=True, horizontal_alignment="center")
  test=False
  with myCont:
    if st.button(f':+1:'):
      #st.write('Super!')  
      test=True
    if st.button(f':-1:'):
      #st.write('Bof')
      test=False
  with st.container(horizontal=True, horizontal_alignment="center"):
      'Super' if test else 'bof'



color = build_slider("Rate the Race",notes)
  st.write("My favorite number is", color)  

  cars = [":red [Ferrari]", "Mclaren", "Porsche", "Aston Martin","Alpine", "Cadillac" , "Peugeot" , "Toyota" ]
  action = st.menu_button("Quel est ta voiture préféré", options=cars)
  try:
    if action is not None:
      st.write(f"Ta voiture préféré est {action}")
  except:
    pass

  demo = build_slider("Vroums",cars)
  tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(cars)
  agree = st.checkbox("I agree")
  genre = st.radio(
      ":rainbow[Are you sure ?]",
      ["I'm sure", "I'm not sure"],
    )
    
  if genre == "I'm sure":
    st.write("Great!")
  else:
    st.write("Please select", "I'm sure")
    st.snow()





df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.line_chart(
    df,
    x="a",
    y=["b", "c"],
    color=["#FF0000", "#0000FF"],


 

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    st.write("Merci pour votre réponse") 

)


 #Sélectionner un niveau pour l'élève
option = st.selectbox(
    "Quel est le niveau de votre fils ?",
    ("Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4", "Niveau 5"),
    index=None,
    placeholder="Select contact method...",
)
st.write("You selected:", option)


# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Je n'accepte pas", key="disabled")
    st.checkbox("J'accepte")

with col2:
    st.radio(
        "Votre nage préférée 👇",
        ["Brasse", "Crawl", "Papillon"],
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    ) 

