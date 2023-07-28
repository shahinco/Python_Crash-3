offer_foods = ['pasta','soupe', 'pizza', 'hamburger', 'fish&chips']
print(offer_foods)

for offer_food in offer_foods:
    print(offer_food.title())

offer_foods = offer_foods[:]
offer_foods.append('carrot cake')
offer_foods.append('beef rosted')
print("\nModified menu:")
for offer_food in offer_foods:
    print(offer_food.title())




