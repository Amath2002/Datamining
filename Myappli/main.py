import streamlit
from PIL import Image
import streamlit as st
import numpy as np
import pickle
f = open('model.sav','rb')
model_load = pickle.load(f)
#Fonction prédiction

def Prediction(input_data):
    input_data=np.asarray(input_data,float)
    input_data = input_data.reshape((1, 12))
    pred=model_load.predict(input_data)
    if (pred[0] == 0):
       return  "Ce client est un cilent sur "
    else:
        return "Ce client est succeptible de quitter votre banque. Veuillez le contacter pour lui faire de nouveaux offres"

def main():

    # Titre et entête de l'application
    st.set_page_config(
        page_title="MyAplli",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="auto",


    )

    st.markdown('**<h1 style="color:white;text-align:center;font-size:35px;font-family:Bodoni MT;background:#128ac7;"> '
                'Application de prédiction des clients succeptibles de quitter notre banque </h1>**',
                unsafe_allow_html=True)
    # Sidebar
    st.sidebar.title("Dévéloppeurs")
    imageA = Image.open("img/as.jpg")
    imageM = Image.open("img/md.jpeg")
    st.sidebar.image(imageA, caption='Amath SALL, élève ingénieur  à ENSAE', width=100,use_column_width=True )
    st.sidebar.image(imageM,caption='Mamadou Diallo,élève ingénieur  à ENSAE', width=100,use_column_width=True )

    #Formulaire
    st.markdown('**<h1 style="color:black;text-align:center;font-size:35px;font-family:Bodoni MT;border-bottom: 2px solid rgb(10, 10, 10) "> '
                'Formulaire</h1>**',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        Gender = st.selectbox("SEXE", ("Homme", "Femme"))
        Marital_Status = st.selectbox("Situation Matrimoniale ?", ("Married", "Single", "Unknown", "Divorced"))
        Total_Relationship_Count = st.number_input("Nombre total de produit détenus par le client")

        Months_Inactive_12_mon = st.number_input("Nombre de mois d'inactivité au cours des 12 derniers mois")

        Contacts_Count_12_mon = st.number_input("Nombre de contact au cours des 12 derniers mois")

        Credit_Limit = st.number_input("Limite de crédit sur la carte")

    with col2:
        Total_Revolving_Bal = st.number_input("Solde renouvelable total sur la carte de crédit")

        Total_Amt_Chng_Q4_Q1 = st.number_input("Changement du montant de la transaction T4 par rapport à T1")

        Total_Trans_Amt = st.number_input("Montant total des transactions au  cours des 12 derniers mois")

        Total_Trans_Ct = st.number_input("Nombre total de transactions aux cours des deux derniers mois")

        Total_Ct_Chng_Q4_Q1 = st.number_input("Changement du nombre de la transaction T4 par rapport à T1")

        Avg_Utilization_Ratio = st.number_input("Taux d'utlisation moyenne de la carte")

        resultat=""
    #Recodage des variables qualitatives

    ##Sexe
        if Gender=='Femme':
            Gender=0
        else:
            Gender=1

    #Situations

        if Marital_Status == "Married":
            Marital_Status = 1
        if Marital_Status == "Single":
            Marital_Status = 2
        if Marital_Status == "Unknown":
            Marital_Status = 3
        if Marital_Status == "Divorced":
            Marital_Status = 0
        #Listes des nouvelles données saisies
        donnees_saisie = [Gender, Marital_Status, Total_Relationship_Count,
                          Months_Inactive_12_mon, Contacts_Count_12_mon,
                          Credit_Limit, Total_Revolving_Bal, Total_Amt_Chng_Q4_Q1,
                          Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio]


        ##Normalisations des variables quantitatives :diviser par la valeur maximale dans la base
        Total_Relationship_Count = Total_Relationship_Count / 6
        Months_Inactive_12_mon = Months_Inactive_12_mon / 6
        Contacts_Count_12_mon = Contacts_Count_12_mon / 6
        Credit_Limit = Credit_Limit / 34516.0
        Total_Revolving_Bal = Total_Revolving_Bal / 2517
        Total_Amt_Chng_Q4_Q1 = Total_Amt_Chng_Q4_Q1 / 3.397
        Total_Trans_Amt = Total_Trans_Amt / 18484
        Total_Trans_Ct = Total_Trans_Ct / 139
        Total_Ct_Chng_Q4_Q1 = Total_Ct_Chng_Q4_Q1 / 3.714
        Avg_Utilization_Ratio = Avg_Utilization_Ratio / 0.9990000000000001

        donnees_saisie= [Gender, Marital_Status, Total_Relationship_Count,
                        Months_Inactive_12_mon, Contacts_Count_12_mon,
                        Credit_Limit,Total_Revolving_Bal, Total_Amt_Chng_Q4_Q1,
                        Total_Trans_Amt,Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio]
    if st.button("Prediction"):
            resultat=Prediction (donnees_saisie)
    st.success(resultat)


if __name__=='__main__':
        main()
