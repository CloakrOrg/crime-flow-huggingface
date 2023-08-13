import os
import time
from datetime import datetime, timedelta
import json

import requests
from tqdm import tqdm
from dotenv import load_dotenv

from news_listener import NewsListener


def listen():
    print("Scraping outlets...")
    lstn = NewsListener(key=os.getenv("NEWS_API_KEY"))

    print("Pushing to database...")
    for payload in tqdm(lstn.get()["records"]):
        resp = requests.post(
            url="https://cloakr-backend.vercel.app/crime", json=payload
        )


def time_until_next_execution():
    DELTA = 5
    # DELTA = 86400
    now = time.time()
    midnight = now - (now % DELTA) + DELTA
    return midnight - now


if __name__ == "__main__":
    load_dotenv()

    while True:
        current_time = datetime.now()
        next_execution_time = time_until_next_execution()
        next_refresh_time = current_time + timedelta(seconds=next_execution_time)

        last_updated = current_time.strftime("%I:%M%p, %d-%m-%Y")
        next_refresh = next_refresh_time.strftime("%I:%M%p, %d-%m-%Y")

        print(f"Last updated: {last_updated}. Will refresh in: {next_refresh}")

        time.sleep(next_execution_time)
        listen()
