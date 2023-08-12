import requests


class Listener:
    def __init__(self) -> None:
        pass

    def get_news(self):
        res = requests.get(
            f"https://www.tmz.com/2023/08/04/bryan-kohberger-suspect-idaho-murders-college-student-stabbings-alibi-drive/"
        )
        print(res.text)


if __name__ == "__main__":
    l = Listener()
    l.get_news()
