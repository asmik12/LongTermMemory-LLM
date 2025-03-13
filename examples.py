#Example questions:
#Information Extraction
information_extraction = [{
        "question": "What was the last project I asked you for help with?",
        "follow_up": [
            "Is this question referring to a personal, academic, or work-related project of the user?",
            "What are the questions the user has had about this project?",
            "What is the project name, and also the main challenge faced in the project?",
            "What are solutions or suggestions that were provided previously for the user’s project?",
        ]
    },
    {
        "question": "Can you summarize the key points from my discussion about text embeddings?",
        "follow_up": [
            "Did the user discuss text embeddings, including previous discussions focused on theoretical concepts, implementation details, or both?",
            "What are the specific libraries or models that were considered for text embeddings?",
            "Is the user  usually interested in a high-level summary sufficient, or a more detailed recall?",
            "Is this discussion was related to the Is the user working on a recommendation system project?",
            "What are unresolved questions or next steps mentioned by the user in previous discussions about text embeddings?"
        ]
    },
    {
        "question": "What was the name of the panel I wanted to conduct at LA Hacks?",
        "follow_up": [
            "What are names of panels the user wants to conduct  at LA Hacks?",
            "What details did the user discuss about the topics and speakers that were considered at LA Hacks?",
            "Was the panel name was finalized or still tentative?",
            "What kinds of panels has the user held before at LA Hacks?",
            "Would it be helpful to include any logistical challenges or updates discussed?",
            "Does this request also ask for suggestions to move forward with the panel in the future?"
        ]
    },
    {
        "question": "Can you remind me what issue I encountered while using GridSearchCV?",
        "follow_up": [
            "What was the exact error message or the general issue encountered while using GridSearchCV?",
            "Was this issue related to a specific dataset or model being tuned while using GridSearchCV?",
            "What were any debugging steps or solutions that were discussed while using GridSearchCV?",
            "Did this issue about GridSearchCV occurr during a coursework project or personal research project?"
        ]
    },
    {
        "question": "What are the datasets I have worked with in my past projects?",
        "follow_up": [
            "Does the user need a full list, or only the most recent datasets used?",
            "What are datasets from the user's personal projects, academic work, or internships?",
            "How the datasets were preprocessed or used?",
            "What were some datasets that were considered but ultimately not used?"
        ]
    }]

# Multi-Session Reasoning
multi_session_reasoning = [
        {
            "question": "How has my research focus evolved over time?",
            "follow_up": [
                "Has the user previously discussed changes in their research focus?",
                "Are there multiple research projects, internships, or coursework records indicating an evolution in focus?",
                "Has the user mentioned their initial research interests and compared them to their current ones?",
                "Are there patterns in the technologies or methodologies the user has worked with over time?",
                "Has the user referenced how their research interests align with industry trends?"
            ]
        },
        {
            "question": "Can you compare my approach to optimizing recommendation systems from my past and current projects?",
            "follow_up": [
                "Has the user worked on multiple recommendation system projects?",
                "Has the user described different algorithmic approaches or implementation details in past discussions about optimizing recommendation systems?",
                "Are there mentions of key improvements, challenges, or external influences (e.g., dataset changes, business goals)?",
                "Has the user referenced performance metrics for previous recommendation models?",
                "Has the user shared lessons learned or trade-offs they had to make for optimizing recommendation systems?"
            ]
        },
        {
            "question": "What strategies have I used in the past to debug machine learning models?",
            "follow_up": [
                "What has the user discussed about debugging machine learning models in previous conversations?",
                "What are the references to specific debugging techniques used in different projects?",
                "Has the user faced and documented common issues like overfitting, data leakage, or training instability?",
                "Has the user evaluated which debugging methods were most effective?",
                "Are there mentions of how the user's debugging workflow has improved over time?"
            ]
        },
        {
            "question": "How have my leadership responsibilities changed since I joined LA Hacks?",
            "follow_up": [
                "Has the user held multiple leadership roles within LA Hacks?",
                "Are there discussions with timestamps indicating shifts in responsibilities within LA Hacks?",
                "Has the user referenced specific initiatives or projects they led within LA Hacks?",
                "Are there mentions of skills developed or challenges overcome in their leadership role?",
                "Has the user discussed their contributions and impact on LA Hacks?"
            ]
        },
        {
            "question": "Can you summarize the different approaches I’ve considered for CAPTCHA security?",
            "follow_up": [
                "Has the user explored multiple approaches to CAPTCHA security?",
                "Has the user compared traditional CAPTCHAs with AI-based methods?",
                "Are there references to attack vectors and security weaknesses the user has analyzed?",
                "Has the user provided a timeline of when they considered each approach for CAPTCHA security?",
                "Did the user express interest in evaluating which approach is most effective?"
            ]
        }
    ]

