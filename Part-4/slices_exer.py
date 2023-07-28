my_favorite_teams = ['Fener Bahce', 'Manchester City', 'Liverpool','Juventus']
my_friend_team = my_favorite_teams[:-3]

print(my_favorite_teams)
print("\nMy Best best Turkish team is: ")
print(my_favorite_teams[0:1])

print("\nMy UK Best favorite team is:")
print(my_favorite_teams[1:3])

my_friend_team.append("Arsenal")

print("\nMy Friend teams are:")
print(my_friend_team)

for my_favorite_team in my_favorite_teams:
    print(my_favorite_team[2])
    print('\nChampion is', my_favorite_team[:1])


