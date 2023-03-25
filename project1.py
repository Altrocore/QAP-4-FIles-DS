# Project 1 - One Stop Insurance Company
# Author: Daniel Shepelev
# Created 21 March
# Updated 25 March

# Imports
import datetime
import FormatValues as FV

# Open the OSICDef.dat file and read the values into variables
f = open('OSICDef.dat', 'r')
policy_number = int(f.readline())
basic_premium = float(f.readline())
discount_add_car = float(f.readline())
extra_liability_coverage = float(f.readline())
glass_coverage = float(f.readline())
loaner_car_coverage = float(f.readline())
hst_rate = float(f.readline())
proc_fee_monthly = float(f.readline())
f.close()

# Define a list of Canadian provinces and policies
provinces = ["AB", "BC", "MB", "NB", "NL", "NT", "NS", "NU", "ON", "PE", "QC", "SK", "YT"]
policy_info = []


# User inputs and convert some inputs in upper and title case
while True:
    first_name = input("Enter the customer's first name: ").title()
    last_name = input("Enter the customer's last name: ").title()
    address = input("Enter customer's address: ")
    city = input("Enter customer's city: ").title()
    province = input("Enter customer's province (2 letter): ").upper()
    while province.upper() not in provinces:
        province = input("You entered invalid province. Please re-enter a valid province using 2 letter: ").upper()
    postal_code = input("Enter the postal code: ").upper()
    phone_number = input("Enter the customer phone number: ")
    cars_numbers = int(input("Enter the number of cars being insured: "))
    option_extra_liability = input("Enter (Y/N) if you want or not extra liability coverage up to $1.000.000: ").upper()
    option_glass_coverage = input("Enter (Y/N) if you want or not optional glass coverage: ").upper()
    option_loaner_car = input("Enter (Y/N) if you want or not optional loaner car: ").upper()
    payment_type = input("Enter the payment type (F) for full or (M) for monthly: ").upper()

    # Calculations
    insurance_premium = basic_premium + ((cars_numbers-1) * (basic_premium * discount_add_car))
    total_extra_cost = 0.00
    if option_extra_liability == 'Y':
        total_extra_cost += extra_liability_coverage * cars_numbers
    if option_glass_coverage == 'Y':
        total_extra_cost += glass_coverage * cars_numbers
    if option_loaner_car == 'Y':
        total_extra_cost += loaner_car_coverage * cars_numbers

    total_insurance_premium = insurance_premium + total_extra_cost
    hst = total_insurance_premium * hst_rate
    total_cost = total_insurance_premium + hst
    monthly_payment = 0
    if payment_type == 'M':
        monthly_payment = (proc_fee_monthly + total_cost) / 8

    invoice_date = datetime.date.today()
    next_payment_date = invoice_date.replace(day=1)
    if invoice_date.month == 12:
        next_payment_date = next_payment_date.replace(year=invoice_date.year+1, month=1)
    else:
        next_payment_date = next_payment_date.replace(month=invoice_date.month+1)

    # Converting
    total_extra_cost_DPS = FV.FDollar2(total_extra_cost)
    total_insurance_DPS = FV.FDollar2(total_insurance_premium)
    total_cost_DPS = FV.FDollar2(total_cost)
    hst_DPS = FV.FDollar2(hst)
    monthly_payment_DPS = 0
    if payment_type == 'M':
        monthly_payment_DPS = FV.FDollar2(monthly_payment)
    city_DPS = "{:>19s}".format(city)

    # Outputs
    heading = "One Stop Insurance Company"
    print("-"*76)
    print()
    print(f"{heading:^76}")
    print()
    print("-"*76)
    heading2 = "Customer information"
    print(f"{heading2:^76}")
    print(f"     {first_name[0]}. {last_name:<26}     ")
    print(f"     {address:<29s}")
    print(f"     {city_DPS.strip()},{province:<2s} {postal_code:<6}")
    print()
    print(f"Phone number: {phone_number:<10s}")
    print("-"*76)
    heading3 = "Car Details"
    print(f"{heading3:^76}")
    print(f"Number of cars: {cars_numbers}")
    if option_extra_liability == 'Y':
        print(f"Extra liability coverage: selected")
    else:
        print(f"Extra liability coverage: doesn't selected")
    if option_glass_coverage == 'Y':
        print(f"Glass coverage: selected")
    else:
        print(f"Glass coverage: doesn't selected")
    if option_loaner_car == 'Y':
        print(f"Loaner car coverage: selected")
    else:
        print(f"Loaner car coverage: doesn't selected")
    print("-"*76)
    heading4 = "Payment information"
    print(f"{heading4:^76}")
    print(f"Payment method: {'Full' if payment_type == 'F' else 'Monthly'}")
    print(" " * 38, "Total extra cost:", f"{total_extra_cost_DPS:>19}")
    print(" " * 38, "Total insurance premium:", f"{total_insurance_DPS:>12}")
    print(" " * 38, "HST:", f"{hst_DPS:>32}")
    print(" " * 38, "-"*37)
    print(" " * 38, f"Total cost: {total_cost_DPS}")
    if payment_type == 'M':
        print()
        print(f"Monthly payment: {monthly_payment_DPS}")
    print()
    print("-" * 76)
    print(f"Invoice date: {invoice_date}", " " * 13, f"Next payment date: {next_payment_date}")
    print()

    # Saving policy data into list
    policy_info.append((policy_number, invoice_date, first_name, last_name, address, city, province, postal_code,
                        phone_number, cars_numbers, option_extra_liability, option_glass_coverage, option_loaner_car,
                        payment_type, total_insurance_premium))

    policy_number += 1

    continue_policies = input("Do you want to start enter the another policy? (Y/N): ").upper()
    if continue_policies == 'N':
        break

# Save policy data to file Policies.dat
f = open('Policies.dat', 'a')
for data in policy_info:
    f.write(",".join(map(str, data)) + "\n")
f.close()

f = open('OSICDef.dat', 'w')
f.write(str(policy_number) + "\n")
f.write(str(basic_premium) + "\n")
f.write(str(discount_add_car) + "\n")
f.write(str(extra_liability_coverage) + "\n")
f.write(str(glass_coverage) + "\n")
f.write(str(loaner_car_coverage) + "\n")
f.write(str(hst_rate) + "\n")
f.write(str(proc_fee_monthly))
f.close()

print("Policy information processed and saved")
