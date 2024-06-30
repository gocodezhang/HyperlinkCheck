from transformers import pipeline

zero_shot_classification = pipeline("zero-shot-classification", model='../../huggingFace/models/bart-large-mnli')

def classifier(str, labels):
  return zero_shot_classification(str, labels, multi_label=True)