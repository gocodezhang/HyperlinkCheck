from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from pathlib import Path
from pyvirtualdisplay import Display
from src.verification import HyperlinkVerifier
import logging
import nltk
import os


class PassageContext(BaseModel):
    linked_str: str  # str that hyperlink is linked to
    sentence: Union[str, None] = None  # the sentence contains hyperlink
    # the nearest three sentences around the hyperlink
    three_sentences: Union[str, None] = None


class LinkItem(BaseModel):
    hyperlink: str
    passage_context: PassageContext


# ----------------- Set up -------------------------- #
env = os.environ.get('ENV_VAR', 'localhost')

# set up path for nltk
curr_dir = Path(__file__).parent
nltk_data_path = curr_dir / './models/nltk_data'
if (nltk_data_path not in nltk.data.path):
    nltk.data.path.append(nltk_data_path)

# set up virtual display and browser
if (env != 'localhost'):
    disp = Display(visible=False)
    disp.start()

verifier = HyperlinkVerifier()

# set logging level
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('FastAPI')

# --------------- Initialize API ---------------------- #
app = FastAPI()


@app.get('/')
async def root():
    return 'Checker is running'


@app.post('/verify')
async def verifyLinks(items: list[LinkItem]):
    logger.info('verifyLinks() %s', items)
    try:
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
    except Exception as e:
        logger.error(e)
        raise e

