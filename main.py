from classes.agent import Agent
from classes.mission import Mission
from classes.inteltools import Inteltools
from classes.mission_control import MissionControl
from classes.report import Report


unit_8200 = Agent("8200",4)
repo = Report("hagay",4)
MissionControl.analyze_report(repo)
msg = Inteltools.encript_message("hello")
Inteltools.log_transmission(unit_8200.code_name,msg)