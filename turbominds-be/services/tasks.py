from textwrap import dedent
from typing import List
from crewai import Agent, Task
from schemas.brief import AllQuestions, ResultQuestions
from utils.logging import logger
from utils.job_manager import append_event


class BriefAnalyzer():
    def __init__(self, brief_id):
        self.brief_id = brief_id

    def append_event_callback(self, task_output):
        logger.info("Callback called: %s", task_output)
        append_event(self.brief_id, task_output.exported_output)

    def business_analysis_task(self, agent: Agent, content: str):
        return Task(
            agent=agent,
            expected_output=dedent(f"Text in Markdown format containing detailed brief analysis in numbered format of sections and subsections."),
            description=dedent(f"""
            Analyze the brief given to a marketing firm and give results containing 
            - Requirement
            - Campaign Overview
            - Campaign Goals
            - Target Audience
            - KPIs
            - Budget
            - Timeline

            Do not assume anything on your own or make any suggestions for any of the topic mentioned above.
            If anything within the topic not mentioned in the prompt just say: Nothing specified about the topic.
            You must not create campaign goals, budget, timeline, KPIs on your own or make any suggestions.
            Here is the prompt given by client
            ```
            {content}
            ```
            """),
            output_file = f"Brief.md",
            callback=self.append_event_callback
        )   

    def gap_analyst_task(self, agent: Agent, brief: Task, content: str):
        return Task(
            agent=agent,
            expected_output=dedent("JSON response in format array of objects containing topic and question"),
            description=dedent(f"""
            Based on the response from Business Analyst agent for the prompt {content},
            Identify gaps in brief given by Business Analyst agent. Ask follow-up questions about the brief on each topic.
            The topics are 
            - Requirement
            - Campaign Overview
            - Campaign Goals
            - Target Audience
            - KPIs
            - Budget
            - Timeline
            These topics should be mentioned in the the brief. Give only one question for each topic.
            For each question give a unique id in UUID4 format.
            End output should be a json array of objects containing id, question and topic.
            """),
            context=[brief],
            callback=self.append_event_callback,
            output_json=AllQuestions
        )

    