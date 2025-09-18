menu_chicken = int(input())
menu_fish = int(input())
menu_vegetarian = int(input())

menu_chicken_price = 10.35
menu_fish_price = 12.40
menu_vegetarian_price = 8.15
delivery_price = 2.50

menu_chicken_total = menu_chicken * menu_chicken_price
menu_fish_total = menu_fish * menu_fish_price
menu_vegetarian_total = menu_vegetarian * menu_vegetarian_price

menus_total = menu_chicken_total + menu_fish_total + menu_vegetarian_total

dessert_price = (0.20 * menus_total)

total = menus_total + dessert_price + delivery_price

print(f"The total price is: {total}")
