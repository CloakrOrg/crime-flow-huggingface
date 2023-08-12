from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

C = C = """Days after a 65-year-old man was shot dead at his Moga residence in an alleged fallout of a clash that took place in the prison where his history-sheeter son is lodged, the Punjab Police on Friday arrested wanted gangster Gopi Dallewalia, saying he was “a key associate involved in the murder”.

On July 16, four assailants had barged into Santokh Singh’s house and shot him dead. Santokh’s son Sukhdev Singh is lodged in Faridkot jail with at least 19 cases registered against him.

Police said the entire conspiracy was planned from jail after Sukhdev had clashed with gangster Gaurav Sharma alias Goru Bacha in Faridkot jail. Subsequently, the police said, Goru and his accomplices planned to kill Sukhdev’s father. As per preliminary investigations, the police added, gangsters Dallewalia and Goru Bacha were the masterminds behind Santokh’s murder.

“In an intelligence-led operation, Anti-Gangster Task Force (AGTF) & Moga Police have arrested gangster Gurpreet Singh @ Gopi Dallewalia of Goru Baccha group. Gopi was the key associate involved in the murder of Santokh Singh at Moga in July 2023. He was convicted in 4 criminal cases and a proclaimed offender in a murder case at Goraya in 2016. A pistol along with 5 live cartridges has been recovered from the accused,” Punjab Director General of Police Gaurav Yadav said.

On July 28, police had arrested three shooters from this gang in the case – Nirmal Singh alias Nimma, Aprail Singh alias Shera and Jaskaran Singh alias Karan.

A Ludhiana-based gangster, Goru Bacha and his supporters had clashed with Sukhdev and his supporters inside Faridkot jail a few days ago. After Santokh’s murder, an accomplice of Bacha had purportedly posted a Facebook status claiming responsibility for it, terming it as “revenge” for “harming Goru” in jail."""

nlp = pipeline("question-answering", model=model_name, tokenizer=model_name)
QA_input = {"question": "Who is the criminal?", "context": C}
res = nlp(QA_input)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
