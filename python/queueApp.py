# TUAZON, Francesca Marie A. 

'''
	Mini Activity
		- add the ability to prioritize tasks
			- have the priority leel for each task and when processing tasks, higher priority tasks will be processed first
		- add the remaining_task method that prints the remaining tasks in the queue
			-- after dequeuing a task, the remaining tasks are displayed using the remaining_task method
		- Screen shot and sample output paste it in the given fileName: 231123_FFernandez_MAQueue
'''

import time

class QueueApp:
    def __init__(self):
        # initialize empty list to hold tasks
        self.task_queue = []

    def add_task(self, task, priority):
        self.task_queue.append((task, priority))
        print(f"Task added: {task} | Priority Level: {priority}")
        time.sleep(1)
        return self.task_queue

    def priority_key(self, task_priority):
        return task_priority[1]

    def process_task(self):
        if not self.task_queue:
            print("No tasks to process.")
            return

        # Sort the task queue based on priority in descending order and dequeue the highest priority task
        self.task_queue.sort(key=self.priority_key, reverse=True)
        current_task, priority = self.task_queue.pop(0)
        print(f"Processing task: {current_task} | Priority Level: {priority}")
        time.sleep(1)

    def dequeue(self):
        if not self.task_queue:
            print("No tasks to remove.")
            return None

        # Sort the task queue based on priority in descending order and dequeue the highest priority task
        self.task_queue.sort(key=self.priority_key, reverse=True)
        dequeued_task, priority = self.task_queue.pop(0)
        print(f"Task Completed: {dequeued_task} | Priority Level: {priority}")
        time.sleep(1)
        return dequeued_task

    def remaining_tasks(self):
        print("Upcoming Tasks:", self.task_queue)

# Example usage:
scheduler = QueueApp()

scheduler.add_task("fixing my bed", priority=2)
scheduler.add_task("cleaning my room", priority=1)
scheduler.add_task("washing dishes", priority=3)

scheduler.remaining_tasks()
scheduler.dequeue()
scheduler.remaining_tasks()
scheduler.dequeue()
scheduler.remaining_tasks()
scheduler.dequeue()
scheduler.remaining_tasks()
scheduler.process_task()
