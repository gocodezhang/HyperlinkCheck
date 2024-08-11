mock_simple_data = [
    {'passage_context': {'linked_str': 'wallet'},
     'hyperlink': "https://www.cnn.com/cnn-underscored/fashion/the-best-mens-wallets"
     },
    # {'passage_context': {'linked_str': 'Boeing'},
    #  'hyperlink': 'https://www.cnbc.com/quotes/BA'
    #  },
    # {'passage_context': {'linked_str': 'money-losing and delayed modification'},
    #  'hyperlink': 'https://www.cnbc.com/2022/04/27/boeing-lost-billion-dollars-on-trump-air-force-one-plane-deal.html'
    #  },
    # {'passage_context': {'linked_str': 'Joe Biden’s'},
    #  'hyperlink': 'https://www.cnbc.com/joe-biden/'
    #  },
    # {'passage_context': {'linked_str': 'Biscuit Basin', 'sentence': 'The Biscuit Basin area of Yellowstone National Park in Wyoming is closed following a hydrothermal explosion Tuesday morning, park officials said in a news release and post on X.'},
    #  'hyperlink': 'https://yellowstonenationalpark.com/biscuitbasin.htm'
    #  },
    # {'passage_context': {'linked_str': 'Alphabet',
    #                      'sentence': 'Google parent company Alphabet reported second-quarter results after the bell Tuesday that were in-line with analyst estimates on revenue and earnings, but missed on YouTube advertising revenue.'
    #                      },
    #  'hyperlink': 'https://www.cnbc.com/quotes/GOOG/'
    #  },
    # {'passage_context': {'linked_str': 'largest video platform in the world', 'sentence': 'Though it’s the largest video platform in the world, it faces increased competition from social video sites like TikTok.'},
    #  'hyperlink': 'https://www.cnbc.com/2024/06/26/youtube-streaming-dominance-media-strategy.html'
    #  },
    # {'passage_context': {'linked_str': 'opened', 'sentence': 'During the second quarter, Alphabet saw a number of expansion updates, including for Waymo, which opened its service to all San Francisco users.'},
    #  'hyperlink': 'https://www.cnbc.com/2024/06/25/waymo-opens-robotaxi-service-to-all-san-francisco-users.html'
    #  },
    # {'passage_context': {'linked_str': 'he would end his teetering re-election campaign'},
    #  'hyperlink': 'https://www.cnbc.com/'
    #  },
]

mock_broken_url = [
    {'passage_context': {'linked_str': 'invalid url'},
     'hyperlink': 'https://prod-reporting-center-api.labs.thry.com/'
     },
]

mock_complex_data = [
    {'context': "Navisite, part of Accenture, today announced the launch of its fourth annual Navisite’s Next Steminist Scholarship U.S. program. Designed to encourage young women to pursue careers in STEM (science, technology, engineering, and math), the program will award three $10,000 scholarships to eligible female candidates pursuing a degree in STEM. Applications are now being accepted through May 17, 2024.",
     'hyperlink_text': "At Navisite, part of Accenture, supporting women in their STEM education is not only important to us–it’s vital to building an inclusive and diverse tech workforce. Navisite’s Next Steminist scholarship program is designed to help close the gender gap in tech and encourage young women to pursue their passion in STEM. The program provides scholarships to eligible female candidates who are currently pursuing or plan to pursue a degree in STEM."
     },
    {'context': "Gain a detailed view of your customers and sales pipeline by automatically syncing your business contacts and estimates between Thryv and Copper",
     'hyperlink_text': "Integrating your Copper CRM with Business Center offers a seamless synergy that amplifies your business efficiency and effectiveness. By consolidating customer and lead data from both platforms, you gain a comprehensive view of your clients, streamlining communication and enhancing personalized interactions. This integration eliminates the need for manual data entry, reducing errors and saving valuable time, allowing your team to focus on cultivating meaningful relationships and driving revenue growth. Experience the power of unified CRM systems working in tandem to propel your business forward with unparalleled cohesion and productivity."
     }
]