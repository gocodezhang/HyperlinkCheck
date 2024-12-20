mock_simple_data = [
    {"passage_context": {"linked_str": "wallet"},
     "hyperlink": "https://www.cnn.com/cnn-underscored/fashion/the-best-mens-wallets"
     },
    {"passage_context": {"linked_str": "Boeing"},
     "hyperlink": "https://www.cnbc.com/quotes/BA"
     },
    {"passage_context": {"linked_str": "money-losing and delayed modification"},
     "hyperlink": "https://www.cnbc.com/2022/04/27/boeing-lost-billion-dollars-on-trump-air-force-one-plane-deal.html"
     },
    {"passage_context": {"linked_str": "Joe Biden’s"},
     "hyperlink": "https://www.cnbc.com/joe-biden/"
     },
    {"passage_context": {"linked_str": "Biscuit Basin", "sentence": "The Biscuit Basin area of Yellowstone National Park in Wyoming is closed following a hydrothermal explosion Tuesday morning, park officials said in a news release and post on X."},
     "hyperlink": "https://yellowstonenationalpark.com/biscuitbasin.htm"
     },
    {"passage_context": {"linked_str": "Alphabet",
                         "sentence": "Google parent company Alphabet reported second-quarter results after the bell Tuesday that were in-line with analyst estimates on revenue and earnings, but missed on YouTube advertising revenue."
                         },
     "hyperlink": "https://www.cnbc.com/quotes/GOOG/"
     },
    {"passage_context": {"linked_str": "largest video platform in the world", "sentence": "Though it’s the largest video platform in the world, it faces increased competition from social video sites like TikTok."},
     "hyperlink": "https://www.cnbc.com/2024/06/26/youtube-streaming-dominance-media-strategy.html"
     },
    {"passage_context": {"linked_str": "opened", "sentence": "During the second quarter, Alphabet saw a number of expansion updates, including for Waymo, which opened its service to all San Francisco users."},
     "hyperlink": "https://www.cnbc.com/2024/06/25/waymo-opens-robotaxi-service-to-all-san-francisco-users.html"
     },
    {"passage_context": {"linked_str": "he would end his teetering re-election campaign"},
     "hyperlink": "https://www.cnbc.com/"
     },
    # --- new added ---
    {"passage_context": {"linked_str": "docker container run"},
     "hyperlink": "https://docs.docker.com/reference/cli/docker/container/run/"
     },
    {"passage_context": {"linked_str": "tennis"},
     "hyperlink": "https://www.youtube.com/watch?v=-MpDhmfvH2Q"
     },
    {"passage_context": {"linked_str": "announced a “possible” cyberattack on its systems", "sentence": "Several days after the Port of Seattle announced a “possible” cyberattack on its systems, Seattle-Tacoma Airport is still largely offline, causing chaos among travelers and acting as a standing warning against taking cybersecurity lightly"},
     "hyperlink": "https://techcrunch.com/2024/08/25/the-port-of-seattle-and-sea-tac-airport-say-theyve-been-hit-by-possible-cyberattack/"
     },
    {"passage_context": {"linked_str": "Nvidia"},
     "hyperlink": "https://www.cnbc.com/quotes/NVDA/"
     },
    {"passage_context": {"linked_str": "filed", "sentence": "X, formerly known as Twitter, originally filed the suit in November after Media Matters published a report showing that hateful content on the platform appeared next to online ads from companies like Apple, IBM and Disney."},
     "hyperlink": "https://www.cnbc.com/2023/11/21/x-sues-media-matters-over-report-about-ads-appearing-next-to-nazi-posts.html"
     },
    {"passage_context": {"linked_str": "first interview", "sentence": "Vice President Kamala Harris was pressed about her policy evolutions Thursday in her first interview since she became the Democratic Party’s presidential nominee, sitting alongside her running mate, Tim Walz."},
     "hyperlink": "https://www.nbcnews.com/politics/2024-election/kamala-harris-pledges-republican-cabinet-member-rcna168879"
     },
    {"passage_context": {"linked_str": "Ray", "sentence": "We're commercializing a popular open source project called Ray - which is an “operating system” for heterogeneous distributed computing as well as an ecosystem of libraries for scalable machine learning, including large language models (LLMs) and GenAI."},
     "hyperlink": "https://www.ray.io/"
     },
    {"passage_context": {"linked_str": "referred to", "sentence": "In a speech after a school shooting in 2018, Walz, the governor of Minnesota, referred to the weapon that was used as being similar to the one he carried “in war,” even though he had never seen combat."},
     "hyperlink": "https://www.nbcnews.com/politics/2024-election/tim-walz-misspoke-discussed-using-weapons-war-campaign-says-rcna166038"
     },
    {"passage_context": {"linked_str": "Idempotency"},
     "hyperlink": "https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html"
     },
    {"passage_context": {"linked_str": "AWS Command Line Interface"},
     "hyperlink": "https://aws.amazon.com/cli/"
     },
    # below work not well
    {"passage_context": {"linked_str": "", "sentence": "Starting in September, 2023, fixed defects can be found on this site. Additional defect information is available at https://issues.salesforce.com/#f[sfcategoryfull]=Tableau."},
     "hyperlink": "https://issues.salesforce.com/?_ga=2.77771165.863332541.1725138942-2001046278.1725138942#f[sfcategoryfull]=Tableau"
     },
    # based on anyscale docs
    {"passage_context": {"linked_str": "Anyscale", "sentence": "This is what Anyscale aims to accomplish."},
     "hyperlink": "https://techcrunch.com/2019/12/17/anyscale-ray-project-distributed-computing-a16z/"
     },
    {"passage_context": {"linked_str": "here", "sentence": "We recently announced our Series C and general availability! See more here."},
     "hyperlink": "https://www.anyscale.com/blog/the-future-is-distributed"
     },
    {"passage_context": {"linked_str": "Anyscale Teams Up With NVIDIA to Scale Generative AI Models Into Production"},
     "hyperlink": "https://finance.yahoo.com/news/anyscale-teams-nvidia-scale-generative-220000760.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAJQdrdT_yu3Qi-89Jqtd7CyMcsx3C50yCWve_nEhj-Kw36fH05tuDdZQhPvmmZxYySxep3SNZi_1zD00suR9vzlBiwLkF9V6sud4s3wlnA8SYfuzFDOGlqhHXFwZEWFFb1Vc1v9g75LzUgna7lAd6mkvBCgERbKMmtEUjzSg4Ev1"
     },
    {"passage_context": {"linked_str": "Series A", "sentence": "$20M Series A led by Andreessen Horowitz (a16z), with participation from New Enterprise Associates (NEA), Intel Capital, Ant Financial, and more."},
     "hyperlink": "https://www.crunchbase.com/funding_round/anyscale-series-a--fc48bb05#section-overview"
     },
    {"passage_context": {"linked_str": "Scaling AI and Python Workloads Effortlessly with Ray"},
     "hyperlink": "https://drive.google.com/file/d/1-Doyz0x8i6kaPx-ZhL7pLjuidUkqxety/view"
     },
    {"hyperlink": "https://www.wsj.com/articles/ai-startup-anyscale-adds-99-million-to-andressen-horowitz-led-funding-round-11661254200",
     "passage_context":
     {"linked_str": "$99M",
      "sentence": "Additional $99M Led by a16z announced during Ray Summit 2022"}
     }
]

