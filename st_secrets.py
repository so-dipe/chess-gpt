import streamlit as st
import json

def load_secrets():

    service_account_key = {
        "type": st.secrets['TYPE'], 
        "project_id": st.secrets['PROJECT_ID'], 
        "private_key_id": st.secrets['PRIVATE_KEY_ID'], 
        "private_key": st.secrets['PRIVATE_KEY'], 
        "client_email": st.secrets['CLIENT_EMAIL'], 
        "client_id": st.secrets['CLIENT_ID'], 
        "auth_uri": st.secrets['AUTH_URI'], 
        "token_uri": st.secrets['TOKEN_URI'], 
        "auth_provider_x509_cert_url": st.secrets['AUTH_PROVIDER_X509_CERT_URL'], 
        "client_x509_cert_url": st.secrets['CLIENT_X509_CERT_URL'], 
        "universe_domain": st.secrets['UNIVERSE_DOMAIN']
    }

    with open('service_account_key.json', 'w') as f:
        json.dump(service_account_key, f)

    print("secrets loaded successfully!")