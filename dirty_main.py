from datetime import *
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    print(f'Сегодня удачный день: {datetime.now().strftime("%d.%m.%Y")}')
    calculate_salary('Петр Сидорович Иванов')
    get_employees('Отдел глобального потепления')