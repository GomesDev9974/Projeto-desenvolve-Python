import streamlit as st 
import pandas as pd
import plotly.express as px 
from tkinter import *


# sidebar
st.sidebar.title("Configurações")
st.sidebar.text("aluno:joao vitor gomes")
st.sidebar.text("PDITA: PD550")

#carregar dados de exemplo
dados = pd.DataFrame({
    'Dia': ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5', 'Dia 6', 'Dia 7'],
    'Exercício': [20, 15, 25, 30, 22, 18, 27],
    'Descanso': [10, 12, 8, 5, 9, 11, 6]
})

# Criar gráfico de barras com Plotly
fig = px.bar(dados, x='Dia', y=['Exercício', 'Descanso'], 
             title='Exercício vs Descanso por Dia',
             labels={'value': 'Minutos', 'variable': 'Atividade'},
             barmode='group')


# Exibir gráfico
st.plotly_chart(fig)

# Adicionar estilo com CSS
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    </style>
    """,
    unsafe_allow_html=True
)
