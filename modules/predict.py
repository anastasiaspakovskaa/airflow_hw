import dill
import os
import pandas as pd
import json


path = os.path.expanduser('~/airflow_hw')


model_path = path + '/data/models/cars_pipe_202401192000.pkl'
with open(model_path, 'rb') as file:
    model = dill.load(file)


def get_test_dir():
    tests_path = path + '/data/test'
    files = os.listdir(tests_path)
    return [tests_path + '/' + f for f in files if os.path.isfile(os.path.join(tests_path, f))]


def get_prediction(data):
    data_dict = json.loads(data)
    df = pd.DataFrame([data_dict])
    y = model.predict(df)

    ans_df = pd.DataFrame([{'id': df['id'][0],
                            'price': df['price'][0],
                            'prediction': y[0]}])
    return ans_df


def predict():
    tests = get_test_dir()
    columns = ['id', 'price', 'prediction']
    predictions = pd.DataFrame(columns={col: [] for col in columns})

    for test in tests:
        with open(test, 'r') as file:
            predictions = pd.concat([predictions, get_prediction(file.read())], ignore_index=True)

    predictions.to_csv(path + '/data/predictions/predictions.csv', index=False)


if __name__ == '__main__':
    predict()