mock_broken_url = [
    {"passage_context": {"linked_str": "invalid url"},
     "hyperlink": "https://prod-reporting-center-api.labs.thry.com/"
     },
]

mock_complex_data = [
    {"context": "Navisite, part of Accenture, today announced the launch of its fourth annual Navisite’s Next Steminist Scholarship U.S. program. Designed to encourage young women to pursue careers in STEM (science, technology, engineering, and math), the program will award three $10,000 scholarships to eligible female candidates pursuing a degree in STEM. Applications are now being accepted through May 17, 2024.",
     "hyperlink_text": "At Navisite, part of Accenture, supporting women in their STEM education is not only important to us–it’s vital to building an inclusive and diverse tech workforce. Navisite’s Next Steminist scholarship program is designed to help close the gender gap in tech and encourage young women to pursue their passion in STEM. The program provides scholarships to eligible female candidates who are currently pursuing or plan to pursue a degree in STEM."
     },
    {"context": "Gain a detailed view of your customers and sales pipeline by automatically syncing your business contacts and estimates between Thryv and Copper",
     "hyperlink_text": "Integrating your Copper CRM with Business Center offers a seamless synergy that amplifies your business efficiency and effectiveness. By consolidating customer and lead data from both platforms, you gain a comprehensive view of your clients, streamlining communication and enhancing personalized interactions. This integration eliminates the need for manual data entry, reducing errors and saving valuable time, allowing your team to focus on cultivating meaningful relationships and driving revenue growth. Experience the power of unified CRM systems working in tandem to propel your business forward with unparalleled cohesion and productivity."
     }
]

