from typing import List, Optional
from pydantic import BaseModel
from api.granite import Granite


class Generator(BaseModel):
    station_id: Optional[str]=None
    language: Optional[str]=None
    date_1: Optional[str]=None
    date_2: Optional[str]=None
    date_3: Optional[str]=None
    potability_1: Optional[str]=None
    potability_2: Optional[str]=None
    potability_3: Optional[str]=None



   
    def generate_rapport_introduction(self) -> str:
        granite = Granite()
        # station_meta = get_station_info(station_id: self.station_id)
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
         - Water station meta : {}
        - Water station potability evolution : {self.date_1} - {self.potability_1}, {self.date_2} - {self.potability_2}, {self.date_3} - {self.potability_3}
        The output language should be {self.language} and the tone should be formal.
        The introduction should be between 300 and 500 words.
        Use Latex language
        """
        return granite.ask(prompt)
    
    def generation_rapport_prediction(self) -> str:
        granite = Granite()
        # station_meta = get_station_info(station_id: self.station_id)
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
         - Water station meta : {}
        - Water station potability evolution : {self.date_1} - {self.potability_1}, {self.date_2} - {self.potability_2}, {self.date_3} - {self.potability_3}
        The output language should be {self.language} and the tone should be formal.
        The introduction should be between 300 and 500 words.
        Use Latex 
        """
        return granite.ask(prompt)
    
    
    def generate_rapport_conclusion(self) -> str:
        granite = Granite()
        # station_meta = get_station_info(station_id: self.station_id)
        prompt = f"""
        Write a well-structured conclusion for a technical report on predicting the potability of
        water in monitoring stations based on monthly chemical records. The conclusion should
        summarize key findings, highlight the study's significance, and suggest future directions.
        The section should include:
        - Summary of findings: Recap the maininsights from the report, including the 
        effectiveness of the prediction models and the key trends observed in water quality.
        - Significance of the study: Explain the pratical implications of predicting water
        potability, such as improving public health measures and optimizing water resource management.
        - Water station meta : {}
        - Water station potability evolution : {self.date_1} - {self.potability_1}, {self.date_2} - {self.potability_2}, {self.date_3} - {self.potability_3} 
        The output language should be {self.language} and the tone should be formal.
        The introduction should be between 300 and 500 words.
        Use Latex language
        """
        return granite.ask(prompt)
    
    def generate_rapport(self) -> str:
        sle
        introduction = self.generate_rapport_introduction()
        prediction = self.generation_rapport_prediction()
        conclusion = self.generate_rapport_conclusion()
        rapport = introduction + prediction + conclusion
        return rapport