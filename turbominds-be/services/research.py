from uuid import uuid4
from schemas.research import ResGenerateResearch

def generate_research(data):
    research_id = uuid4()
    print(data)
    # thread = Thread(target=kickoff_crew, args=(brief_id, content))
    # thread.start()
    return ResGenerateResearch(research_id = research_id)

def get_research_status(research_id):
    # print("getting research status...", research_id)
    sample_response = {
        "research_id": research_id,
        "status": "COMPLETED",
        "results": {
            "final_research": "<h1>Analysis of the Brief Provided</h1>\n    \n    <h2>Requirement:</h2>\n    <p>Nothing specified about the requirement.</p>\n    \n    <h2>Campaign Overview:</h2>\n    <p>Lush locks is a socks brand for old generation who have very strong hairs.</p>\n    \n    <h2>Campaign Goals:</h2>\n    <p>Nothing specified about the campaign goals.</p>\n    \n    <h2>Target Audience:</h2>\n    <p>Old generation individuals with strong hair.</p>\n    \n    <h2>KPIs:</h2>\n    <p>Nothing specified about the Key Performance Indicators.</p>\n    \n    <h2>Budget:</h2>\n    <p>Nothing specified about the budget.</p>\n    \n    <h2>Timeline:</h2>\n    <p>Nothing specified about the timeline.</p>```",
            "sources": [
                {
                "id": "a89ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c85",
                "description": "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ...",
                "title": "Google Search",
                "url": "https://www.google.com/"
                },
                {
                "id": "389ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c84",
                "description": "Meta ranks among the largest American information technology companies, alongside other Big Five corporations Alphabet (Google), Amazon, Apple, and Microsoft.",
                "title": "Facebook Meta",
                "url": "https://www.meta.com/"
                },
                {
                "id": "a89ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c85",
                "description": "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ...",
                "title": "Google Search",
                "url": "https://www.google.com/"
                },
                {
                "id": "389ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c84",
                "description": "Meta ranks among the largest American information technology companies, alongside other Big Five corporations Alphabet (Google), Amazon, Apple, and Microsoft.",
                "title": "Facebook Meta",
                "url": "https://www.meta.com/"
                },
                {
                "id": "a89ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c85",
                "description": "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ...",
                "title": "Google Search",
                "url": "https://www.google.com/"
                },
                {
                "id": "389ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c84",
                "description": "Meta ranks among the largest American information technology companies, alongside other Big Five corporations Alphabet (Google), Amazon, Apple, and Microsoft.",
                "title": "Facebook Meta",
                "url": "https://www.meta.com/"
                },
                {
                "id": "a89ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c85",
                "description": "Search the world's information, including webpages, images, videos and more. Google has many special features to help you find exactly what you're looking ...",
                "title": "Google Search",
                "url": "https://www.google.com/"
                },
                {
                "id": "389ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c84",
                "description": "Meta ranks among the largest American information technology companies, alongside other Big Five corporations Alphabet (Google), Amazon, Apple, and Microsoft.",
                "title": "Facebook Meta",
                "url": "https://www.meta.com/"
                }
            ]
        },
        "events": [
            {
            "timestamp": "2024-07-18T16:57:20.655339",
            "data": "Task Started"
            },
            {
            "timestamp": "2024-07-18T16:57:24.867423",
            "data": "```html\n<!DOCTYPE html>\n<html>\n<head>\n    <title>Brief Analysis</title>\n</head>\n<body>\n    <h1>Analysis of the Brief Provided</h1>\n    \n    <h2>Requirement:</h2>\n    <p>Nothing specified about the requirement.</p>\n    \n    <h2>Campaign Overview:</h2>\n    <p>Lush locks is a socks brand for old generation who have very strong hairs.</p>\n    \n    <h2>Campaign Goals:</h2>\n    <p>Nothing specified about the campaign goals.</p>\n    \n    <h2>Target Audience:</h2>\n    <p>Old generation individuals with strong hair.</p>\n    \n    <h2>KPIs:</h2>\n    <p>Nothing specified about the Key Performance Indicators.</p>\n    \n    <h2>Budget:</h2>\n    <p>Nothing specified about the budget.</p>\n    \n    <h2>Timeline:</h2>\n    <p>Nothing specified about the timeline.</p>\n</body>\n</html>\n```"
            },
            {
            "timestamp": "2024-07-18T16:57:34.090442",
            "data": "{\n  \"questions\": [\n    {\n      \"id\": \"a89ebbf1-7d1b-46a7-9f8b-8f6b6f5b4c85\",\n      \"question\": \"What are the specific requirements for the campaign?\",\n      \"topic\": \"Requirement\"\n    },\n    {\n      \"id\": \"9daffb5f-0d81-49d0-ad51-9c6e8f4e2dfa\",\n      \"question\": \"What are the campaign goals that need to be achieved?\",\n      \"topic\": \"Campaign Goals\"\n    },\n    {\n      \"id\": \"c37d8b9e-0a4d-4c98-8d9f-5b6f8d1f4a52\",\n      \"question\": \"What are the Key Performance Indicators (KPIs) to measure the success of the campaign?\",\n      \"topic\": \"KPIs\"\n    },\n    {\n      \"id\": \"3c4c9f45-28d4-4e5b-9025-63f7c29b1408\",\n      \"question\": \"What is the allocated budget for the campaign?\",\n      \"topic\": \"Budget\"\n    },\n    {\n      \"id\": \"8d3ef0e1-9f64-4f63-8bdc-6f12e943c4e4\",\n      \"question\": \"What is the timeline for the campaign execution?\",\n      \"topic\": \"Timeline\"\n    }\n  ]\n}"
            },
            {
            "timestamp": "2024-07-18T16:57:34.090880",
            "data": "Task Completed"
            },
            {
            "timestamp": "2024-07-18T16:57:34.090930",
            "data": "Crew complete"
            }
        ]
        }
            
    return sample_response