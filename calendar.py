import streamlit as st
import calendar
from streamlit_calendar import calendar
import pyodbc
import pandas as pd


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

calendar = calendar(
    events=calendar_events,
    options=calendar_options,
    custom_css=custom_css,
    key='calendar', # Assign a widget key to prevent state loss
    )
st.write(calendar)






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

