import pandas as pd
import streamlit as st
import plotly.graph_objects as go


st.title('Analisador de proventos de investimentos')
file = "./file/PlanilhaProventos.xlsx"

df = pd.read_excel(file)
total_ano = df.groupby('Ano')['Valor'].sum().reset_index(name="Valor")
meses_agrupado = df.groupby('Mes')['Valor'].sum().reset_index(name="Valor")
anos = total_ano['Ano']
valores = total_ano['Valor']
# Criar o gráfico de barras
fig_total_ano = go.Figure()
fig_total_ano.add_trace(go.Bar(
    x=anos,
    y=valores,
    text=valores,
))
# Atualizar o layout
fig_total_ano.update_layout(
    title='Total por Ano',
    yaxis_title='Valor',
    xaxis=dict(
         title='Valores por hora',
         tickvals=list(range(len(anos))),
         ticktext=valores,
     ),
)

fig_mes = go.Figure()
for ano, grupo in df.groupby('Ano'):
    fig_mes.add_trace(go.Bar(
        x=grupo['Mes'],
        y=grupo['Valor'],
        name=str(ano),
        text=grupo['Valor'],
    ))

# Atualizar o layout
fig_mes.update_layout(
    title='Total por Mês',
    yaxis_title='Valor',
    barmode='group',
)

st.write(fig_mes)
st.write(fig_total_ano)