class SimpleAgent:
    def __init__(self,goal):
        self.goal = goal

    def decide_action(self, current_state):
        if current_state == "dirty":
            return "clean"
        elif current_state == "clean":
            return "rest"
        else:
            return "explore"

agent = SimpleAgent(goal = "keep area clean")
print(agent.decide_action("clean"))