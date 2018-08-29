import json
import requests
from watson_developer_cloud import ConversationV1


def lambda_handler(event, context):
    """
    event:
        token=XXXXXXXXXXXXXXXXXX
        team_id=T0001
        team_domain=example
        channel_id=C2147483705
        channel_name=test
        thread_ts=1504640714.003543
        timestamp=1504640775.000005
        user_id=U2147483697
        user_name=Steve
        text=googlebot: What is the air-speed velocity of an unladen swallow?
        trigger_word=googlebot:
    """

    msg = watson_conversation(event['text'])
    print(msg)
    return {
        "text": msg
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

    # print(json.dumps(response, ensure_ascii=False, indent=2))
    return response['output']['text'][0]
