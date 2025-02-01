# Liver Cirrhosis Prediction using Machine Learning

## Project Description

This project implements a Flask-based web application for predicting liver cirrhosis stages based on patient data. It utilizes machine learning models trained on a dataset containing relevant clinical features.

## Features

- Web-based interface for data input and predictions.
- Flask backend for processing and model inference.
- Data preprocessing using SMOTE for handling class imbalance.
- Multiple models compared for accuracy and performance.

## Installation

To set up the project, follow these steps:

1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask server:
   ```sh
   python app.py
   ```
2. Open a web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Dependencies

Ensure the following Python packages are installed:

- Flask
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn (for SMOTE)
- Jupyter Notebook (for working with `.ipynb` files)

Install missing dependencies using:

```sh
pip install flask pandas numpy scikit-learn imbalanced-learn jupyter
```

## Project Structure

```
├── app.py                 # Flask application
├── index.html             # Web interface
├── liver_cirrhosis.csv    # Dataset
├── smotefds.ipynb         # Data preprocessing using SMOTE
├── final_compare_smote_normal_mrp.ipynb  # Model comparison notebook
├── fdsproject.ipynb       # Main project notebook
├── requirements.txt       # Dependencies (should be created)
```

## Contributors

- Your Name (Replace with actual names if needed)

## License

This project is licensed under the MIT License.

---


This project aims to assist medical profess\
ionals in predicting the progression of liver cirrhosis using advanced machine learning techniques. By leveraging patient data, it can provide insights into disease stages, helping doctors make informed decisions. The application features an interactive web-based tool for real-time predictions, backed by a robust Flask-based backend. The predictive models have been trained on a comprehensive dataset, ensuring accuracy and reliability. Additionally, techniques such as SMOTE are employed to address class imbalance, improving model performance.
