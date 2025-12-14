# import mymodule

# mymodule.calculator()
# mymodule.module_name
import datetime
from datetime import datetime
from datetime import date 

def date_calculation():
    date_of_birth_str = input("Enter your date of birth (YYYY-MM-DD: ")
    date_of_birth = datetime.strptime(date_of_birth_str,"%Y-%m-%d").date()
    current_date = date.today()
    years_old = current_date.year - date_of_birth.year
    print("You are: ", years_old, "years old")

date_calculation()


class University:
    def __init__(self, name):
        self.name = name
        self.students = []
    def __str__(self):
        return f"University: {self.name} ,students: {len(self.students)}"
    def register_student(self, student):
        self.students.append(student)
    def graduate_student(self, student):
        self.students.pop(student)

class TodoList:
    def __init__(self, owner):
        self.owner = owner
        self.tasks = []

    def add_task(self):
        user_task1 = input("Enter a task: ")
        user_task2 = input("Enter a second task: ")
        self.tasks.append({"task": user_task1, "done": False})
        self.tasks.append({"task": user_task2, "done": True})

    def done(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                if task["done"] is True:
                    return task
                else:
                    return "Not done yet, loh"
        return "Task not found"

todo = TodoList("Misha")
todo.add_task()
print(todo.tasks)  
print(todo.done(todo.tasks[1]["task"]))



