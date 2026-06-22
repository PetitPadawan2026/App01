import streamlit as st

if "vote" not in st.session_state:
    st.session_state.vote=None

@st.dialog("Choisissez")
def vote():
    in_item = st.text_input("item")
    in_reason = st.text_input("reason")

    if st.button("Ok"):
        st.session_state.vote=("A voté")
        st.session_state.vote = {"item": in_item, "reason": in_reason}
        st.rerun()
    if st.button("Annuler"):
        st.session_state.vote=None
        st.rerun()
    #if st.button("Submit"):
        #st.session_state.vote = {"item": item, "reason": reason}
        

if st.session_state.vote is not None:
    st.write("Choix:")
    st.dataframe(st.session_state.vote)

if st.button("Sélectionner un cours"):
    vote()
    

#else:
#   f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"    