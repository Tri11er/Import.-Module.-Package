from application.salary import calculate_salary
from application.db.people import get_employees
from package_date.date import today


if __name__ == '__main__':
    print(today)
    calculate_salary()
    get_employees()