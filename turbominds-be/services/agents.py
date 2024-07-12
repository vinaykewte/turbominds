import os
from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from crewai import Agent

load_dotenv()

class BriefAgents():
    def __init__(self):
        self.llm = ChatGroq(
            model=os.getenv("LLM_MODEL"),
            max_tokens=750
        )

        # self.llm = ChatOpenAI(
        #     model="gpt-3.5-turbo",
        #     api_key="sk-proj-PTf4h7r3PYlcMM9ESrdYT3BlbkFJC4dQJKWejHop3wvfyh42",
        #     max_tokens=500
        # )

    def business_analyst_agent(self) -> Agent:
        return Agent(
            role = "Business Analyst",
            goal = "Analyse Brief given to marketing firm and re-format it.",
            backstory = """
            As an expert Business Analyst in a marketing firm you can 
            create an detailed brief based on the prompt given by client 
            to the marketing firm. You are not allowed to make any suggestions.
            """,
            allow_delegation=False,
            llm = self.llm,
            verbose = True,
            max_iter = 2
        )

    def gap_analyst_agent(self) -> Agent:
        return Agent(
            role = "Gap Analyst",
            goal = "Identify gaps in a client brief and frame questions",
            backstory = """
            As an expert Gap Analyst, you are required to ask followup questions on the brief on each topic.
            """,
            allow_delegation=False,
            llm = self.llm,
            verbose = True,
            max_iter = 2
        )

    
