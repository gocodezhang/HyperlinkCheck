from typing import TypedDict, Optional
from src.verification import HyperlinkVerifier
from pathlib import Path
from pyvirtualdisplay import Display
import logging
import nltk

curr_dir = Path(__file__).parent
nltk_data_path = curr_dir / './models/nltk_data'
if (nltk_data_path not in nltk.data.path):
    nltk.data.path.append(nltk_data_path)
logger = logging.getLogger('handler')
logger.setLevel('INFO')


class PassageContext(TypedDict):
    linked_str: str  # str that hyperlink is linked to
    sentence: Optional[str]  # the sentence contains hyperlink
    # the nearest three sentences around the hyperlink
    three_sentences: Optional[str]


class Hyperlink(TypedDict):
    hyperlink: str
    passage_context: PassageContext


class APIGateWayEvent(TypedDict):
    body: list[Hyperlink]


def handler(event: APIGateWayEvent, context):
    links_to_verify = []  # event['body']
    print('testing')
    logger.info('handler(): %s', links_to_verify)
    verifier = HyperlinkVerifier()
    # results = []
    # try:
    #     for item in links_to_verify:
    #         validation_code = verifier.read_url(item['hyperlink'])
    #         if (validation_code > 2):
    #             results.append({'validation_code': validation_code})
    #         else:
    #             result = verifier.validate(item['passage_context'])
    #             result['validation_code'] = validation_code
    #             results.append(result)
    #     return {
    #         "statusCode": 200,
    #         "headers": {
    #             "Content-Type": "application/json"
    #         },
    #         "body": results
    #     }
    # except Exception as e:
    #     logger.error(e)
    return 'Hello'