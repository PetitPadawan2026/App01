import streamlit as st
import calendar
from streamlit_calendar import calendar
import datetime
import time
import pyodbc
import pandas as pd
from datetime import timedelta
import uuid
from openpyxl import load_workbook
import random

# ===============================================================================================================
# https://wgrhbpwvstegeekoqww2ua.streamlit.app/
# ===============================================================================================================

# ===============================================================================================================
# Variables de session
ret_event = {}
if "book_event" not in st.session_state:
    st.session_state.book_event=None

if not st.session_state.get("calendar", False):
        st.session_state["calendar"] = str(uuid.uuid4())

local_xls='./data/data_app.xlsx'
excel_loaded=False

# ===============================================================================================================
# Sélections
if "sel_parent" not in st.session_state:
    st.session_state.sel_parent=None

if "sel_enfant" not in st.session_state:
    st.session_state.sel_enfant=None

if "sel_niveau" not in st.session_state:
    st.session_state.sel_niveau=None

# ===============================================================================================================
# Options / params calendrier
def build_event(titre,debut,fin,ressource="a"):
    event_to_add = {"allDay": False, "title": "Test", "start": "2026-06-23T12:40:00", "end": "2026-06-23T14:30:00", "resourceId": "a2", }
    event_to_add["title"]=titre
    event_to_add["start"]=debut
    event_to_add["end"]=fin
    event_to_add["resourceId"]=ressource
    return event_to_add

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
st.write(calendar_events)
if "updated_events" not in st.session_state:
    st.session_state.updated_events=calendar_events
else:
    calendar_events.clear()
    df=st.session_state.updated_events
    try:
        rows,cols=df.shape
        for x in range(rows):
            evt=build_event(df["title"][x],
                            df["start"][x],
                            df["end"][x],
                            df["resourceId"][x])
            calendar_events.append(evt)
    except:
        df=df
st.write(calendar_events)

if "calendar_events" not in st.session_state:
    st.session_state.calendar_events=calendar_events

if st.session_state.book_event is not None:
    with st.expander("st.session_state.book_event"):
        st.write(st.session_state.book_event)
    #calendar_events.append(st.session_state.book_event)
    #calendar_events = st.session_state.book_event

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
    
# ===============================================================================================================
# Calendrier Widget
def build_calendar(events,options=calendar_options,css=custom_css):
    st.write(events)
    obj_cal = calendar(
        events=events,
        options=options,
        custom_css=css,
        key='calendar', # Assign a widget key to prevent state loss
        )
    with st.expander("Calendar data", expanded=False):
        st.write(obj_cal)    
    return obj_cal

build_calendar(calendar_events)

if 1 == 2:
    st.write(calendar_events)
    state = calendar(
        events=calendar_events,
        options=calendar_options,
        custom_css=custom_css,
        key='calendar', # Assign a widget key to prevent state loss
        )
    with st.expander("Calendar data", expanded=False):
        st.write(state)
    #key=st.session_state["calendar"],


event_to_add = { "title": "Test", "start": "2026-06-23T12:40:00", "end": "2026-06-23T14:30:00", "resourceId": "a2", }

# ===============================================================================================================
# Excel
cols_niv=['niveau_id','niveau_txt']
cols_par=['parent_id','parent_nom','parent_tel','parent_mail']
cols_enf=['enfant_id','parent_id','enfant_nom','enfant_niveau']
cols_cours=['cours_id','cours_date','cours_heure_debut','cours_heure_fin','cours_niveau','cours_capacite']


df_niv=None
df_par=None
df_enf=None
df_cours=None

df_xls = { #                    0            1               2                3  
        "Worksheet":      ["t_niveau",  "t_parent",     "t_enfant",       "t_cours"],
        "DisplayName":    ["Niveau",    "Parent",       "Enfant",         "Cours"],
        "Range":          ["A:B",       "A:D",          "A:D",            "A:F"],
        "SkipRows":       [0,           0,              0,                0],
        "UpToRow":        [14,          4,              5,                6],
        "DisplayColumns": [cols_niv,    cols_par,       cols_enf,         cols_cours],
        "DataFrame":      [df_niv,      df_par,         df_enf,           df_cours],
        "Description":    ["Niveau",   "Parent",       "Enfant",         "Cours"]
       }
def get_df_idx(idx=0,bln_table=False):
    try:
        data_values=get_data_from_excel(xls_file=local_xls,
                                        xls_sheet=df_xls["Worksheet"][idx],
                                        skip=df_xls["SkipRows"][idx],
                                        rng_cols=df_xls["Range"][idx],
                                        rng_rows=df_xls["UpToRow"][idx],
                                        rencols=df_xls["DisplayColumns"][idx],
                                        show_table=bln_table
                                        )        
        return data_values
    except:
        return None

def get_data_from_excel(xls_file,xls_sheet,skip,rng_cols,rng_rows,rencols=None,show_table=False):
    try: 
        df = pd.read_excel(
            io=xls_file,
            engine="openpyxl",
            sheet_name=xls_sheet,
            skiprows=int(skip),
            usecols=str(rng_cols),
            nrows=int(rng_rows),
        )
        if rencols is not None:
            try:
                df.columns = rencols
            except:
                df=df
        try:
            df['URL'] = df['URL'].fillna('')
        except:
            df=df
        if show_table == True:
            with st.expander(xls_sheet, expanded=False, icon=':material/table_view:', width='stretch'):
                st.dataframe(df)
    except:
        df = None
    return df

