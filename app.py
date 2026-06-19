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

pages = {
 "Menu": [
  st.Page(page_menu, title="Menu", icon="🏠"),
 ],
 "Resources": [
  st.Page(page_1, title="Page 1", icon="📰"),
  st.Page(page_2, title="Page 2", icon="📰"),
 ],
 "Inscription / Connexion": [
  st.Page("inc_streamlit_app.py", title="**Login**", icon="📌"),
  st.Page("form.py", title="Formulaires", icon="📋"),
  st.Page("calendar.py", title="Calendrier", icon="📋"),
 ],
}

pg = st.navigation(pages)
pg.run()






