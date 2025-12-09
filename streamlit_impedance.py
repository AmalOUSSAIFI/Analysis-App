import streamlit as st

st.set_page_config(
    page_title="Impedance AI App",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Impedance Prediction & Analysis App")
st.write("""
Bienvenue dans votre plateforme d'analyse et de prédiction de l'impédance.
Utilisez le menu à gauche pour naviguer entre :
- 🔮 Modèle de prédiction  
- 📊 Visualisations interactives  
- 📈 Dashboard Power BI  
- 🗂 Historique des prédictions  
- 👤 À propos de moi  
""")

st.image(
    "https://img.icons8.com/?size=512&id=53644&format=png",
    width=200
)

st.success("Choisissez une section dans la barre latérale pour commencer.")