import streamlit as st
import datetime

if "book_event" not in st.session_state:
    st.session_state.book_event=None

@st.dialog("Choisissez")
def book_event():
    in_name = st.text_input("Nom de l'élève")
    in_date = st.datetime_input("Date")
    


    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Ok"):
            st.session_state.book_event=("A voté")
            st.session_state.book_event = {"Nom de l'élève": in_name, 
                                    "Date": in_date,}
            st.rerun()

    with col3:
        if st.button("Annuler"):
            st.session_state.book_event=None
            st.rerun()

    #if st.button("Submit"):
        #st.session_state.book_event = {"item": item, "reason": reason}
        

if st.session_state.book_event is not None:
    st.write("Choix:")
    st.dataframe(st.session_state.book_event)

if st.button("Sélectionner un cours"):
    book_event()
    

   # "Choisissez la date et l'heure",
    #datetime.datetime(2025, 11, 19, 16, 45),

#st.write("Choisi", event_time)

#{"allDay":false,"title":"Event 1","start":"2026-06-16T08:30:00+02:00","end":"2026-06-16T10:30:00+02:00","resourceId":"a"}

#else:
#   f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"    