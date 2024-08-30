# CMPE-258-Deep-Learning-Project(Human Action Recognition)


### About Team
#### Team Name -GeekSquad
#### Team Members 
1. Ruchitha Reddy Koluguri(017434534)
2. Suresh Ravuri
3. Sri Vinay Appari
4. Harshavardhan Valmiki

## Project Folder Description
1. ml_flow - folder containing MLOPS Experiment tracking CSV Files and Screenshots
2. notebooks - folder containing model notebooks - CNN, CNN-RNN, Transformers 
3. test_videos - folder containing videos from youtube predicted in Gradio App
4. Video_and_PPT- folder contains the video explanation and PPT

## Google Colab Links 
1. Classification using CNN Google Colab Link - https://colab.research.google.com/drive/1bjCnm57-C_LqtqzMxYQf8-U9MPAHcl_Z?usp=sharing
2. Classification using CNN-RNN Google Colab Link - https://colab.research.google.com/drive/1JGubXmCQ2eqUzen1ukzBt8BMqGNjSpqq?usp=sharing
3. Classification using Transformers Google Colab Link - https://colab.research.google.com/drive/1ing3kEgz92I285EbG49d2wt-W9mg7unL?usp=sharing

#### Report Link :https://docs.google.com/document/d/1acOjN-HY9sL7OkX8zWCHWSNcJgivP6h4kY_57kaMtdQ/edit?usp=sharing

## Visualize the dataset:
![image](https://github.com/ruchithareddy269/258-Deep_learning-Project/assets/64256985/27ee59ad-9552-476f-95ae-9aa3fcf58394)

## MLFLOW and Databricks Visualizations:
![image](https://github.com/ruchithareddy269/258-Deep_learning-Project/assets/64256985/a8777b53-a6fc-45f9-9c43-87d33122b6d1)
![image](https://github.com/ruchithareddy269/258-Deep_learning-Project/assets/64256985/5d39bd3b-3846-4e09-aec7-ac9e03695019)
![image](https://github.com/ruchithareddy269/258-Deep_learning-Project/assets/64256985/4ba2d427-c79f-4455-9778-bc3fc62fc707)
![image](https://github.com/ruchithareddy269/258-Deep_learning-Project/assets/64256985/efac2636-effe-49a7-9b08-ed2445384454)


## Output:
![image](https://github.com/ruchithareddy269/258-Deep_learning-Project/assets/64256985/63d56b9a-08a8-4521-b8e0-4bc49462f68d)

## Model Results:

#### CNN Model:
Training Accuracy: 97.55%
Validation Accuracy: 98.95%
Test Metrics: Accuracy: 80.02%, AUC: 93.70%, Precision: 89.93%, Recall: 79.95%
Strengths: High precision and overall accuracy.
Weaknesses: Lower recall compared to other metrics.
#### CNN-RNN Model:
Accuracy: 57.59%
Strengths: Suitable for sequence data.
Weaknesses: Lower accuracy, indicating possible inefficiencies.
#### Transformers Model:
Accuracy: 88.84%
Strengths: Handles complex temporal dynamics effectively.
Weaknesses: Lower accuracy than CNN when evaluated on test data.
Conclusion: The CNN model outperforms the others in precision and validation accuracy, making it the best choice for scenarios requiring high accuracy and precision. Transformers offer advantages for complex temporal patterns but do not reach the CNN's raw performance levels.




#### Deployment
1. We deployed our project in Gradio.