def date_time_to_datetime(date_in,time_in):
    a = date_in[:10]
    b = time_in
    c = f'{a} {b}'

    d= time.strptime(c, '%Y-%m-%d %H:%M:%S')
    ret_val = datetime.datetime.fromtimestamp(time.mktime(d))
    return c #ret_val #ret_val.strftime("%Y-%m-%d %H:%M:%S")

def charger_excel():
    global df_xls,df_niv,df_par,df_enf,df_cours

    df_niv=get_df_idx(0,False)
    df_par=get_df_idx(1,False)
    df_enf=get_df_idx(2,False) 
    df_cours=get_df_idx(3,False)   

    df_cours = df_cours.dropna()
    
    nouveau_cours={}

    df_xls["DataFrame"][0]=df_niv
    df_xls["DataFrame"][1]=df_par
    df_xls["DataFrame"][2]=df_enf
    df_xls["DataFrame"][3]=df_cours

def get_df(id=0):
    try:
        data_values=get_df_idx(id,False)       
        return data_values
    except:
        st.write(f'Erreur get_df pour {id}')
        return None
# ===============================================================================================================
# Form 1
def make_select_niveau(txt_label="Test"):
    #return st.selectbox(
        #txt_label,
        #("Tous Niveaux ", "Niveau 1 ", "Niveau 2 ", "Niveau 3 ", "Niveau 4 ", "Niveau 5 ", "Niveau 6 ", "Niveau 7 ", "Niveau 8 ", "Niveau 9 ", "Niveau 10 ", "Niveau 11 ", "Niveau 12 "),
        #label_visibility="hidden" if txt_label == "Test" else "visible"
    #)
    df=get_df(0)
    sel_niveau = st.selectbox(label ="Niveau",
                             options=df['niveau_id'].unique(),
                             format_func=lambda x: f"{x} - {df['niveau_txt'][ x ]}"
                             )

    return sel_niveau

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
    time_gap = 45 #minutes
    heure_fin = heure_debut + timedelta(minutes=time_gap)
    return heure_fin

@st.dialog("Choisissez")
def book_event():
    st.write(f"Parent sélectionné: {st.session_state.sel_parent}")
    in_name = st.text_input("Nom de l'élève")
    in_date = st.datetime_input("Date")
    in_niveau = make_select_niveau()
    in_parent = st.session_state.sel_parent

    erreurs = []

    # Vérifications des champs obligatoires
    if not in_name.strip():
        erreurs.append("Le Nom de l'élève est obligatoire.")
        st.toast("Le Nom est obligatoire", icon="❗")
        time.sleep(0.5)
    else:
        st.session_state.sel_enfant=in_name

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Ok"):
            ret_event = init_event()

            st.session_state.sel_parent=in_parent
            st.session_state.sel_enfant=in_name
            st.session_state.sel_niveau=in_niveau

            ret_event = {
                "allDay": False,
                "title": st.session_state.sel_enfant, #in_name
                "start": str(in_date),   
                "end": str(calc_heure_fin(in_date)),
                "resourceId": "a2",
                "niveau":in_niveau
            }
            ret_event = build_event(in_name,str(in_date),str(calc_heure_fin(in_date)),"a")
            st.session_state.book_event=ret_event
            st.session_state.updated_events=pd.concat([
                                            pd.DataFrame(st.session_state.calendar_events), 
                                            pd.Series(ret_event).to_frame().T], 
                                            ignore_index=True)

            st.rerun()
 
    with col3:
        if st.button("Annuler"):
            st.session_state.book_event=None
            st.rerun()

if st.session_state.book_event is not None:
    st.write("Choix:")
    st.dataframe(st.session_state.book_event)

if st.button("Sélectionner un parent"):
    st.session_state.sel_parent=None
    df=get_df(1)
    sel_parent = st.selectbox ("Parent:", options=df['parent_id'].unique() )
    st.session_state.sel_parent=sel_parent

if st.button("Sélectionner un cours"):
    book_event()

if st.button("Reserver"):
    nouveau_cours={
        'cours_id':'Tom',
        'cours_date':'2026-06-25 00:00:00',
        'cours_heure_debut':'09:00:00',
        'cours_heure_fin':'11:45:00',
        'cours_niveau':10,
        'cours_capacite':3
    }

    booked_event = st.session_state.book_event
    nouveau_cours={
        'cours_id':booked_event["title"],
        'cours_date':booked_event["start"],
        'cours_heure_debut':booked_event["start"],
        'cours_heure_fin':booked_event["end"],
        'cours_niveau':booked_event["niveau"],
        'cours_capacite':3
    }

    new_row = pd.Series(nouveau_cours)
    df_cours=pd.concat([df_cours, new_row.to_frame().T], ignore_index=True)
    df_cours

    nouveau_event={
        "title":f"Event {nouveau_cours['cours_id']}",
        "start":date_time_to_datetime(nouveau_cours['cours_date'], nouveau_cours['cours_heure_debut']),
        "end":date_time_to_datetime(nouveau_cours['cours_date'], nouveau_cours['cours_heure_fin']),
        "resourceId":"a"
        }

    if 1 == 2:
        st.session_state.updated_events=pd.concat([
                                        pd.DataFrame(st.session_state.calendar_events), 
                                        pd.Series(nouveau_event).to_frame().T], 
                                        ignore_index=True)
        st.rerun()

# ===============================================================================================================
# Données via Excel
charger_excel()
