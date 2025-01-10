# Sistema de Nutrición

## Tabla de Contenidos

- [Acerca del Proyecto](#acerca-del-proyecto)
- [Contenido del Proyecto](#contenido-del-proyecto)
- [Desarrollo del Proyecto](#desarrollo-del-proyecto)
  - [Prerequisitos](#prerequisitos)
  - [Iniciando](#iniciando) 
  - [Instalación](#instalación)   
  - [Ejecución](#ejecución)  
- [Uso del proyecto](#uso-del-proyecto)
- [Contacto](#contacto)
- [Licencia](#licencia)

---

## Acerca del Proyecto

El Sistema de Nutrición es un proyecto que desarrolla una aplicación de gestión nutricional enfocada para nutriólogos. 

Fue desarrollado para optimizar el trabajo de los nutriólogos al proporcionar una plataforma que abarque todas las funcionalidades primordiales de gestión y seguimiento de pacientes en uno. La aplicación aborda la necesidad de manejar datos de manera ágil, organizada y visualmente atractiva.

La aplicación le permite a los profesionales:

- Registrar nuevos pacientes.
- Almacenar y actualizar el expediente de pacientes, incluyendo peso, grasa, músculo, IMC y otros parámetros.
- Comparar datos históricos con registros actuales.
- Clasificar a los pacientes en base a sus porcentajes de parámetros como altos, medios y bajos.
- Visualizar el historial de los pacientes para monitorear su progreso a lo largo del tiempo.

La aplicación está desarrollada con Python utilizando Streamlit como base para la interfaz web y MongoDB Atlas para el almacenamiento de la base de datos en la nube.

## Contenido del proyecto

El proyecto ofrece las siguientes tres páginas con sus respectivas funcionalidades:
- Una página para registrar nuevos pacientes.
- Una página para actualizar los expedientes de pacientes, la cual permite:
  - Mostrar una tabla con todos los pacientes registrados.
  - Permitir la selección de un paciente para actualizar sus parámetros.
  - Mostrar una comparación entre el último registro y el recién ingresado.
  - Indicadores que clasifiquen los parámetros de un paciente dentro de los rangos de nutrición.
- Una página para consultar el histórico de un expediente de un paciente.

El Sistema de Nutrición se creó para abordar los desafíos que enfrentan los nutriólogos al gestionar los datos de sus pacientes de manera efectiva. La motivación detrás del proyecto fue simplificar el proceso de seguimiento y análisis del progreso de los pacientes mientras se proporciona una interfaz intuitiva y visualizaciones útiles. La aplicación elimina la necesidad de llevar registros manuales y reduce errores, convirtiéndola en una herramienta confiable para los profesionales.

---

## Desarrollo en el proyecto

### Prerequisitos

 - Python
 - Powershell/bash
 - MongoDB
 - Streamlit

### Iniciando

Sigue estos pasos para configurar y ejecutar el Sistema de Nutrición:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/ZaidDeAnda/sistema-nutricion.git
   ```

2. **Navega al directorio del proyecto:**
   ```bash
   cd ruta/al/proyecto/sistema-nutricion
   ```

### Instalación

1. **Crea un entorno virtual de Python**
   ```bash
   python3 -m venv venv
   ```

2. **Accede al entorno virtual:**
   Para Linux/Mac:
   ```bash
   source venv/bin/activate
   ```
   Para Windows:
   ```bash
   source venv/Scripts/activate
   ```

3. **Instala los requisitos:**
     ```bash
   pip install -r requirements.txt
   ```

### Ejecución

1. **Ejecuta la aplicación:**
   ```bash
   streamlit run app.py
   ```

---

## Uso del Proyecto

1. **Registrar nuevos pacientes:**
   - Navega a la página **Añadir Paciente**.
   - Completa la información básica.
   - Haz clic en **Submit** para guardar el registro en la base de datos.

2. **Actualizar parámetros de un paciente:**
   - Navega a la página **Añadir Consulta**.
   - Visualiza una tabla con todos los pacientes registrados (mostrando nombres y la fecha de su último registro).
   - Selecciona un paciente.
   - Introduce los parámetros actualizadas.
   - Haz clic en **Actualizar datos** para guardar el nuevo registro.
   - Se mostrará una comparación entre el último registro y el recién ingresado.

3. **Ver datos históricos:**
   - Navega a la página **Histórico**.
   - Accede al historial de progreso de cada paciente.

---

## Contacto

- Zaid De Anda - https://github.com/ZaidDeAnda
- Project Link: https://github.com/ZaidDeAnda/sistema-nutricion.git

---

## License

Este proyecto posee la licencia [MIT License](LICENSE).  
Ve el archivo `LICENSE` para más detalles.

---