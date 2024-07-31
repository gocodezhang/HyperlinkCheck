from fastapi import FastAPI
from pydantic import BaseModel
from verification import HyperlinkVerifier
from typing import Union
from pathlib import Path
import nltk


class PassageContext(BaseModel):
    linked_str: str  # str that hyperlink is linked to
    sentence: Union[str, None] = None  # the sentence contains hyperlink
    # the nearest three sentences around the hyperlink
    three_sentences: Union[str, None] = None


class LinkItem(BaseModel):
    hyperlink: str
    passage_context: PassageContext


curr_dir = Path(__file__).parent
nltk_data_path = curr_dir / '../models/nltk_data'
if (nltk_data_path not in nltk.data.path):
    nltk.data.path.append(nltk_data_path)
verifier = HyperlinkVerifier()
app = FastAPI()


@app.get('/')
async def root():
    return 'Checker is running'


@app.post('/verify')
async def verifyLinks(items: list[LinkItem]):
    results = []
    for item in items:
        validation_code = verifier.read_url(item.hyperlink)
        if (validation_code > 2):
            results.append({'validation_code': validation_code})
        else:
            result = verifier.validate(item.passage_context.model_dump())
            result['validation_code'] = validation_code
            results.append(result)
    return results
