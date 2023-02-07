total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
annual_salary = float(input("Enter your annual salary "))
portion_saved = float(input("Enter the percent of your salary, as a decimal: "))
investment = 0 
number_of_months = 0
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal "))

while current_savings < portion_down_payment:
    number_of_months = number_of_months + 1

    if number_of_months % 6 == 0:
        annual_salary = (annual_salary * semi_annual_raise) + annual_salary
    
    current_savings = current_savings + (annual_salary/12) * portion_saved
    investment = current_savings*r/12
    current_savings = current_savings + investment

    

print(number_of_months)

    
    
    
    
    
    
    
    
    