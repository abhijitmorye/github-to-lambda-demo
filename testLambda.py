import requests
import pandas as pd


def lambda_handler(event, context):
    url = 'http://echo.jsontest.com/key/value/one'
    data = []
    for i in range(100):
        response = requests.get(f'{url}/{i}')
        data.append(response.json())

    dataframe = pd.DataFrame(data)
    print(dataframe)

lambda_handler('a', 'b')
