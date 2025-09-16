square_meters_to_landscape = float(input())
one_square_meter = 7.61
discount_rate = 0.18

total = square_meters_to_landscape * one_square_meter
discount = discount_rate * total
final_price = total - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")
