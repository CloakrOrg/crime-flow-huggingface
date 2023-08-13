import re

from transformers import pipeline


class Extractor:
    def __init__(self) -> None:
        self.model = "deepset/roberta-base-squad2"
        self.pipeline = pipeline(
            "question-answering", model=self.model, tokenizer=self.model
        )

    def clean(self, text):
        pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"  # Emojis
            "\U0001F300-\U0001F5FF"  # Symbols & Pictographs
            "\U0001F680-\U0001F6FF"  # Transport & Map Symbols
            "\U0001F700-\U0001F77F"  # Alchemical Symbols
            "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            "\U0001FA00-\U0001FA6F"  # Chess Symbols
            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
            "\U00002702-\U000027B0"  # Dingbats
            "\U000024C2-\U0001F251"
            "]+",
            flags=re.UNICODE,
        )
        return pattern.sub(r"", text)

    def __call__(self, context: str) -> dict:
        ret = {"description": self.clean(context)}
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


if __name__ == "__main__":
    obj = Extractor()
    print(
        obj(
            "The Bharatiya Nagarik Suraksha Sanhita, 2023 proposes several important changes to the Criminal Procedure Code (CrPC) which guides the criminal justice system. From technological changes to allow trials via video-conferencing to allowing handcuffs for the arrest of persons in some cases including murder, rape, and counterfeit currency — these are some of the main changes proposed in the CrPC. Greater use of technology Trials, appeal proceedings, recording of depositions including those of public servants and police officers, may be held in electronic mode, the Bill states. The statement of the accused too can be recorded through video-conferencing. Summons, warrants, documents, police reports, statements of evidence can be done in electronic form. The search and seizure of articles and properties, the visit to a crime scene by a forensic expert, and the recording of the victim’s statement shall be audio-videographed, preferably on a mobile phone. The name and address of an arrested accused and the nature of the offence will be maintained by a designated officer in each police station and district, and shall be “prominently displayed” including in digital mode in every police station and district headquarters. Information to police too can be sent electronically, and it shall be taken on record on being signed by the person sending it, within three days. Communication devices The Bill adds electronic communication including “communication devices” to the provision on summons to produce a document. On the directions of a court or police officer, a person is required to produce any document — and now devices — that is likely to contain digital evidence for the purpose of an inquiry. Electronic communication is defined as “the communication of any written, verbal, pictorial information or video content transmitted (whether from one person to another, from one device to another or from a person to a device or from a device to a person).” Use of handcuffs A police officer may be permitted to use handcuffs while arresting a person if he is a habitual, repeat offender who escaped from custody, or has committed an organised crime, terrorist act, drug-related crime, illegal possession of arms, murder, rape, acid attack, counterfeit currency, human trafficking, sexual offence against children or offences against the state. Specific safeguards Section 41A of CrPC — which has a prominent safeguard against arrests — will get a new number, Section 35. It has an additional provision: no person can be arrested without prior permission of an officer, not below the rank of a deputy SP, in cases where the offence is punishable with less than three years, or if the person is infirm above 60 years of age. On receiving information in cognizable cases where the offence attracts 3-7 years, the police officer will conduct a preliminary inquiry to ascertain whether there exists a prima facie case to proceed within 14 days. Mercy petitions There is a provision on procedures for the timeframe to file mercy petitions in death sentence cases. After being informed by jail authorities about the disposal of the petition of a convict sentenced to death, he, or his legal heir or relative can submit a mercy petition within 30 days to the Governor. If rejected, the person can petition the President within 60 days. No appeal against the order of the President shall lie in any court. Sanction to prosecute A decision to grant or reject sanction to prosecute a public servant must be reached by the government within 120 days of receiving a request. If the government fails to do so, the sanction will be deemed to have been accorded. No sanction is required in cases including sexual offences, trafficking, etc. Arms in procession Section 144A of the CrPC gives the district magistrate the power to prohibit the carrying of arms in any procession, mass drill or mass training, to preserve the public peace. While the provisions granting powers to the DM to pass orders in urgent cases of nuisance or apprehended danger remain as they are in Section 144 of the CrPC, the provision to prohibit carrying arms does not find a mention. Samples without arrest The Bill has provisions for the magistrate to order any person to give samples of his signature, handwriting, voice or finger impressions for the purpose of investigation without being arrested. Detention by police There are provisions for police to detain or remove any person resisting, refusing or ignoring, or disregarding directions given as part of preventive action. 👉🏼 From holding trials on video to community service as punishment: Centre’s overhaul of criminal laws\n👉🏼 Key provisions and processes proposed in Bill to replace CrPC\n👉🏼 Expert Explains: What does the proposed legislation to overhaul criminal justice system mean?\n👉🏼 From holding trials on video to community service as punishment: Centre’s overhaul of criminal laws"
        )
    )
