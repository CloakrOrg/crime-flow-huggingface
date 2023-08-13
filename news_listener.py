import os
import re
import json
import requests
import datetime

from dotenv import load_dotenv
from bs4 import BeautifulSoup

from tqdm import tqdm
from typing import List, Dict

import utils
from extractor import Extractor


class NewsListener:
    def __init__(
        self,
        key: str,
        keywords: List[str] = [
            "murder",
            "kill",
            "burglar",
            "kidnap",
            "hit and run",
            "suspect",
            "criminal",
            "victim",
        ],
        domains: List[str] = [
            "indianexpress.com",
        ],
    ) -> None:
        self._key = key
        self.keywords = keywords
        self.domains = domains
        self.date = datetime.datetime.now().date().strftime("%y-%m-%d")
        self.url = f"https://newsapi.org/v2/everything?domains={','.join(self.domains)}&from={self.date}&apiKey={self._key}"

    def get(self) -> Dict:
        response = requests.get(self.url).json()
        data = {"date": self.date, "records": []}
        for article in tqdm(response["articles"]):
            for keyword in self.keywords:
                if (
                    keyword in article["title"]
                    or keyword in article["description"]
                    or keyword in article["content"]
                ):
                    payload = self.scrape(article["url"])
                    record = {
                        "title": article["title"],
                        "description": payload["description"],
                        "date": self.date,
                        "state": "WB",
                        "type": "unverified",
                        "suspect": payload["suspect"],
                        "victim": payload["victim"],
                        "image": article["urlToImage"],
                    }
                    for state, code in utils.state_dict.items():
                        if state in article["content"].lower():
                            record["state"] = code
                    data["records"].append(record)
        return data

    def clean(self, text):
        special_chars = re.compile(r"[^\w\s]")
        web_address = re.compile(r"http(s)?://[a-z0-9.~_\-\/]+")
        unicode = re.compile(r"\\u[0-9a-fA-F]{4}")

        text = re.sub(unicode, " ", text)
        text = re.sub(web_address, " ", text)
        text = re.sub(special_chars, " ", text)

        text = text.replace("\n", " ")
        text = text.replace("\t", " ")

        return text

    def scrape(self, url: str) -> Dict:
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        target = soup.find("div", class_="full-details")
        children = target.find_all("p")
        content = " ".join([p.get_text() for p in children])
        extractor = Extractor()
        res = extractor(content)
        return res


if __name__ == "__main__":
    load_dotenv()

    nL = NewsListener(key=os.getenv("NEWS_API_KEY"))

    with open("./dump.json", "w") as json_file:
        json.dump(nL.get(), json_file, indent=4)
