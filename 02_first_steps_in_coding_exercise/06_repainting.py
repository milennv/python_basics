nylon_quantity_square_meters = int(input())
paint_quantity_liters = int(input())
thinner_quantity_liters = int(input())
hours = int(input())

nylon_price_square_meter = 1.50
paint_price_liter = 14.50
thinner_price_liter = 5.00

nylon_total = (nylon_quantity_square_meters + 2) * nylon_price_square_meter
paint_total = (paint_quantity_liters * 1.10) * paint_price_liter
thinner_total = thinner_quantity_liters * thinner_price_liter
bags_total = 0.40

materials_total = nylon_total + paint_total + thinner_total + bags_total

craftsmen_total = (materials_total * 0.30) * hours

print(materials_total + craftsmen_total)
