from transformers import pipeline


class Extractor:
    def __init__(self) -> None:
        self.model = "deepset/roberta-base-squad2"
        self.pipeline = pipeline(
            "question-answering", model=self.model, tokenizer=self.model
        )

    def __call__(self, context: str) -> dict:
        ret = {}
        prompts = {
            "location": "What is the location of the crime???",
            "suspect": "Who is/are the criminal(s)?",
            "victim": "Who is/are the victim(s)?",
        }

        for attr, prompt in prompts.items():
            ret[attr] = self.pipeline({"question": prompt, "context": context})[
                "answer"
            ]

        return ret
