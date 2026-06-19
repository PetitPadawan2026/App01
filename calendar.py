import streamlit as st
import calendar
from streamlit_calendar import calendar
 
calendar_options = {
    "editable": True,
    "selectable": True,
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
    },
    "slotMinTime": "06:00:00",
    "slotMaxTime": "20:00:00",
    "initialView": "resourceTimelineDay",
    "resourceGroupField": "cours",
    "resources": [
        {"id": "a", "cours": "Eleve A", "title": "Cours A"},
        {"id": "a", "cours": "Eleve A", "title": "Cours B"},
        {"id": "b", "cours": "Eleve B", "title": "Cours A"},
        {"id": "a", "cours": "Eleve B", "title": "Cours B"},
        {"id": "a", "cours": "Eleve C", "title": "Cours A"},
    ],
}
calendar_events = [
    { "title": "Event 1", "start": "2026-06-16T08:30:00", "end": "2026-06-16T10:30:00", "resourceId": "a", },
    { "title": "Event 2", "start": "2026-06-17T07:30:00", "end": "2026-06-17T10:30:00", "resourceId": "b", },
    { "title": "Event 3", "start": "2026-06-18T10:40:00", "end": "2026-06-19T12:30:00", "resourceId": "a", }
]
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
