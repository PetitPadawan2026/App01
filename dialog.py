import streamlit as st

@st.dialog("Choisissez")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    if st.button("Ok"):
        vote("Ok")
    if st.button("Annuler"):
        vote("Annuler")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Veuillez cliquez")
    if st.button("Ok"):
        vote("Ok")
    if st.button("Annuler"):
        vote("Annuler")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"