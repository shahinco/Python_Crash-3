# motorcycles =['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# # motorcycles[-2] = 'ducati'
# # print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)

# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
#
# print(motorcycles)

# motorcycles =['honda', 'yamaha', 'suzuki']
#
# # print(motorcycles)
# #
# # # del motorcycles[1]
# # # print(motorcycles)
# #
# # popped_motorcycle = motorcycles.pop()
# # print(motorcycles)
# # print(popped_motorcycle)
#
# last_owner = motorcycles.pop(-1)
# print(f"The lastmotorcycle I owned was a {last_owner.title()}.")

motorcycles =['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")