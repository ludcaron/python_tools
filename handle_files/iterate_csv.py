import pandas as pd
import requests
import os
from datetime import datetime

def iterate_csv(file_path):
    # Lire le fichier CSV
    df = pd.read_csv(file_path)

    # Vérifier si les fichiers CSV existent déjà, sinon les créer
    if not os.path.exists('response_ok.csv'):
        pd.DataFrame(columns=['url', 'param', 'status', 'timestamp']).to_csv('response_ok.csv', index=False)
    if not os.path.exists('response_ko.csv'):
        pd.DataFrame(columns=['url', 'param', 'status', 'error_message', 'timestamp']).to_csv('response_ko.csv', index=False)

    # Lire les fichiers CSV existants
    response_ok = pd.read_csv('response_ok.csv')
    response_ko = pd.read_csv('response_ko.csv')

    # Itérer sur chaque ligne du DataFrame
    for index, row in df.iterrows():
        url = row['url']
        param = row['param']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       
        try:
            # Faire une requête HTTP GET
            response = requests.get(url, params={'param': param})
           
            if response.status_code == 204:
                # Ajouter à response_ok
                response_ok = response_ok.append({'url': url, 'param': param, 'status': 'ok', 'timestamp': timestamp}, ignore_index=True)
            else:
                # Ajouter à response_ko avec le message d'erreur
                response_ko = response_ko.append({'url': url, 'param': param, 'status': 'ko', 'error_message': response.text, 'timestamp': timestamp}, ignore_index=True)
        except Exception as e:
            # Ajouter à response_ko en cas d'exception
            response_ko = response_ko.append({'url': url, 'param': param, 'status': 'ko', 'error_message': str(e), 'timestamp': timestamp}, ignore_index=True)

    # Sauvegarder les DataFrames en CSV
    response_ok.to_csv('response_ok.csv', index=False)
    response_ko.to_csv('response_ko.csv', index=False)

if __name__ == "__main__":
    file_path = "chemin/vers/votre_fichier.csv"
    iterate_csv(file_path)
