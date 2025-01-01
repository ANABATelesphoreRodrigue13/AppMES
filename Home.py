pip install plotly
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='HOKAGE', page_icon=None, layout="centered", 
                   initial_sidebar_state="auto", menu_items=None)

st.title("Capital humain et croissance économique en Côte d'Ivoire")

st.markdown(
    """
    une approche par les équations simultanées

    """
)

st.info("Cliquez sur le menu latéral de gauche pour naviguer vers les différentes applications.")

st.subheader("Profitez de votre expérience!")

from utils import afficher_profil_sidebar



afficher_profil_sidebar("ANABA.jpg", "ANABA", "Telesphore",
                        "student.rodrigue.anaba@issea-cemac.org", "(237) 6 96 26 90 77")

afficher_profil_sidebar("ANATO.jpg", "ANATO", "Diane", "dianeanato1@gmail.com", "(229) 61 19 24 40")

from utils import display_single_metric_advanced


tables = st.tabs(["Présentation du pays", "Données", "Tableau de Bord","Modélisation","Rapport"])

with tables[0]:
     from utils import Presentation
     Presentation()

with tables[1]:
     from utils import load_data
     df = load_data()
     st.write("Aperçu des données :")
     st.dataframe(df)
     st.write("Source: WDI, OMS (2023)")

with tables[2]:
    from utils import Plot
    cl1,cl2,=st.columns(2)
    with cl1:
            display_single_metric_advanced("PIB TOTAL", 78.79, 1, unit="$", caption="Total", color_scheme="green")
    with cl2:
        display_single_metric_advanced("Taux de chômage Moyen", 2.60, 1, unit="%", caption="Maximun", color_scheme="red")
    Plot()

with tables[4]:
     from utils import show_pdf
     st.title("Visualiseur de PDF")
     pdf_path = "Anaba&Anato.pdf"  

     try:
          show_pdf(pdf_path)
     except Exception as e:
        st.error(f"Erreur lors du chargement du PDF : {str(e)}")



