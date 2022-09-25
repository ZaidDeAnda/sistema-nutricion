import streamlit as st

import warnings

from utils.database import get_mongo_client
from utils.database import change_date_format

warnings.filterwarnings('ignore')


client = get_mongo_client(secrets_dict=st.secrets)
database = client.nutridb
collection = database.consultas

st.header("Datos del paciente")

paciente = {}


paciente["nombre"] = st.text_input("Nombre del paciente")

st_cols_header = st.columns(3)

paciente["fecha"] = str(st_cols_header[0].date_input("Fecha de la consulta"))

paciente["fecha"] = change_date_format(paciente["fecha"])

paciente["edad"] = st_cols_header[1].text_input("Edad del paciente")

paciente["sexo"] = st_cols_header[2].selectbox(label="Sexo del paciente", options=["masculino", "femenino"])

st_cols_paciente = st.columns(3)

paciente["altura"] = st_cols_paciente[0].text_input("Altura del paciente (m)", key="height")

paciente["peso"] = st_cols_paciente[1].text_input("Peso del paciente (kg)", key="weigth")

paciente["grasa"] = st_cols_paciente[2].text_input("Porcentaje de grasa")

paciente["musculo"] = st_cols_paciente[0].text_input("Porcentaje de musculo")

paciente["grasa_vis"] = st_cols_paciente[1].text_input("Porcentaje de grasa visceral")

paciente["edad_meta"] = st_cols_paciente[2].text_input("Edad metabólica")

submit = st.button("Registrar paciente")

if submit:

    paciente["IMC"] = float(paciente["peso"]) / (float(paciente["altura"]) * float(paciente["altura"]))

    collection.insert_one(paciente)

    st.success("Paciente registrado correctamente")



