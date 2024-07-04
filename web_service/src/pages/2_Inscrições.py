import streamlit as st
import requests

from settings import Settings

st.set_page_config(page_title='Inscrições', layout='wide')

st.title('Inscrições')

response = requests.get('http://host.docker.internal/newsletter/subscribers')

if response.status_code != 200:
    st.write(response.text, unsafe_allow_html=True)
    st.stop()

for item in response.json()['items']:
    col1, col2, col3 = st.columns(3)

    col1.write(f"- {item['email']}")
    col2.write(f"Frequência: {float(item['frequency']) / 60 / 60:.2f} horas")

    with col3:
        if st.button('Remover', key=item['email']):
            requests.post(
                f'{Settings.BACKEND_URL}/newsletter/unsubscribe',
                json={'email': item['email']},
            )
            st.rerun()
