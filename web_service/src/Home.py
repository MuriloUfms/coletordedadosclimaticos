import streamlit as st
import requests
from settings import Settings

st.set_page_config(page_title='Clima - Facom', layout='wide')

st.title('Clima - Facom')

st.write('##### Inscreva-se para receber notificações do clima da Facom')

col1, col2 = st.columns([1, 2])

with col1:
    sub_email = st.text_input('Email', key='sub_email')
    frequency_hours = st.number_input('Frequência (em horas)')

    if st.button('Inscrever'):
        if not sub_email or not frequency_hours:
            st.error('Preencha todos os campos')
            st.stop()

        response = requests.post(
            f'{Settings.BACKEND_URL}/newsletter/subscribe',
            json={'email': sub_email, 'frequency_hours': frequency_hours},
        )
        if response.status_code == 200:
            st.success('Inscrição realizada com sucesso')
        else:
            st.error('Erro ao realizar inscrição')
            st.write(response.json())

    st.write('---')

    st.write('##### Desinscrever')

    unsub_email = st.text_input('Email', key='unsub_email')

    if st.button('Desinscrever'):
        if not unsub_email:
            st.error('Preencha o campo de email')
            st.stop()

        response = requests.post(
            f'{Settings.BACKEND_URL}/newsletter/unsubscribe',
            json={'email': unsub_email},
        )
        if response.status_code == 200:
            st.success('Desinscrição realizada com sucesso')
        else:
            st.error('Erro ao realizar desinscrição')
            st.toast(response.json())
