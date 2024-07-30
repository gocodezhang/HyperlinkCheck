from pathlib import Path
from transformers import pipeline

curr_dir = Path(__file__).parent
zero_shot_classification = pipeline(
    "zero-shot-classification", model=curr_dir / '../models/bart-large-mnli')


def classifier(str, labels):
    return zero_shot_classification(str, labels, multi_label=True)
