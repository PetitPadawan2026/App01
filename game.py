import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng



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
