import streamlit as st
import datetime
 
test=False
notes=["1","2","3","4","5"]


def build_slider(label="Demo",values=[]):
  return st.select_slider(
    label,
    options=values,
  )


def page_1():
 st.header("Page 1")
  
def page_2():
  st.header("Page 2")

def page_menu():
  st.title("Menu")

#pg = st.navigation([page_1, page_2])
#pg.run()

pages ={
 "Menu": [
  st.Page(page_menu, title="Menu", icon="🏠"),
 ],
 "Inscription / Connexion": [
  st.Page("inc_streamlit_app.py", title="**Login**", icon="📌"),
  st.Page("form.py", title="Formulaires", icon="📋"),
 ],
"Réservation":[
  st.Page("calendar.py", title="Calendrier", icon="📋"),
  st.Page("dialog.py", title="Dialogue", icon="📋"),
  st.Page("resa.py", title="Reservation", icon="📋"),

 ] 
}


pg = st.navigation(pages)
pg.run()
