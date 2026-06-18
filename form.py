import streamlit as st
import pandas as pd
import os
import time
import re

st.set_page_config(
    page_title=" Informations personnelles",
    page_icon="📝"
)

st.title("📝 Informations personnelles")

# Formulaire
with st.form("formulaire_parent"):
    nom = st.text_input("Nom *")
    prenom = st.text_input("Prénom *")
    telephone = st.text_input("Téléphone *")
    adresse = st.text_area("Adresse (optionnel)")
    email = st.text_input("Adresse e-mail (optionnel)")

    submit = st.form_submit_button("Enregistrer")

if submit:

    erreurs = []

    # Vérifications des champs obligatoires
    if not nom.strip():
        erreurs.append("Le nom est obligatoire.")
        st.toast("Le Nom est obligatoire", icon="❗")
        time.sleep(0.5)

    if not prenom.strip():
        erreurs.append("Le prénom est obligatoire.")

    if not telephone.strip():
        erreurs.append("Le numéro de téléphone est obligatoire.")

    # Vérification de l'email si renseigné
    if email:
        pattern_email = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern_email, email):
            erreurs.append("L'adresse e-mail n'est pas valide.")

    if erreurs:
        for erreur in erreurs:
            st.error(erreur)
    else:

        donnees = {
            "Nom": [nom],
            "Prénom": [prenom],
            "Téléphone": [telephone],
            "Adresse": [adresse],
            "Email": [email]
        }

        df = pd.DataFrame(donnees)

        fichier = "utilisateurs.csv"

        if os.path.exists(fichier):
            df.to_csv(
                fichier,
                mode="a",
                header=False,
                index=False,
                encoding="utf-8"
            )
        else:
            df.to_csv(
                fichier,
                index=False,
                encoding="utf-8"
            )

        st.success("Informations enregistrées avec succès !")









st.set_page_config(
    page_title="Informations personnelles de l'élève",
    page_icon="📝"
)

st.title("📝 Informations personnelles de l'élève")

# Formulaire 
with st.form("formulaire_eleve"):
    prenom = st.text_input("Prénom *")
    niveau = st.text_input("Niveau *")
    with st.container(horizontal=True, horizontal_alignment="distribute"):
        submit = st.form_submit_button("Enregistrer")
        #with st.button("Annuler"):
            #
            #st.empty()
        #with st.button("Enregistrer et nouveau"):
            #
            #st.empty()

    if submit:
    
        erreurs = []
    
        # Vérifications des champs obligatoires
        if not prenom.strip():
            erreurs.append("Le prénom est obligatoire.")
    
        if not niveau.strip():
            erreurs.append("Le niveau est obligatoire.")
    
        if erreurs:
            for erreur in erreurs:
                st.error(erreur)
        else:
    
            donnees = {
                "Nom": [nom],
                "Niveau": [niveau]
            }
    
            df = pd.DataFrame(donnees)
    
            fichier = "utilisateurs.csv"
    
            if os.path.exists(fichier):
                df.to_csv(
                    fichier,
                    mode="a",
                    header=False,
                    index=False,
                    encoding="utf-8"
                )
            else:
                df.to_csv(
                    fichier,
                    index=False,
                    encoding="utf-8"
                )
    
            st.success("Informations enregistrées avec succès !")

