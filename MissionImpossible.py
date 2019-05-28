import requests
import base64
from collections import Counter
import re

QUEST_ENDPOINT = "https://missionimpossible.appspot.com/"

QUEST_1_URL_CALCULATOR = QUEST_ENDPOINT + "api/calculator"
QUEST_1_GET_CODE_URL = QUEST_ENDPOINT + "api/secret?code="
QUEST_2_FIRST_WEB_PAGE_URL = QUEST_ENDPOINT + "FirstWebPageInTheWorld.html"
QUEST_4_DOORLOCK_URL = QUEST_ENDPOINT + "api/doorlock?code="


def mathematic_manipulations(a, b):
    QUEST_1_REQUEST = {'a': a, 'b': b}
    r = requests.post(QUEST_1_URL_CALCULATOR, json=QUEST_1_REQUEST)
    print(r.text)


def get_first_secret_code(code):
    response = requests.get(QUEST_1_GET_CODE_URL + code)
    return response.text


