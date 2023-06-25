import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import change_dict_format, get_mongo_client
from utils.database import create_dataframe_from_cursor
from utils.database import change_date_format

st.set_page_config(layout="wide")

client = get_mongo_client()
database = client.nutridb
collection = database.consultas

cursor = collection.find({})
df = create_dataframe_from_cursor(cursor)
pacientes = list(df['nombre'].unique())

paciente_seleccionado = st.selectbox(label="Seleccione el paciente" ,options=pacientes)

if paciente_seleccionado:

    paciente_df = df.loc[df['nombre'] == paciente_seleccionado]

    st.write(paciente_df)

    cols = st.columns(2)

    cols[0].subheader("Peso")

    fig = px.line(paciente_df, y="peso", x="fecha")

    fig.update_layout(
        width=500,
        height=500
    )

    cols[0].plotly_chart(fig)

    cols[1].subheader("Porcentaje de grasa")

    fig = px.line(paciente_df, y="grasa", x="fecha")

    fig.update_layout(
        width=500,
        height=500
    )

    cols[1].plotly_chart(fig)

    cols[0].subheader("Porcentaje de músculo")

    fig = px.line(paciente_df, y="musculo", x="fecha")

    fig.update_layout(
        width=500,
        height=500
    )

    cols[0].plotly_chart(fig)

    cols[1].subheader("Edad metabólica")

    fig = px.line(paciente_df, y="edad_meta", x="fecha")

    fig.update_layout(
        width=500,
        height=500
    )

    cols[1].plotly_chart(fig)
