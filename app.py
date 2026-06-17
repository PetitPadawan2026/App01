import streamlit as st
import datetime
 
test=False
notes=["1","2","3","4","5"]

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

def build_slider(label="Demo",values=[]):
  return st.select_slider(
    label,
    options=values,
  )


def page2_cont():
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


def page_1():
 st.write("***Page 1***")
 page1_cont()
  
def page_2():
  st.write("Page 2")
  page2_cont()

def page_menu():
  st.title("Menu")

def page_take_rdv():
  st.title("Prendre rendez-vous")
  d = st.date_input("Quand voulait vous prendre un rendez-vous ?", datetime.date(2010, 4 , 3 ))
  st.write("Votre rendez-vous est prévue le:", d)

#pg = st.navigation([page_1, page_2])
#pg.run()

pages = {
 "Menu": [
  st.Page(page_menu, title="Menu", icon="🏠"),
 ],
 "Resources": [
  st.Page(page_1, title="Page 1", icon="📰"),
  st.Page(page_2, title="Page 2", icon="📰"),
  st.Page(page_take_rdv, title="Prendre rendez-vous", icon="📋"),
  st.Page("calendar.py", title="Calendrier", icon="📋"),
 ],
}

pg = st.navigation(pages)
pg.run()



sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    st.write("Merci pour votre réponse") 



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
