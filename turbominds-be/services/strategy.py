from uuid import uuid4
from schemas.strategy import ResGenerateStrategy

def generate_strategy(data):
    strategy_id = uuid4()
    print(data)
    # thread = Thread(target=kickoff_crew, args=(brief_id, content))
    # thread.start()
    return ResGenerateStrategy(strategy_id = strategy_id)

def get_strategy_status(strategy_id):
    # print("getting research status...", research_id)
    sample_response = {
        "strategy_id": strategy_id,
        "status": "COMPLETED",
        "results": {
            "final_strategy": "<h1>Analysis of the Brief Provided</h1>\n    \n    <h2>Requirement:</h2>\n    <p>Nothing specified about the requirement.</p>\n    \n    <h2>Campaign Overview:</h2>\n    <p>Lush locks is a socks brand for old generation who have very strong hairs.</p>\n    \n    <h2>Campaign Goals:</h2>\n    <p>Nothing specified about the campaign goals.</p>\n    \n    <h2>Target Audience:</h2>\n    <p>Old generation individuals with strong hair.</p>\n    \n    <h2>KPIs:</h2>\n    <p>Nothing specified about the Key Performance Indicators.</p>\n    \n    <h2>Budget:</h2>\n    <p>Nothing specified about the budget.</p>\n    \n    <h2>Timeline:</h2>\n    <p>Nothing specified about the timeline.</p>```"
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