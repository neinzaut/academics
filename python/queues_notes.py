
import time

class QueueApp:
    def __init__(self):
        # Initialize an empty list to hold tasks
        self.task_queue = []

    # Add tasks to the queue as they arrive
    def add_task(self, task):
        self.task_queue.append(task)
        print(f"Task added: {task}")
        time.sleep(1)
        return self.task_queue

    #process tasks in a first-come-first-serve basis
    # def process_task(self):
    #     index = 0
    #     while index < len(self.task_queue):
    #         current_task = self.task_queue[index]
    #         print(f"Processing task: {current_task}")
    #         index += 1
    # Process tasks in a first-come-first-serve basis

    def process_task(self):
        if not self.task_queue:
            print("No tasks to process.")
            return

        current_task = self.task_queue.pop(0)
        print(f"Processing task: {current_task}")
        time.sleep(1)

    def dequeue(self):
        if not self.task_queue:
            print("No tasks to remove.")
            return None

        dequeued_task = self.task_queue.pop(0)
        print(f"Tasks Completed: {dequeued_task}")
        time.sleep(1)
        return dequeued_task

# Example Usage:
scheduler = QueueApp()

scheduler.add_task("fixing my bed")
scheduler.add_task("cleaning my room")
scheduler.add_task("washing dishes")

print("Upcoming Tasks: ", scheduler.task_queue)
scheduler.dequeue()
scheduler.dequeue()
scheduler.dequeue()

scheduler.process_task()

'''
	Mini Activity
		- add the ability to prioritize tasks
			- have the priority leel for each task and when processing tasks, higher priority tasks will be processed first
		- add the remaining_task method that prints the remaining tasks in the queue
			-- after dequeuing a task, the remaining tasks are displayed using the remaining_task method
		- Screen shot and sample output paste it in the given fileName: 231123_FFernandez_MAQueue
'''


