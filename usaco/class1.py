def calculate ():
    month_salary = float(input())
    over_time_hour = float(input())
    overtime_payment = month_salary/160 * 1.5*over_time_hour
    return overtime_payment