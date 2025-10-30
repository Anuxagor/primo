from datetime import datetime, timedelta
class Task:
    def __init__(self,
                 description, # Обязательный параметр
                ):
        self.dt           = datetime.now()
        self.deadline     = datetime(2025, 12,12)
        self.description  = description
        self.done         = False


    def later(self, more_days):
        self.deadline += timedelta(more_days)

t = Task('Написать классы Автомобиль, Человек, Одежда, Товар')
print(t.deadline)  # какой получился срок у задачи?
t.later(3)         # отсрочить задачу на три дня. Какой теперь срок? Напечатайте
print(t.deadline)