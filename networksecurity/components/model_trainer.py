import os
import sys
from networksecurity.expection.expection import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.artifact_entity import DataTransformationArtifact,ModelTrainerArtifact
from networksecurity.entity.config_entity import ModelTrainerConfig


from networksecurity.utils.main_utlis.utils import save_object,load_object
from networksecurity.utils.main_utlis.utils import load_numpy_array_data,evaluate_models
from networksecurity.utils.ml_utlis.model.estimator import NetworkModel
from networksecurity.utils.ml_utlis.metric.classifaction_metric import get_classification_score

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import(
    RandomForestClassifier,
    AdaBoostClassifier,
    GradientBoostingClassifier,
)
import warnings
warnings.filterwarnings('ignore')

import mlflow

import dagshub
dagshub.init(repo_owner='Moulik-23', repo_name='NetworkSecurity', mlflow=True)


class ModelTrainer:
    def __init__(self,model_trainer_config:ModelTrainerConfig,data_transformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config=model_trainer_config
            self.data_transformation_artifact=data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def track_mlflow(self,best_model,classificationmetric):
        with mlflow.start_run():
            f1_score=classificationmetric.f1_score
            precision_score=classificationmetric.precision_score
            recall_score=classificationmetric.recall_score

            mlflow.log_metric("f1_score",f1_score)
            mlflow.log_metric("precision",precision_score)
            mlflow.log_metric("recall_score",recall_score)
            mlflow.sklearn.log_model(best_model,"model")

    def train_model(self,X_train,y_train,X_test,y_test):
        
        models ={
            "Random Forest":RandomForestClassifier(verbose=1),
            "Decision Tree":DecisionTreeClassifier(),
            "Gradient Boosting":GradientBoostingClassifier(verbose=1),
            "Logistic Regression":LogisticRegression(verbose=1),
            "AdaBoost":AdaBoostClassifier(),
            }
        params={
            "Decision Tree": {
                'criterion':['gini', 'entropy', 'log_loss'],
                # 'splitter':['best','random'],
                # 'max_features':['sqrt','log2'],
            },
            "Random Forest":{
                #'criterion':['gini', 'entropy', 'log_loss'],
                
                #'max_features':['sqrt','log2',None],
                'n_estimators': [8,16,32,128,256]
            },
            "Gradient Boosting":{
                # 'loss':['log_loss', 'exponential'],
                'learning_rate':[.1,.01,.05,.001],
                'subsample':[0.6,0.7,0.75,0.85,0.9],
                # 'criterion':['squared_error', 'friedman_mse'],
                # 'max_features':['auto','sqrt','log2'],
                'n_estimators': [8,16,32,64,128,256]
            },
            "Logistic Regression":{},
            "AdaBoost":{
                'learning_rate':[.1,.01,.001],
                'n_estimators': [8,16,32,64,128,256]
            }
            
        }
        model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,
                                          models=models,param=params)
        
        ## To get best Model Score
        best_model_score = max(sorted(model_report.values()))

        ## To get best Model Name
        best_model_name = list(model_report.keys())[
            list(model_report.values()).index(best_model_score)
        ]
        best_model =models[best_model_name]
        y_train_pred = best_model.predict(X_train)

        classification_train_metric=get_classification_score(y_true=y_train,y_pred=y_train_pred)

        ## Track the mlflow
        self.track_mlflow(best_model,classification_train_metric)


        y_test_pred = best_model.predict(X_test)
        classification_test_metric = get_classification_score(y_true=y_test,y_pred=y_test_pred)
        self.track_mlflow(best_model,classification_test_metric)


        logging.info("Load object")
        preprocessor = load_object(file_path=self.data_transformation_artifact.transformed_object_file_path)

        model_dir_path = os.path.dirname(self.model_trainer_config.model_trained_file_path)
        os.makedirs(model_dir_path,exist_ok=True)
        logging.info("Saving Model.pkl ")
        Network_model=NetworkModel(preprocessor=preprocessor,model=best_model)
        save_object(self.model_trainer_config.model_trained_file_path,obj=Network_model)

        ## Model Pusher
        save_object("final_models/model.pkl",best_model)

        ## Model Trainer Artifact

        model_trainer_artifact=ModelTrainerArtifact(trained_model_file_path=self.model_trainer_config.model_trained_file_path,
                             train_metric_artifact=classification_train_metric,
                             test_metric_artifact=classification_test_metric
                             )
        logging.info(f"Model Trainer Artifact: {model_trainer_artifact}")       
        return model_trainer_artifact

    def initiate_model_trainer(self)->ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path
            
            ## Loading train and test array
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            X_train,y_train,X_test,y_test = (
                train_arr[:, :-1],
                train_arr[:,-1],
                test_arr[:, :-1],
                test_arr[:, -1]
            )
            model=self.train_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test)
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        