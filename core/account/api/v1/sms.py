from kavenegar import *
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')


def send_sms():
    try:
        api = KavenegarAPI(api_key)
        params = {
            'sender': '2000500666',
            'receptor': '09991377711',
            'message': 'Hello, this is a test message from your server.',
        }
        response = api.sms_send(params)
        print(str(response))

    except APIException as e:
        print(str(e))

    except HTTPException as e:
        print(str(e))


send_sms()