# Knowledge Update (KU)
knowledge_update = [{
            "question": "When did I start working on my current research project?",
            "follow_up": [
                "Has the user previously mentioned a specific research project they are working on?",
                "Is there a timestamp associated with the start of this project in past interactions?",
                "Has the user provided any updates on this project that might indicate a timeline?",
                "Did the user mention collaborators or institutions that could help identify the project's timeframe?",
            ]
        },
        {
            "question": "How long have I been using Word2Vec embeddings in my projects?",
            "follow_up": [
                "Has the user previously mentioned using Word2Vec in any project?",
                "Is there a first mention of Word2Vec in past interactions that could indicate the start date?",
                "Has the user discussed switching from another embedding technique to Word2Vec?",
                "Are there multiple instances where the user referenced using Word2Vec, and do they indicate a timeframe?"
            ]
        },
        {
            "question": "When was the last time I updated my resume with new technical skills?",
            "follow_up": [
                "Has the user mentioned making updates to their resume before?",
                "Is there a timestamp associated with the last resume-related conversation?",
                "Did the user recently acquire or mention learning a new technical skill that might have prompted an update?",
                "Has the user shared a resume draft or requested feedback on one?"
            ]
        },
        {
            "question": "How has my involvement in LA Hacks changed over time?",
            "follow_up": [
                "Has the user mentioned multiple roles or responsibilities related to LA Hacks?",
                "Are there timestamps associated with different mentions of LA Hacks involvement?",
                "Did the user indicate any leadership or role changes within LA Hacks?",
                "What are some details about specific events or initiatives the user contributed to at LA Hacks in previous years?",
                "Has the user discussed their future plans or ongoing commitments to LA Hacks?"
            ]
        },
        {
            "question": "What was the last machine learning model I trained, and when did I do it?",
            "follow_up": [
                "Has the user previously mentioned training a machine learning model?",
                "Is there a record of the most recent model training session in past interactions?",
                "Did the user provide details on datasets, frameworks, or performance metrics for a recent model?",
                "Has the user mentioned transitioning to a different model type or approach recently?"
            ]
        }]

# Temporal reasoning
temporal_reasoning = [{
        "question": "When did I last work on the recommendation system project?",
        "follow_up": [
            "Did the user mention they are working on a recommendation system project?"
        ]
    },
    {
        "question": "What progress did I make on the Math Success Program in the past month?",
        "follow_up": [
            "Did the user mention they were working at the Math Success Program?",
            "What work did the user do at the Math Success Program in the past month?"
        ]
    },
    {
        "question": "Can you remind me of the details from our discussion about the panel at LA Hacks last year?",
        "follow_up": [
            "Did the user mention they were working on a panel at LA Hacks last year?"
        ]
    },
    {
        "question": "What were the main issues I encountered while using GridSearchCV in the past few weeks?",
        "follow_up": [
          "Did the user mention they were working on projects involving GridSearchCV in the past few weeks?"        ]
    },
    {
        "question": "When did I mention considering a dataset for my project but ultimately deciding against it?",
        "follow_up": [
           "Did the user mention considering a dataset for any project and ultimately deciding against it?"        ]
    }]
