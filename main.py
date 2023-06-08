from datetime import datetime, date, time
import application.salary    
from application import salary
import application.db.people
from application.db import people

if __name__ == '__main__':
    print(datetime.now(tz=None), salary.calculate_salary(1))
    print(datetime.now(tz=None), people.get_employees(1))
    
