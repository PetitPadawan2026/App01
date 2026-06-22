import streamlit as st
import datetime

if "vote" not in st.session_state:
    st.session_state.vote=None

@st.dialog("Choisissez")
def vote():
    in_name = st.text_input("Nom de l'élève")
    in_date = st.datetime_input("Date")
    


    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Ok"):
            st.session_state.vote=("A voté")
            st.session_state.vote = {"Nom de l'élève": in_name, 
                                    "Date": in_date,}
            st.rerun()

    with col3:
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
    

   # "Choisissez la date et l'heure",
    #datetime.datetime(2025, 11, 19, 16, 45),

#st.write("Choisi", event_time)



#else:
#   f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"    