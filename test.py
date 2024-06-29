from transformers import pipeline

classifier = pipeline("zero-shot-classification", model='../../huggingFace/models/bart-large-mnli')
keyWordExtractor = pipeline("token-classification", model='../../huggingFace/models/keyphrase-extraction-kbir-inspec')

sequence_to_classify = "Alteryx, Inc. is an American computer software company based in Irvine, California, with a development center in Broomfield, Colorado,and offices worldwide. The company's products are used for data science and analytics. The software is designed to make advanced analytics automation accessible to any data worker."
outputs = keyWordExtractor(sequence_to_classify)

tags = []

startIndex = 0
endIndex = 0
for output in outputs:
  if output['entity'] == 'B-KEY':
    if startIndex < endIndex:
      tags.append(sequence_to_classify[startIndex:endIndex])
    startIndex = output['start']
  
  if output['entity'] == 'I-KEY':
    endIndex = max(output['end'], endIndex)


print(tags)

print(classifier(sequence_to_classify, tags, multi_label = True))