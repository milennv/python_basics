deposit_total = float(input())
deposit_deadline_in_months = int(input())
annual_interest_rate = float(input())

total = deposit_total * annual_interest_rate
annual_interest_decimal = annual_interest_rate / 100
interest_per_month = (deposit_total * annual_interest_decimal) / 12
final_total = deposit_total + deposit_deadline_in_months * interest_per_month

print(final_total)
