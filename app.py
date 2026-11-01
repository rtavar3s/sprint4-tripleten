from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(Path(__file__).parent / "vehicles_us.csv")  # lendo os dados

st.title("Dashboard de anúncios de vendas de carros")
st.write(
    "Aplicativo web com visualizações interativas do conjunto de dados de "
    "anúncios de vendas de carros."
)

hist_button = st.button("Criar histograma")
scatter_button = st.button("Criar gráfico de dispersão")

if hist_button:  # se o botão for clicado
    st.write("Criando um histograma para o conjunto de dados de anúncios de vendas de carros")

    fig = px.histogram(car_data, x="odometer")  # criar um histograma
    st.plotly_chart(fig, use_container_width=True)  # exibir um gráfico Plotly interativo

if scatter_button:  # se o botão for clicado
    st.write("Criando um gráfico de dispersão entre preço e odômetro")

    fig = px.scatter(car_data, x="odometer", y="price")  # criar um gráfico de dispersão
    st.plotly_chart(fig, use_container_width=True)
