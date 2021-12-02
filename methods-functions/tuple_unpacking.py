# stock_price = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
# for item in stock_price:
#     print(item)

# for tikcer,price in stock_price:
#     print(tikcer)
#     print(price)

work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]
def employee_check(work_hours):
    current_max = 0 #get the highest in the list
    employee_of_month = '' #placeholder

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
    
    return employee_of_month,current_max

print(employee_check(work_hours))