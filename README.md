# Overview
This project aims to predict the price category of cars based on various features 
using machine learning techniques. The model is trained on a dataset that includes 
information such as the car's model, manufacturer, price, and other relevant attributes.

# Dataset
The dataset used for training and testing the model is included in the 'data/train' directory.
It contains next columns:
* id (record identifier) 
* url (sale record URL)
* region
* region_url 
* price
* year (year of manufacture)
* manufacturer 
* model 
* fuel (fuel type)
* odometer (mileage)
* title_status 
* transmission (transmission type)
* image_url 
* description
* state 
* lat (latitude)
* long (longitude)
* posting_date (posting date of the sales ad)
* price_category

# Usage
1. Clone the repository:

`git clone https://github.com/anastasiaspakovskaa/car_price_prediction/tree/master`

2. Open the project in your IDE.
3. Run 'modules/pipeline.py' to train the best model, and save it in the 'data/models' 
directory.
4. After training, run 'modules/predict.py' to save predictions in the 'data/predictions' 
directory.
5. The files to predict are stored in the 'data/test' directory, which contains JSON files.
You can modify these files to obtain different predictions.
6. If everything works, you can run this program using Apache Airflow. The 'dags' directory contains the 'dag_hw.py' file. Instructions on how to run Airflow can be found [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/pipeline.html).
