import streamlit as st
import pandas as pd

# CONFIGURACIÓN
st.set_page_config(
    page_title="Sistema de Notas",
    layout="wide"
)

# TÍTULO
st.title("📚 Sistema de Consulta de Notas")

# LEER EXCEL
archivo = "Repositorio de Notas.xlsx"

df = pd.read_excel(archivo)

# BUSCADOR
busqueda = st.text_input(
    "Ingrese código o nombre del estudiante"
)

if busqueda:

    filtro = df[
        df.iloc[:,10].astype(str).str.contains(busqueda, case=False, na=False)
        |
        df.iloc[:,11].astype(str).str.contains(busqueda, case=False, na=False)
    ]

    if len(filtro) > 0:

        st.success(f"Se encontraron {len(filtro)} resultado(s)")

        columnas = [
            df.columns[10],
            df.columns[11],
            df.columns[1],
            df.columns[9],
            df.columns[8],
            df.columns[7]
        ]

        st.dataframe(
            filtro[columnas],
            use_container_width=True
        )

    else:
        st.error("No se encontraron resultados")