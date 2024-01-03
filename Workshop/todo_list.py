class Task:
    def __init__(self, nombre, estado="Pendiente"):
        self.nombre = nombre
        self.estado = estado

    def completar(self):
        if self.estado == "Pendiente":
            self.estado = "Completada"

tasks_list = []

#Adding a task
def add_task(nombre):
    task = Task(nombre)
    tasks_list.append(task)

def list_all_task():
    print("Tasks: ")
    for task in tasks_list:
        print("\t- " + task.nombre)

def mark_completed(task):
    task.completar()

def clear_completed():
    tasks = tasks_list.copy()
    tasks_list.clear()
    for task in tasks:
        if(task.estado == "Pendiente"):
            tasks_list.append(task)

def clear_all_task():
    tasks_list.clear()

def mark_all_completed():
    for task in tasks_list:
        task.completar()


