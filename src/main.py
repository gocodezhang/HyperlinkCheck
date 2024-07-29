from fastapi import FastAPI
from pydantic import BaseModel
from verification import HyperlinkVerifier
from typing import Union


class PassageContext(BaseModel):
    linked_str: str  # str that hyperlink is linked to
    sentence: Union[str, None] = None  # the sentence contains hyperlink
    # the nearest three sentences around the hyperlink
    three_sentences: Union[str, None] = None


class LinkItem(BaseModel):
    hyperlink: str
    passage_context: PassageContext


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
        print(validation_code)
        if (validation_code > 2):
            results.append({'validation_code': validation_code})
        else:
            result = verifier.validate(item.passage_context.model_dump())
            result['validation_code'] = validation_code
            results.append(result)
    return results
