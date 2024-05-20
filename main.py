import pandas as pd
from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel
from deep_translator import GoogleTranslator
from pretraitement import cleaned_text, vectorize_text_column



df =  pd.read_csv('df_c.csv')
# Chargement du modèle
loaded_model = load('reg_model.joblib')

# Création d'une nouvelle instance fastAPI
app = FastAPI()

@app.get("/") #
def Accueil ():
    return {"message": "Bienvenu sur l'appli de prediction des sentiments"} 

# Définir un objet (une classe) pour réaliser des requêtes
class request_body(BaseModel):
    text_tweet : str
    

# Definition du chemin du point de terminaison (API)
@app.post("/predict") 
# Définition de la fonction de prédiction  uvicorn main:app --reload
def predict(data : request_body):
    
    text_en = GoogleTranslator(source="fr", target="en").translate(data['text_tweet'])
    t_cl= cleaned_text(text_en)
    vect = vectorize_text_column(t_cl)
    
    # Prédiction 
    class_idx = loaded_model.predict(vect)[0]

    # Je retourne si le twitt est positif ou negatif
    return {'target' : df.target[class_idx]}
    


