import streamlit as st
import datetime

ret_event = {}
if "book_event" not in st.session_state:
    st.session_state.book_event=None

def make_select_niveau(txt_label="Test"):
    return st.selectbox(
        txt_label,
        ("Niveau Débutant", "Niveau Confirmé", "Niveau Expert"),
        label_visibility="hidden" if txt_label == "Test" else "visible"
    )


def init_event():
    base_event = {
        "allDay": False,
        "title": "",            #"Event 1",
        "start": "",            #"2026-06-16T08:30:00+02:00",
        "end": "",              #"2026-06-16T10:30:00+02:00",
        "resourceId":"",        #"a"
    } 
    return base_event   

def calc_heure_fin(heure_debut):
    heure_fin = heure_debut
    return heure_fin

@st.dialog("Choisissez")
def book_event():
    in_name = st.text_input("Nom de l'élève")
    in_date = st.datetime_input("Date")
    in_title = make_select_niveau()
    #in_title = make_select_niveau("Niveau")


    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Ok"):
            ret_event = init_event()
            ret_event = {
                "allDay": False,
                "title": "Cours démo",
                "start": in_date,   
                "end": calc_heure_fin(in_date),
                "resourceId":in_name
            }

            st.session_state.book_event=ret_event

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










#{
#   "allDay":false,
#   "title":"Event 1",
#   "start":"2026-06-16T08:30:00+02:00",
#    "end":"2026-06-16T10:30:00+02:00",
#   "resourceId":"a"
# }



#st.write("Choisi", event_time)
#else:
#   f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"    