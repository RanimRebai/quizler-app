import requests

TYPE = "boolean"
AMOUNT = 10

PARAMETES = {"amount": AMOUNT,
             "type": TYPE,}

response = requests.get("https://opentdb.com/api.php",PARAMETES)
question_data = response.json()["results"]

print(question_data)



