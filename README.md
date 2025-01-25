 

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
  

<<<<<<< HEAD
=======
---

## 📂 Folder Structure
├── Network_Data/                        
│   └── PhishingData.csv              
├── final_models/                     
├── networksecurity/                  
│    ├── components/                   
│    │   ├── data_ingestion.py        
│    │   ├── data_transformation.py    
│    │   ├── data_validation.py       
│    │   └── model_trainer.py        
│    │
│    ├── constant/                     
│    │   └── training_pipeline/       
│    │       └── __init__.py          
│    │
│    ├── entity/                      
│    │   ├── artifact_entity.py       
│    │   └── config_entity.py        
│    │
│    ├── exception/                   
│    │   └── exception.py            
│    │
│    ├── logging/                     
│    │   └── logger.py               
│    │
│    ├── pipeline/                    
│    │   └── training_pipeline.py    
│    │
│    └── utils/                       
│        ├── main_utils/              
│        │   └── utils.py            
│        └── ml_utils/               
│            ├── metric/             
│            │   └── classification_metric.py
│            └── model/              
│                └── estimator.py    
├── requirements.txt                
├── README.md                       
└── LICENSE


      





>>>>>>> e0c529d6b0419eef33b69bf4b4acd5d353e47d54
## 🛠️ Installation and Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Moulik-23/NetworkSecurity.git
   ```
2. Navigate to the project directory:
   ```bash
   cd NetworkSecurity
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Dataset

The dataset includes features extracted from URLs and labels indicating whether a website is fake or legitimate. 

---

## 🚀 How to Run

1. Just Run the app.py Python script
   This Script will automatically invoke all steps

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

<<<<<<< HEAD
=======
Does this cover everything? Let me know if you'd like to tweak any part further! 😊
>>>>>>> e0c529d6b0419eef33b69bf4b4acd5d353e47d54
