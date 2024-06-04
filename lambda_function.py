import requests
import pandas as pd


def lambda_handler(event, context):
    url = 'http://echo.jsontest.com/key/value/one/100'
    response = requests.get(url)
    dataframe = pd.DataFrame(response.json())
    print(dataframe)
