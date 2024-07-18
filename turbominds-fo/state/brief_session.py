class Brief_State():

    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.brief_result = None
        self.research_result = None
        self.stategy_result = None
        self.design_result = None
        self.final_brief = None # string 

    def update_brief_result(self, brief_result):
        self.brief_result = brief_result 
        # brief, questions

    def update_research_result(self, research_result):
        self.research_result = research_result
    
    def update_strategy_result(self, strategy_result):
        self.strategy_result = strategy_result

    def update_design_result(self, design_result):
        self.design_result = design_result


    def add_to_brief(self, content):
        if self.final_brief:
            self.final_brief.append(content)
        else:
            self.final_brief = content

    def get_final_brief(self):
        return self.final_brief
    
    def get_brief_info(self):
        return {'brief_id': self.brief_id, 'title': self.brief_title}

