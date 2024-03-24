import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import time
import datetime as dt

st.title('Análise de proventos')
with st.sidebar:
    with st.spinner("Carregando..."):
        time.sleep(3)
    st.success("Informações carregadas com sucesso!" )
    st.write("No COMEÇO seus proventos vão pagar")
    st.write("Uma bala: R$ 0,75 :candy:")
    st.write("Depois de um tempo:")
    st.write("Um lanche: R$ 15,00 :hamburger:")
    st.write("O Netflix: R$ 40,00 :tv:")
    st.write("A academia: R$ 100,00 :man-lifting-weights:")
    st.write("Um aluguel: R$ 800,00 :house:")
    st.write("Um salário mínimo: R$ 1412,00 :dollar:")
    st.write("Por fim, sua liberdade FINANCEIRA :unlock:")


file = "./file/PlanilhaProventos.xlsx"

df = pd.read_excel(file)

df['Ano'] = df['Ano'].astype(int)
df['Mes'] = df['Mes'].astype(str)
df['Valor'] = df['Valor'].astype(float)
total_ano = df.groupby('Ano')['Valor'].sum().reset_index(name="Valor")
total_ano['Valor'] = total_ano['Valor'].round(2)
ultimo_provento = df.tail(1)['Valor'].sum()
ultimo_6_meses = df.tail(6)['Valor'].sum()
ultimo_12_meses = df.tail(12)['Valor'].sum().round(2)


col1, col2, col3 = st.columns(3)

with col1:
   st.header("Mensal")
   st.subheader(f"R$ {ultimo_provento}")

with col2:
   st.header("Semestral")
   st.subheader(f"R$ {ultimo_6_meses}")

with col3:
   st.header("Anual")
   st.subheader(f"R$ {ultimo_12_meses}")

fig_mes = go.Figure()
for ano, grupo in df.groupby('Ano'):
    fig_mes.add_trace(go.Bar(
        x=grupo['Mes'],
        y=grupo['Valor'],
        name=str(ano),
        text=grupo['Valor'],
        textfont=dict(
            family='Arial',
            size=14,
        ),
    ))

fig_mes.update_layout(
    title='Total por Mês',
    yaxis_title='Valor',
    barmode='group',
)

anos = total_ano['Ano']
valores = total_ano['Valor']
# Criar o gráfico de barras
fig_total_ano = go.Figure()
fig_total_ano.add_trace(go.Bar(
    x=anos,
    y=valores,
    text=valores,
))
fig_total_ano.update_xaxes(tickvals=anos, ticktext=[str(ano) for ano in anos])
fig_total_ano.update_layout(
    title='Total por Ano',
    xaxis=dict(title='Ano'),
    yaxis=dict(title='Valor'),
)

st.write(fig_mes)
st.write(fig_total_ano)