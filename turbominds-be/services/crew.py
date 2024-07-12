from crewai import Crew
from services.agents import BriefAgents
from services.tasks import BriefAnalyzer
from utils.job_manager import append_event


class CompanyBriefingCrew:
    def __init__(self, brief_id: str):
        self.brief_id = brief_id
        self.crew = None
    
    def setup_crew(self, content: str):
        agents = BriefAgents()
        tasks = BriefAnalyzer(brief_id = self.brief_id)

        business_analyst_agent = agents.business_analyst_agent()
        gap_analyst_agent = agents.gap_analyst_agent()

        business_analysis_task = tasks.business_analysis_task(business_analyst_agent, content)
        gap_analyst_task = tasks.gap_analyst_task(gap_analyst_agent, business_analysis_task, content)

        self.crew = Crew(
            agents = [business_analyst_agent, gap_analyst_agent],
            tasks = [business_analysis_task, gap_analyst_task],
            verbose = 2,
            full_output=True,
            max_rpm=29
        )

    def kickoff(self):
        if not self.crew:
            append_event(self.brief_id, "Crew not set up")
            return "Crew not set up"
        append_event(self.brief_id, "Task Started")
        try:
            print("Kicking off crew")
            results = self.crew.kickoff()
            print("******** Usage of crew *******: ", self.crew.usage_metrics)
            append_event(self.brief_id, f"Task Completed")
            return results
        except Exception as e:
            append_event(self.brief_id, f"Task Failed: {str(e)}")
            return str(e)