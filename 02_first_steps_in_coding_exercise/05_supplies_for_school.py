pen_packs = int(input())
marker_packs = int(input())
cleaning_detergent_liters = int(input())
discount = int(input())

pen_pack_price = 5.80
marker_pack_price = 7.20
cleaning_detergent_price_per_liter = 1.20

pen_packs_total = pen_packs * pen_pack_price
marker_pack_total = marker_packs * marker_pack_price
cleaning_detergent_total = cleaning_detergent_liters * cleaning_detergent_price_per_liter

total = pen_packs_total + marker_pack_total + cleaning_detergent_total

total_discounted_price = total - (total * (discount / 100))

print(total_discounted_price)
