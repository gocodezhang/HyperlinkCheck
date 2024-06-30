
from mock_data import mock_simple_data, mock_complex_data
from nlp.keywords_extractor import keywords_extractor
from nlp.classifier import classifier

# for data in mock_simple_data:
#   label = [data['context']]
#   output = classifier(data['hyperlink_text'], label, multi_label=True)
#   print(label)
#   print(output['scores'])

for data in mock_complex_data:
  context = data['context']
  extract_output = keywords_extractor(context)
  
  results = classifier(data['hyperlink_text'], extract_output['words'])
  print(results)