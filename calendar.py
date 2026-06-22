import streamlit as st
import calendar
from streamlit_calendar import calendar
import datetime
import time
import pyodbc
import pandas as pd

ret_event = {}
if "book_event" not in st.session_state:
    st.session_state.book_event=None

calendar_resources = [
        {"id": "a", "cours": "Eleve A", "title": "Cours A"},
        {"id": "a2", "cours": "Eleve A", "title": "Cours B"},
        {"id": "b", "cours": "Eleve B", "title": "Cours A"},
        {"id": "b2", "cours": "Eleve B", "title": "Cours B"},
        {"id": "c", "cours": "Eleve C", "title": "Cours A"},
    ]

calendar_events = [
    { "title": "Event 1", "start": "2026-06-16T08:30:00", "end": "2026-06-16T10:30:00", "resourceId": "a", },
    { "title": "Event 2", "start": "2026-06-17T07:30:00", "end": "2026-06-17T10:30:00", "resourceId": "b", },
    { "title": "Event 3", "start": "2026-06-18T10:40:00", "end": "2026-06-19T12:30:00", "resourceId": "c", },
    { "title": "Event 4", "start": "2026-06-18T10:40:00", "end": "2026-06-19T12:30:00", "resourceId": "a2", }
] 

if st.session_state.book_event is not None:
    #calendar_events.append(st.session_state.book_event)
    calendar_events = st.session_state.book_event

calendar_options = {
    "editable": True,
    "selectable": True,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "08:00:00",
    "slotMaxTime": "20:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "cours",
    "resources": calendar_resources,
} 

custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""

state = calendar(
    events=calendar_events,
    options=calendar_options,
    custom_css=custom_css,
    key='calendar', # Assign a widget key to prevent state loss
    )
st.write(state)

# ===============================================================================================================
# Form 1

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

def datetime_to_str(date_in):
    st.toast(date_in)
    ret_val=date_in.strftime("%Y-%m-%d %H:%M:%S")
    st.toast(ret_val)
    return ret_val

def calc_heure_fin(heure_debut):
    heure_fin = heure_debut
    return str(heure_fin)

@st.dialog("Choisissez")
def book_event():
    in_name = st.text_input("Nom de l'élève")
    in_date = st.datetime_input("Date")
    in_title = make_select_niveau()
    #in_title = make_select_niveau("Niveau")

    erreurs = []

    # Vérifications des champs obligatoires
    if not in_name.strip():
        erreurs.append("Le Nom de l'élève est obligatoire.")
        st.toast("Le Nom est obligatoire", icon="❗")
        time.sleep(0.5)


    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Ok"):
            ret_event = init_event()
            ret_event = {
                "allDay": False,
                "title": "Cours démo",
                "start": str(in_date),   
                "end": str(calc_heure_fin(in_date)),
                "resourceId":in_name
            }

            st.session_state.book_event=ret_event

            st.rerun()

    with col3:
        if st.button("Annuler"):
            st.session_state.book_event=None
            st.rerun()

if st.session_state.book_event is not None:
    st.write("Choix:")
    st.dataframe(st.session_state.book_event)

if st.button("Sélectionner un cours"):
    book_event()

# ===============================================================================================================
#base de donnée
sql_conn = None

if state.get("sql_conn") is not None:
    sql_conn = st.session_state["sql_conn"]

def show_table(tabname):
    if st.session_state["sql_conn"] is not None:
        query = "SELECT * FROM " + tabname
        df = pd.read_sql(query, st.session_state["sql_conn"])
        return st.dataframe(df)

cxn_status = False
with st.spinner("Connecting database...", show_time=True):
    try:
        sql_conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+st.secrets["Server"]+';DATABASE='+st.secrets["Database"]+';Uid='+st.secrets["Uid"]+';Pwd='+st.secrets["Pwd"])
        #;Trusted_Connection=yes'
        cxn_status = True
        st.session_state["sql_conn"] = sql_conn
    except pyodbc.Error as ex:
        st.error('Database unreachable', icon="🚨")
        cxn_status = False
        st.session_state["sql_conn"] = None

if cxn_status:
    query = "SELECT * FROM t_niveau"
    df = pd.read_sql(query, sql_conn)
    st.dataframe(df)

    show_table('t_parent')


