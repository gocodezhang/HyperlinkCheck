from pathlib import Path
from transformers import pipeline
import requests
import os
import logging

logger = logging.getLogger('extractor')
env = os.environ.get('ENV_VAR', 'localhost')
curr_dir = Path(__file__).parent

KEY_WORD_API_URL = "https://api-inference.huggingface.co/models/ml6team/keyphrase-extraction-kbir-inspec"


def token_classification_infer_api(str: str):
    logger.info('token_classification_infer_api()')
    headers = {"Authorization": "Bearer " + os.environ.get('HF_API_KEY')}
    data = {"inputs": str, "parameters": {
        "aggregation_strategy": "none"}, "options": {"wait_for_model": True}}
    response = requests.post(KEY_WORD_API_URL, headers=headers, json=data)
    return response.json()


token_classification = pipeline(
    "token-classification", model=curr_dir / '../../models/keyphrase-extraction-kbir-inspec') if env == "localhost" else token_classification_infer_api


def keywords_extractor(str: str):
    logger.info('keywords_extractor(): %s', str)
    # apply token classification to identify key words
    raw_output = token_classification(str)
    logger.info('keywords_extractor() llm_output: %s', raw_output)
    length = len(raw_output)

    # convert the model output into actual key words
    tags = {'words': [], 'scores': []}
    visited = set()
    index = 0
    while (index < length):
        curr_output = raw_output[index]
        # skip curr index if it is not B-KEY
        if (curr_output['entity'] != 'B-KEY'):
            index += 1
            continue

        # locate start/end for curr keyword
        start = curr_output['start']
        end = curr_output['end']
        total_word_length = (end - start)
        score = curr_output['score'] * (end - start)
        # move until we find the next B-KEY
        while (index + 1 < length and raw_output[index + 1]['entity'] != 'B-KEY'):
            next_output = raw_output[index + 1]
            end = next_output['end']
            total_word_length += end - next_output['start']
            score += next_output['score'] * (end - next_output['start'])
            index += 1

        word = str[start: end]
        if (word not in visited):
            visited.add(word)
            tags['words'].append(word)
            tags['scores'].append(score / total_word_length)

        index += 1

    return tags
