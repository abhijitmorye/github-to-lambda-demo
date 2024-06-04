import requests
import pandas as pd
import boto3

sns_client = boto3.client('sns')
sns_arn = 'arn:aws:sns:us-east-2:992382775813:amz-sns-topic-001'


def lambda_handler(event, context):

    try :
        print('In try block now, accessing the url')
        data = {"Key_1": [1, 2, 3], "key_2": [5, 6, 7]}
        dataframe = pd.DataFrame(data)
        print(dataframe)
        message = "Dataframe created"
        response = sns_client.publish(Subject="SUCCESS - Daily Data Processing",TargetArn=sns_arn, Message=message, MessageStructure='text')
    except Exception as err:
        print(err)
        message = "Dataframe failed"
        response = sns_client.publish(Subject="Failure - Daily Data Processing", TargetArn=sns_arn, Message=message,
                                      MessageStructure='text')

