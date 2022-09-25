import streamlit as st
import pandas as pd

from utils.database import change_dict_format, get_mongo_client
from utils.database import create_dataframe_from_cursor
from utils.database import change_date_format
from utils.nutrition import revisar_grasa
from utils.nutrition import revisar_musculo
from utils.nutrition import revisar_IMC

def actualizar_valores():
    if 'actualizar' in st.session_state.keys():
        return True
    else: 
        return False

def activar_actualiazr():
    st.session_state["actualizar"] = True

client = get_mongo_client()
database = client.nutridb
collection = database.consultas

st.header("Pacientes registrados")

cursor = collection.find({})
df = create_dataframe_from_cursor(cursor)
df_dict = df.to_dict("index")
new_dict = change_dict_format(df_dict)
unique_df = pd.DataFrame(new_dict).T
unique_df = unique_df["fecha"]
unique_df = unique_df.rename("Fecha de ultima consulta")
st.dataframe(unique_df)

paciente_seleccionado = st.selectbox(label="Seleccione el paciente" ,options=unique_df.index)

actualizar = st.button(label="Actualizar datos", on_click=activar_actualiazr)

if actualizar_valores():

    st_cols_header = st.columns(2)

    paciente = {}

    paciente["sexo"] = df.loc[df["nombre"] == paciente_seleccionado].iloc[0]["sexo"]

    paciente["fecha"] = str(st_cols_header[0].date_input("Fecha de la consulta"))

    paciente["fecha"] = change_date_format(paciente["fecha"])
    
    paciente["edad"] = st_cols_header[1].text_input("Edad del paciente")

    st_cols_paciente = st.columns(3)

    paciente["peso"] = st_cols_paciente[0].text_input("Peso del paciente (kg)", key="weigth")

    paciente["grasa"] = st_cols_paciente[1].text_input("Porcentaje de grasa")

    paciente["musculo"] = st_cols_paciente[2].text_input("Porcentaje de musculo")

    paciente["grasa_vis"] = st_cols_paciente[0].text_input("Porcentaje de grasa visceral")

    paciente["edad_meta"] = st_cols_paciente[1].text_input("Edad metabólica")

    comparar = st.button(label="Comparar valores")

    if comparar:

        paciente["altura"] = df.loc[df["nombre"] == paciente_seleccionado].iloc[0]["altura"]

        paciente["IMC"] = float(paciente["peso"]) / (float(paciente["altura"]) * float(paciente["altura"]))

        st.subheader("Comparación")

        print(df.loc[df["nombre"] == paciente_seleccionado].iloc[0])


        comparison_dict = {
            "antes" : {},
            "despues" : {}
        }

        for key in paciente:
            comparison_dict["antes"][key] = df.loc[df["nombre"] == paciente_seleccionado].iloc[0][key]
            comparison_dict["despues"][key] = paciente[key]

        comparison_dataframe = pd.DataFrame(comparison_dict).astype(str)

        comparison_dataframe = comparison_dataframe.T[["peso","grasa","musculo","grasa_vis","IMC"]]

        st.dataframe(comparison_dataframe)

        st.subheader("Porcentaje de grasa")

        datos_grasa = revisar_grasa(paciente)
        estado = datos_grasa["estado"]

        if estado != "normal":
            direccion = datos_grasa["direccion"]
            faltante = abs(datos_grasa["faltante"])
            faltante_kg = datos_grasa["faltante_kg"]

            st.warning(f"Tu porcentaje de grasa es {estado} 😥. Tienes que {direccion} un {faltante:.2f} por ciento, o visto de otra manera, {direccion} {faltante_kg:.2f} kilos de grasa.")

        else:
            st.success("Tu porcentaje de grasa es normal! 😁")

        st.subheader("Porcentaje de musculo")

        datos_musculo = revisar_musculo(paciente)
        estado = datos_musculo["estado"]

        if estado != "normal":
            direccion = datos_musculo["direccion"]
            faltante = abs(datos_musculo["faltante"])
            faltante_kg = datos_musculo["faltante_kg"]

            st.warning(f"Tu porcentaje de músculo es {estado} 😥. Tienes que {direccion} un {faltante:.2f} por ciento, o visto de otra manera, {direccion} {faltante_kg:.2f} kilos de músculo.")

        else:
            st.success("Tu porcentaje de músculo es normal! 😁")
        
        st.subheader("IMC")

        datos_IMC = revisar_IMC(paciente)
        estado = datos_IMC["estado"]

        if estado != "normal":
            direccion = datos_IMC["direccion"]
            faltante = abs(datos_IMC["faltante"])

            st.warning(f"Tu IMC es {estado} 😥. Tienes que {direccion} {faltante:.2f} kg para regresar a un valor normal.")

        else:
            st.success("Tu IMC es normal! 😁")



      