test_docus_data = [
    {"hyperlink": "https://www.youtube.com/watch?v=r-NYSeAXCko",
     "passage_context": {"linked_str": "Day 1", "sentence": "Day 1 - Announcement of Anyscale Endpoints is at the beginning, and also includes our CEO Robert Nishihara interviewing John Schulman, co-creator of OpenAI, really fun to hear that conversation!"
                         }
     },
    {"hyperlink": "https://www.youtube.com/watch?v=CwIvsmuGqk4",
     "passage_context": {"linked_str": "Day 2", "sentence": "Day 2 - Includes folks from Uber, Niantic, and Adobe sharing how they are using Ray, and Robert interviewing Ben Horowitz of a16z, a crowd-favorite conversation."}},
    {"hyperlink": "https://www.globenewswire.com/news-release/2023/09/18/2744860/0/en/Anyscale-Launches-New-Service-Anyscale-Endpoints-10X-More-Cost-Effective-for-Most-Popular-Open-Source-LLMs.html",
     "passage_context": {"linked_str": "here",
                         "sentence": "Our press release was picked up here , and the NVIDIA blog post is helpful to understand how we are partnering with NVIDIA to supercharge LLM performance and efficiency to deliver cost savings."}},
    {"hyperlink": "https://blogs.nvidia.com/blog/2023/09/18/llm-anyscale-nvaie/",
     "passage_context":
     {"linked_str": "NVIDIA blog post",
      "sentence": "Our press release was picked up here, and the NVIDIA blog post is helpful to understand how we are partnering with NVIDIA to supercharge LLM performance and efficiency to deliver cost savings."}},
    {"hyperlink": "https://www.anyscale.com/blog/the-future-is-distributed",
     "passage_context":
     {"linked_str": "here",
      "sentence": "We recently announced our Series C and general availability! See more here ."}},
    {"hyperlink": "https://www.crunchbase.com/funding_round/anyscale-series-a--fc48bb05#section-overview",
     "passage_context":
     {"linked_str": "Series A",
      "sentence": "December 2019: $20M Series A led by Andreessen Horowitz (a16z), with participation from New Enterprise Associates (NEA), Intel Capital, Ant Financial, and more."}},
    {"hyperlink": "https://a16z.com/2019/12/17/anyscale/",
     "passage_context":
     {"linked_str": "Andreessen Horowitz",
      "sentence": "December 2019: $20M Series A led by Andreessen Horowitz (a16z), with participation from New Enterprise Associates (NEA), Intel Capital, Ant Financial, and more."}},
    {"hyperlink": "https://www.crunchbase.com/funding_round/anyscale-series-b--8bd426db",
     "passage_context":
     {"linked_str": "Series B",
      "sentence": "October 2020: $40M Series B led by NEA, with participation from a16z, Intel Capital, and Foundation Capital, and more."}},
    {"hyperlink": "https://www.forbes.com/sites/kenrickcai/2021/12/07/berkeley-research-lab-mints-second-billion-dollar-startup-anyscale/",
     "passage_context":
     {"linked_str": "Series C",
      "sentence": "December 2021: $100M Series C led by a16z and Addition, with participation from NEA, Intel Capital, and Foundation Capital."}},
    {"hyperlink": "https://www.wsj.com/articles/ai-startup-anyscale-adds-99-million-to-andressen-horowitz-led-funding-round-11661254200",
     "passage_context":
     {"linked_str": "$99M",
      "sentence": "Additional $99M Led by a16z announced during Ray Summit 2022"}},
    {"hyperlink": "https://www.anyscale.com/ray-summit-2022",
     "passage_context":
     {"linked_str": "Ray Summit 2022",
      "sentence": "Additional $99M Led by a16z announced during Ray Summit 2022 "}}]
