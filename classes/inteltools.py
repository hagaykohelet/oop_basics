class Inteltools:
    @staticmethod
    def encript_message(msg:str):
        return msg [::-1]


    @staticmethod
    def log_transmission(agent_name:str, message:str):
        print(f"{agent_name} sent encrypted messege: {message}")

