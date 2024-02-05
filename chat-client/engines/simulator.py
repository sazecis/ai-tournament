import time


class Simulator:

    no_answer_prefix = "[no-answer][just-info] "

    def __init__(self, name):
        self.name = name
        print(f"Simulator {name} created")

    def message(self, content: str):
        time.sleep(3)
        if content.startswith(self.no_answer_prefix):
            return "Acknowledged"
        return f"Habla blabla {self.name}"

    def delete_assistant():
        return
