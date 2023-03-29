from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(f'Сегодня хороший день: {datetime.now().strftime("%d.%m.%Y")}')
    calculate_salary('Иван Петрович Сидоров')
    get_employees('Отдел тотальной автоматизации')