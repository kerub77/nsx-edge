# Script Python per ottenere il valore di enable_standby_relocation per i Tier-1 Gateway in NSX Manager
import requests
import base64
import urllib3
import argparse

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Parsing degli argomenti da riga di comando
parser = argparse.ArgumentParser(description="Ottieni informazioni sui Tier-1 Gateway da NSX Manager.")
parser.add_argument("-n", "--nsx-manager", required=True, help="Indirizzo NSX Manager")
parser.add_argument("-u", "--username", required=True, help="Username per l'autenticazione")
parser.add_argument("-p", "--password", required=True, help="Password per l'autenticazione")
args = parser.parse_args()

# Configurazione da argomenti
NSX_MANAGER = args.nsx_manager
USERNAME = args.username
PASSWORD = args.password

# Creazione delle credenziali in Base64
credentials = f"{USERNAME}:{PASSWORD}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# Endpoint API per ottenere la lista di tutti i Tier-1
t1_list_url = f"{NSX_MANAGER}/policy/api/v1/infra/tier-1s"

# Headers per l'autenticazione
headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/json"
}

try:
    # Ottenere la lista di tutti i Tier-1 Gateway
    response = requests.get(t1_list_url, headers=headers, verify=False)
    response.raise_for_status()
    t1_list = response.json().get("results", [])

    if not t1_list:
        print("Nessun Tier-1 Gateway trovato.")
    else:
        for t1 in t1_list:
            t1_id = t1.get("id", "UNKNOWN")
            t1_name = t1.get("display_name", "UNKNOWN")

            # Escludi il Tier-1 chiamato "t1"
            if t1_name.lower() == "t1":
                continue

            enable_standby_relocation = t1.get("enable_standby_relocation", "Non disponibile")
            print(f"T1 ID: {t1_id}, Nome: {t1_name}, enable_standby_relocation: {enable_standby_relocation}")

except requests.exceptions.RequestException as e:
    print(f"Errore nella richiesta API: {e}")
