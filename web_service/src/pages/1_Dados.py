import streamlit as st
import requests
import pandas as pd

from settings import Settings
from datetime import datetime, timedelta, time

st.set_page_config(page_title='Ultimas Coletas', layout='wide')

st.title('Ultimas Coletas')

st.sidebar.title('Filtros')
st.sidebar.write('Aqui você pode filtrar as coletas')
size = st.sidebar.number_input(
    'Limite de coletas', min_value=1, max_value=100, value=50
)
dt_inicial = st.sidebar.date_input('Data inicial', datetime.now() - timedelta(days=1))
dt_final = st.sidebar.date_input('Data final', datetime.now())
hora_inicial = st.sidebar.time_input('Hora inicial', datetime.now() - timedelta(hours=12), step=60*30)  # 30 minutos
hora_final = st.sidebar.time_input('Hora final', datetime.now(), step=60*30)  # 30 minutos

gt = dt_inicial.strftime('%Y-%m-%d') + 'T' + hora_inicial.strftime('%H:%M:%S')
lt = dt_final.strftime('%Y-%m-%d') + 'T' + hora_final.strftime('%H:%M:%S')

st.write(f'Coletas entre {dt_inicial.isoformat()} {hora_inicial.isoformat()} e {dt_final.isoformat()} {hora_final.isoformat()}')

response = requests.get(f'{Settings.BACKEND_URL}/coletor/collections?size={size}&gt={gt}&lt={lt}')
response.raise_for_status()

df = pd.DataFrame(response.json()['items'])
if df.empty:
    st.write('Nenhuma coleta encontrada')
    st.stop()

df['timestamp'] = pd.to_datetime(df['timestamp'])
df['timestamp'] = df['timestamp'].dt.tz_localize('UTC').dt.tz_convert('America/Cuiaba')
df.drop('id', axis=1, inplace=True)
df.sort_values('timestamp', ascending=False, inplace=True)
df.set_index('timestamp', inplace=True)

st.write('## Variação da temperatura')
st.line_chart(df['temperatura'])

st.write('## Variação da umidade')
st.line_chart(df['umidade'])

st.write('## Variação da velocidade do vento')
st.line_chart(df['velocidade_vento'])

st.dataframe(
    df,
    use_container_width=True,
    column_config={
        'timestamp': st.column_config.DatetimeColumn(
            format='D MMM YYYY, HH:mm:ss',
            timezone='America/Cuiaba',
        )
    },
)
