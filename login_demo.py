import streamlit as st

st.title("Request manager")

st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}

if st.session_state.role in ["Requester", "Admin"]:
    page_dict["Request"] = request_pages
if st.session_state.role in ["Responder", "Admin"]:
    page_dict["Respond"] = respond_pages
if st.session_state.role == "Admin":
    page_dict["Admin"] = admin_pages
  
if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)

else:
    pg = st.navigation([st.Page(login)])

pg.run()
