from langchain import HuggingFaceHub, LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceHub(repo_id="deepset/roberta-base-squad2")
prompt = PromptTemplate(input_variables=["text"], template="{text")

hub_chain = LLMChain(prompt=prompt, llm=llm, verbose=True)

print(hub_chain.run("What is the histpry of India?"))
