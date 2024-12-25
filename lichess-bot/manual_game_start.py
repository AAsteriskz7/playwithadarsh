import requests
import time
import random

token = "lip_8XmKVTnURl2Q40CJNf8X"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

while True:
    # opponent = input("Who is the opponent you want to play (or type 'exit' to quit): ")
    # if opponent.lower() == 'exit':
    #     break
    opponentList = ["PetersBot", "RaspFish", "Mr-Chess-Berserk", "SwiggityBOTv1", "Alehkine_cat"]
    opponent = random.choice(opponentList)
    # opponent = "PetersBot"
    data = {
        "clock": {
            "limit": random.choice([300, 600, 900, 1200, 1500, 1800]),
            # "limit": 300,
            # "limit": int(input("What is the time limit you want to play with?")),
            "increment": random.randint(3, 15),
            # "increment": 5,
            # "increment": int(input("What is the increment you want to play with?"))
        },
        "rated": True,
        "variant": "standard"
    }

    response = requests.post(f"https://lichess.org/api/challenge/{opponent}", headers=headers, json=data)

    if response.status_code == 200:
        print(f"Challenge sent successfully to {opponent}!")
        print(f"Game details: Time limit - {int(data['clock']['limit'])/60} minutes, Increment - {data['clock']['increment']} seconds, Rated - {data['rated']}, Variant - {data['variant']}")
    else:
        print(f"Failed to send challenge: {response.status_code} - {response.text}")
    
    time.sleep(5 * 60)