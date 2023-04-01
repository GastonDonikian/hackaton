import os
import openai
openai.organization = "org-XNTeefC4qnnZBi1ttm8FA756"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()