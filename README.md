# Project Title

**Sistema de Nutrición**

## What does your application do and why did you use the technologies you used?

Sistema de Nutrición is a comprehensive nutrition management application designed for nutritionists. It allows professionals to:

- Register new patients.
- Store and update patient parameters, including weight, fat, muscle, BMI, and other metrics.
- Compare historical data to current records.
- Classify patients based on their recorded percentages into high, medium, and low ranges of fat, muscle, etc.

The application is built using Python with libraries such as:

- **Streamlit**: For creating an interactive and user-friendly web interface.
- **pymongo**: For seamless interaction with the MongoDB database.
- **yaml**: For configuration management.
- **datetime**: To handle timestamps for records.
- **pandas**: For data manipulation and analysis.
- **plotly express**: For creating interactive visualizations.

The database is hosted on MongoDB Atlas for robust, not relational and scalable cloud-based storage.

### Features to implement in the future

- A page to register new patients with their basic information and initial weight status.
- A page to update patient records, including:
  - Displaying a table of all registered patients.
  - Allowing selection of a patient to update their weight and metrics.
  - Displaying a comparison between the last and the newly entered record.
  - Indicators to show if a patient’s values are within recommended ranges.
- Enhancing the historical page to provide more detailed progress analysis and trend visualizations.

---

## Project Description

Sistema de Nutrición was developed to streamline the work of nutritionists by providing an all-in-one platform for patient management and progress tracking. The application addresses the need for an efficient, organized, and visually appealing way to handle patient data.

Sistema de Nutrición was developed to address the challenges faced by nutritionists in managing patient data effectively. The motivation behind the project was to simplify the process of tracking and analyzing patient progress while providing an intuitive interface and insightful visualizations. The application eliminates the need for manual record-keeping and reduces errors, making it a reliable tool for professionals.

---

## Table of Contents

- [Project Title](#project-title)
- [Project Description](#project-description)
- [Table of Contents](#table-of-contents)
- [How to Install and Run the Project](#how-to-install-and-run-the-project)
- [How to Use the Project](#how-to-use-the-project)
- [License](#license)

---

## How to Install and Run the Project

Follow these steps to set up and run NutriApp:

1. **Clone the repository:**
   ```bash
   git clone [repository URL]
   ```

2. **Navigate to the project directory:**
   ```bash
   cd [project-folder]
   ```

3. **Set up the environment variables:**
   - Create a `.env` file
   - Example:
     ```env
     MONGO_URI=<your-mongo-uri>
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   streamlit run anadir_paciente.py
   ```

---

## How to Use the Project

1. **Register New Patients:**
   - Navigate to the **Añadir Paciente** page.
   - Fill in basic information and initial weight status.
   - Click **Submit** to save the record in MongoDB.

2. **Update Parameters of a Patient:**
   - Navigate to the **Añadir Consulta** page.
   - View a table of all registered patients (showing names and the date of their last record).
   - Use the box to select a patient.
   - Enter updated metrics.
   - Click **Actualizar datos** to save the new record.
   - A comparison between the last and current record will be displayed below.

3. **View Historical Data:**
   - Navigate to the **Histórico** page.
   - Access detailed progress history for each patient.
   - View trends and changes in metrics like weight, fat, muscle, and BMI over time.
   - Visualizations provide insights into progress and whether metrics are within recommended ranges.

---

## License

This project is licensed under the [MIT License](LICENSE).  
See the `LICENSE` file for more details.

---
