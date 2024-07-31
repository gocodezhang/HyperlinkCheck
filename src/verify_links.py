from typing import TypedDict, Optional
from verification import HyperlinkVerifier
import logging

verifier = HyperlinkVerifier()
logger = logging.getLogger('handler')
logging.basicConfig(level=logging.INFO)


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
    links_to_verify = event['body']
    logger.info('handler(): %s', links_to_verify)
    results = []
    for item in links_to_verify:
        validation_code = verifier.read_url(item['hyperlink'])
        if (validation_code > 2):
            results.append({'validation_code': validation_code})
        else:
            result = verifier.validate(item['passage_context'])
            result['validation_code'] = validation_code
            results.append(result)
    return results
