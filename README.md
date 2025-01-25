 

---

# Fake Website Detection using Machine Learning 🚀

This project aims to predict whether a website is fake or legitimate based on various input features. It is a machine learning-based solution for improving online security and combating phishing attacks.

---

## 🔍 Features

- **Input Features**: The model uses several features extracted from websites to make predictions, such as:
  - URL Length
  - Presence of `HTTPS`
  - Domain Age
  - Suspicious Keywords in the URL
  - IP Address in the URL
  - Having Sub Domain

- **Machine Learning Model**: A supervised learning model trained on labeled data to classify websites as fake or legitimate.

- **Technologies Used**:
  - Python 🐍
  - Pandas, NumPy (for data preprocessing)
  - Scikit-learn (for machine learning)
  - Flask,Uvicorn,FastApi(for Web Frameworks & Deployment)
  - Mlflow(For Managing the Machine Learning project)
  - Pymongo, cerifi(for Database Integration)
  - dill, pickle(for Serialization)

# NetworkSecurityProject

## Overview
This project focuses on building a robust pipeline for network security using machine learning. It includes modular components for data ingestion, validation, transformation, model training, and logging.

---

## Project Structure
```plaintext
📂 NetworkSecurityProject/
├── 📂 training_pipeline/
│   ├── __init__.py          # Initializes the training pipeline module
│   ├── constants.py         # Contains constants used in the pipeline
│   └── ...                  # Other pipeline scripts
├── 📂 networksecurity/
│   ├── 📂 exception/
│   │   └── exception.py     # Custom exception handling
│   ├── 📂 logging/
│   │   └── logger.py        # Logging configurations
│   └── 📂 utils/
│       └── utils.py         # Utility functions
├── 📂 data_schema/
│   └── schema.yaml          # Defines data schema for validation
├── 📂 logs/
│   └── [Timestamped logs]   # Logs generated during execution
├── 📂 Artifacts/
│   ├── 📂 Data_Ingestion/      # Outputs from data ingestion
│   ├── 📂 Data_Validation/     # Outputs from data validation
│   ├── 📂 Data_Transformation/ # Outputs from data transformation
│   └── 📂 Model_Trainer/       # Saved models and related artifacts
├── 📂 final_models/
│   ├── preprocessor.pkl     # Saved preprocessor object
│   └── model.pkl            # Trained ML model
├── 📄 app.py                # Main entry point to invoke and run the project
└── 📄 README.md             # Project documentation

  


## 🛠️ Installation and Run

1. Clone this repository:
   ```bash
   git clone https://github.com/Moulik-23/NetworkSecurity.git
   ```
2. Navigate to the project directory:
   ```bash
   cd NetworkSecurity
   ```
4. Create and Activate a Virtual Environment:
   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   On Mac and Linux
   ```bash
   python3 -m venv venv
   source venv/bin/activate


3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4.Run the File
   python app.py

---

## 📊 Dataset

The dataset includes features extracted from URLs and labels indicating whether a website is fake or legitimate. 

---
## How It Works
1. Data Ingestion: Loads and preprocesses network data for analysis.

2. Data Transformation: andles feature engineering and prepares data for modeling.

3. Data Validation: Ensures that the input data conforms to predefined rules using schema.yaml.

4. Model Trainer: trains and evaluates the machine learning model.

Pipeline Execution:
Fetch Data.
 
Transforms data.
 
Validate Data.

Trains the machine learning model.

Saves transformed data and trained models for reuse.

Logging: Generates timestamped log files for debugging and monitoring.
---

## 📈 Results

- **Precision**: 98.85%
- **Recall**: 99.37%
- **F1 Score**: 99.11%



---

## 🔒 Use Cases

1. Identify phishing websites.
2. Enhance online security.
3. Assist in creating browser extensions for real-time detection.

---
Future Improvements
 - Model Deployment: Deploy the trained model using cloud platforms like AWS, Azure, or GCP.
 - Real-Time Data Processing: Integrate real-time processing with tools like Apache Kafka.
 - Advanced Visualizations: Add dashboards for monitoring network activity and anomalies.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📨 Contact

For any questions or feedback, feel free to reach out:  
**Email**: moulikzinzala912@example.com  
**GitHub**: [Moulik-23](https://github.com/Moulik-23)  

---




