import os
import re
import json
import requests
import datetime

from dotenv import load_dotenv

from bs4 import BeautifulSoup

from tqdm import tqdm
from typing import List, Dict

from extractor import Extractor


class NewsListener:
    def __init__(
        self,
        key: str,
        keywords: List[str] = ["murder", "kill", "burglar", "kidnap", "hit and run"],
        domains: List[str] = [
            "indianexpress.com",
            "millenniumpost.in",
            "timesofindia.indiatimes.com",
            "thehindu.com",
            "hindustantimes.com",
            "indiatvnews.com",
        ],
    ) -> None:
        self._key = key
        self.keywords = keywords
        self.domains = domains
        self.date = datetime.datetime.now().date().strftime("%y-%m-%d")
        self.url = f"https://newsapi.org/v2/everything?domains={','.join(self.domains)}&from={self.date}&apiKey={self._key}"

    def get(self) -> Dict:
        response = requests.get(self.url).json()
        data = {"id": id(response), "records": []}
        for article in tqdm(response["articles"]):
            for keyword in self.keywords:
                if (
                    keyword in article["title"]
                    or keyword in article["description"]
                    or keyword in article["content"]
                ):
                    record = {
                        "source": article["source"],
                        "title": article["title"],
                        "url": article["url"],
                        "splash_url": article["urlToImage"],
                        "prompt": self.scrape(article["url"]),
                    }
                    data["records"].append(record)
        return data

    def clean(self, text):
        special_chars = re.compile(r"[^\w\s]")
        web_address = re.compile(r"http(s)?://[a-z0-9.~_\-\/]+")
        unicode = re.compile(r"\\u[0-9a-fA-F]{4}")

        text = re.sub(unicode, "", text)
        text = re.sub(web_address, "", text)
        text = re.sub(special_chars, "", text)

        text = text.replace("\n", " ")
        text = text.replace("\t", " ")

        return text

    def scrape(self, url: str) -> Dict:
        response = requests.get(url).text
        soup = BeautifulSoup(response, "html.parser")
        extractor = Extractor()
        res = extractor(soup.get_text())
        print(res)
        return res


if __name__ == "__main__":
    load_dotenv()

    nL = NewsListener(key=os.getenv("NEWS_API_KEY"))

    with open("./dump.json", "w") as json_file:
        json.dump(nL.get(), json_file, indent=4)
