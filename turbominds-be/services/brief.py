# from sqlalchemy.orm import Session
from datetime import datetime
import json
from fastapi import HTTPException
from threading import Thread
from uuid import uuid4

from pydantic import UUID4
from services.crew import CompanyBriefingCrew
from utils.logging import logger
from utils.job_manager import Event, append_event, jobs, jobs_lock
from schemas.brief import AllQuestions, BriefResult, ResGenerateBrief, ResultQuestions

def get_brief_status(brief_id):
    # print("inside get brief status")
    # response = {
    #     "brief_id": brief_id,
    #     "events": [
    #         {"status": "created", "timestamp": "2022-01-01T12:00:00Z"},
    #         {"status": "updated", "timestamp": "2022-01-02T13:00:00Z"},
    #     ]
    # }
    with jobs_lock:
        brief = jobs.get(brief_id)
        print("****************************************************************", brief_id, type(brief),brief)
        if brief is None:
            raise HTTPException(status_code=400, detail="Brief not found")
        
        result_json = brief.result

        return {
            "brief_id": brief_id,
            "status": brief.status,
            "results": result_json,
            "events": [{"timestamp": event.timestamp.isoformat(), "data": event.data} for event in brief.events]
        }
            

    return response

def kickoff_crew(brief_id: str, content: str):
    logger.info(f"Crew for brief {brief_id} is starting..")
    results = {}
    try:
        logger.info(f"Starting Crew")
        briefing_crew = CompanyBriefingCrew(brief_id)
        briefing_crew.setup_crew(content)
        crew_results = briefing_crew.kickoff()
        logger.info(f"Crew for {brief_id} is completed", crew_results)
        tasks_outputs = crew_results['tasks_outputs']
        # print("*&T#*&Q*W&R^(WQ*&Tasks Outputs: ", tasks_outputs)
        final_brief = tasks_outputs[0].exported_output
        all_questions = tasks_outputs[1].exported_output
        # print("Final Brief: ", final_brief)
        # print("All Question: ", all_questions)
        
        results = {
            "final_brief":final_brief,
            "questions":json.loads(all_questions)
        }

        # print("#@%#%%@%^**@#$", results)


    except Exception as e:
        logger.error(f"Error occurred while starting crew for brief {brief_id}: {str(e)}")
        append_event(brief_id, f"An error in crew: {str(e)}")
        with jobs_lock:
            jobs[brief_id].status = 'ERROR',
            jobs[brief_id].result = str(e)
    
    with jobs_lock:
        jobs[brief_id].status = 'COMPLETE'
        jobs[brief_id].result = results
        jobs[brief_id].events.append(
            Event(timestamp=datetime.now(), data = "Crew complete")
        )

def generate_brief(content:str):
    brief_id = uuid4()
    thread = Thread(target=kickoff_crew, args=(brief_id, content))
    thread.start()
    return ResGenerateBrief(brief_id = brief_id)

# def create_item(db: Session, item: schemas.ItemCreate):
#     db_item = models.Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
