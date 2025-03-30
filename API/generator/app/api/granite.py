from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials
import pandas as pd
import json

class Granite:
    def __init__(self):
        self.creds = Credentials(api_key='bMpVltkwpuYaiMO8xwJWmBAMtFuOL1QxFWpUf94YP-XX', url='https://us-south.ml.cloud.ibm.com')
        self.granite_model = ModelInference(model_id='ibm/granite-3-8b-instruct', credentials=self.creds, project_id='f8d63044-425a-4416-9355-df29fc58ac16', params={"max_new_tokens":600})

    def generate(self, prompt: str) -> str:
        response = self.granite_model.generate(prompt=prompt)
        return response