from pathlib import Path
from transformers import pipeline
import os
import requests
import logging

logger = logging.getLogger('classifier')
env = os.environ.get('ENV_VAR')
curr_dir = Path(__file__).parent
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"


def classifier_infer_api(str: str, labels: list[str], **kwargs):
    headers = {"Authorization": "Bearer " + os.environ.get('HF_API_KEY')}
    data = {"inputs": str, "parameters": {
        "candidate_labels": labels, "multi_label": kwargs.get('multi_label'), "options": {"wait_for_model": True}}}
    response = requests.post(API_URL, headers=headers, json=data)
    return response.json()


zero_shot_classification = pipeline(
    "zero-shot-classification", model=curr_dir / '../../models/bart-large-mnli') if env == "Production" else classifier_infer_api


def classifier(str: str, labels: list[str]):
    logger.info('classifier(): %s', {"str": str, "labels": labels})
    result = zero_shot_classification(str, labels, multi_label=True)

    # enforce scores to be in the same order as labels input
    length = len(labels)
    scores_ordered = [0] * length
    for i in range(length):
        index = result['labels'].index(labels[i])
        scores_ordered[i] = result['scores'][index]

    result['labels'] = labels
    result['scores'] = scores_ordered
    logger.info('classifier() result: %s', result)

    return result
