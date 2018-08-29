import json
import requests
from watson_developer_cloud import ConversationV1


def lambda_handler(event, context):

    msg = watson_conversation('techcafeって？')
    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": msg, "location": ip.text.replace("\n", "")}
        ),
    }

def watson_conversation(msg):

    conversation = ConversationV1(
        version='2017-10-16',
        username='c2a983fe-e55f-40a7-b694-e169ef0e2efa',
        password='XRbVt8Bxp5G7',
        url='https://gateway.watsonplatform.net/assistant/api'
    )

    response = conversation.message(
        workspace_id='ae9b1b53-034b-4dcf-ba5a-f5bef3fd6b8e',
        input={
            'text': msg
        }
    )

    print(json.dumps(response, ensure_ascii=False, indent=2))
    return response['output']['text'][0]
