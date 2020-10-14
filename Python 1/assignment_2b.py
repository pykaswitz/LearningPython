# Brian Wolfe                       Created: 09/14/2020

print("-------------------------------------------------------")
print("     Assignment 2B: Individual and Team Pay Total")
print("-------------------------------------------------------")
print()

loop = True
total_pay = 0.00
max_regular_hours = 40.00

while loop:
    pay_rate = float(input("Enter employee's pay-rate (more than $9.25): "))
    hours_worked = float(input("Enter hours worked this week (zero or a positive number): "))

    # DETERMINES IF THERE WAS OVERTIME PAY
    if hours_worked > max_regular_hours:
        overtime_hours_worked = hours_worked - max_regular_hours
        overtime_pay_rate = pay_rate + (pay_rate / 2)
        calc_pay = (pay_rate * max_regular_hours) + (overtime_pay_rate * overtime_hours_worked)
    else:
        calc_pay = pay_rate * hours_worked

    # TALLIES TOTAL PAY FOR EACH LOOP
    total_pay += calc_pay  # Another way to write this is: total_pay = total_pay + calc_pay

    print(f"Employee's weekly pay: ${format(calc_pay, ',' '.2f')}")

    another_entry = input("Do you wish to continue? (y/n): ")

    if another_entry == "n":
        print(f"Total pay for all employee's is: ${format(total_pay, ',' '.2f')}")
        break  # Could set loop value to False
