from typing import List, Optional
from pydantic import BaseModel
from api.granite import Granite
from api.database import MeasurementsDb, StationDb
import requests


class Generator(BaseModel):
    station_id: Optional[str]=None
    language: Optional[str]="English"
    date_1: Optional[str]=None
    date_2: Optional[str]=None
    date_3: Optional[str]=None
    potability_1: Optional[str]=None
    potability_2: Optional[str]=None
    potability_3: Optional[str]=None

    
    def prepare_station_meta(self):
        latest_data = MeasurementsDb().measurements_collection.find({"station_id":self.station_id},{"sample_date":1, "Potability": 1, "_id":0}).sort("sample_date", -1).limit(3) 
        for doc in latest_data:
            if self.date_1 is None:
                self.date_1 = doc["sample_date"]
                self.potability_1 = doc["Potability"]
            elif self.date_2 is None:
                self.date_2 = doc["sample_date"]
                self.potability_2 = doc["Potability"]
            elif self.date_3 is None:
                self.date_3 = doc["sample_date"]
                self.potability_3 = doc["Potability"]

        print(f"Dates: {self.date_1}, {self.date_2}, {self.date_3}")
        print(f"Potability: {self.potability_1}, {self.potability_2}, {self.potability_3}")
        return self.date_1, self.date_2, self.date_3, self.potability_1, self.potability_2, self.potability_3


    def generate_rapport_introduction(self) -> str:
        granite = Granite()
        prompt = f"""
        Write a well-structured and formal introduction for a technical report on predicting the
        potability of a water stations based on monthly records of chemical elements in the water,
        such as pH, turbidity, nitrates, heavy metals, etc.
        The introduction should include the following elements:
        - Context and importance: Explain why monitoring water quality is crucial for public
        health and the environment.
        - Problem statement: Present the challenges related to evaluating water potability and
        the need for reliable predicton methods.
        - Objective of the report: Describe how analyzing monthly records and using predictive
        models can help anticipate the potability of water stations.
         - Water station meta : {self.station_id}
        - Water station potability evolution : {self.date_1} - {self.potability_1}, {self.date_2} - {self.potability_2}, {self.date_3} - {self.potability_3}
        The output language should be {self.language} and the tone should be formal.
        The introduction should be between 300 and 500 words.
        Use Latex language
        """
        return granite.generate(prompt)
    
    def generate_rapport_prediction(self) -> str:
        granite = Granite()
        prompt = f"""
        Write a detailed section for a technical report on predicting the potability of water in
        monitoring stations. This section should explain the results obtained, and their interpretation.
        The section should include the following elements:
        - Introduction to prediction: Explain the importance of predicting water potability and
        how it helps in water resource management.
        - Methodology: Describe the predictive models applied (statistical, machine
        learning, deep learning,etc), the tested algorithms (eg., regression, decision trees,
          neural networks), and the input variables (pH, turbidity, nitrates, etc).
        - Prediction results: Provide an analysis of the model's performance using metrics such as
        accuracy, precision, recall, and F1-score. Include visualizations (graphs, tables) to illustrate the results.
         - Water station id : {self.station_id}
        - Water station potability evolution : {self.date_1} - {self.potability_1}, {self.date_2} - {self.potability_2}, {self.date_3} - {self.potability_3}
        The output language should be {self.language} and the tone should be formal.
        The introduction should be between 300 and 500 words.
        Use Latex 
        """
        return granite.generate(prompt)
    
    
    def generate_rapport_conclusion(self) -> str:
        granite = Granite()
        prompt = f"""
        Write a well-structured conclusion for a technical report on predicting the potability of
        water in monitoring stations based on monthly chemical records. The conclusion should
        summarize key findings, highlight the study's significance, and suggest future directions.
        The section should include:
        - Summary of findings: Recap the maininsights from the report, including the 
        effectiveness of the prediction models and the key trends observed in water quality.
        - Significance of the study: Explain the pratical implications of predicting water
        potability, such as improving public health measures and optimizing water resource management.
        - Water station id : {self.station_id}
        - Water station potability evolution : {self.date_1} - {self.potability_1}, {self.date_2} - {self.potability_2}, {self.date_3} - {self.potability_3} 
        The output language should be {self.language} and the tone should be formal.
        The introduction should be between 300 and 500 words.
        Use Latex language
        """
        return granite.generate(prompt)
    
    def generate_rapport(self) -> str:
        self.prepare_station_meta()

        introduction_brut = self.generate_rapport_introduction()
        introduction = introduction_brut["results"][0]["generated_text"]
        prediction_brut = self.generate_rapport_prediction()
        prediction = prediction_brut["results"][0]["generated_text"]
        conclusion_brut = self.generate_rapport_conclusion()
        conclusion = conclusion_brut["results"][0]["generated_text"]
        rapport = introduction + prediction + conclusion
        return rapport
    
    def generate_station_details(self) -> str:
        url = f"http://nginx:8000/data/station/{self.station_id}"
        response = requests.get(url=url)
        if response.status_code == 200:
            granite = Granite()
            prompt = f"""
            Generate a detailed report on the water quality of a monitoring station based on the following information:

            ### Station Information:
            {response.text} 

            ### **Report Requirements:**  
            - Provide a **structured** analysis of the station’s water quality.  
            - Explain the **observed trends** based on the latest measurements.  
            - Discuss potential **environmental influences** affecting water quality.  
            - Offer **recommendations** for maintaining or improving water quality.  
            - Ensure the report is **300-500 words long** and written in a **professional and scientific tone**.
            The output language should be {self.language} and the tone should be formal.
            The introduction should be between 300 and 500 words.
            Use Latex language
            """
            details = granite.generate(prompt)
            return details["results"][0]["generated_text"]
        else:
            return "Erreur"