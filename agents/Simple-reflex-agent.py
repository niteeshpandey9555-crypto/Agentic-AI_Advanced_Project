#niteesh pandey
#agentic ai project
# Simple_reflex_agent
# agents/reflex_agent.py

class ReflexAgent:
    """
    Simple Reflex Agent:
    Takes action based only on current percept
    """

    def act(self, percept):
        if percept == "urgent_task":
            return "do_immediately"
        elif percept == "normal_task":
            return "schedule_later"
        else:
            return "no_action"

