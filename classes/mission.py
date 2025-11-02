from classes.agent import Agent
class Mission:
    def __init__(self,mission_name:str, target_location:str):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = Agent("hagay",2000)

    def brief(self):
        print(f"mission: {self.mission_name}, target: {self.target_location}, agent: {self.assigned_agent.code_name}")

