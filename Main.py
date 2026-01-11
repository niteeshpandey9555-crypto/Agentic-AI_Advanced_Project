
from tools.task_tools import (
    send_notification,
    complete_task,
    check_task_status,
    give_feedback
)

print(send_notification("AI Planning Task"))
print(complete_task("AI Planning Task"))
print(check_task_status("AI Planning Task"))
print("Reward:", give_feedback(success=True))
