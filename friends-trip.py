# friends-trip.py
me_and_my_friend = set(["Dorin", "Radj"])
my_friends = ["John", "Marry", "Jane"]
my_best_friend_friends = ["Marry", "Pete", "Oliver", "Mia"]
# people_to_exclude = ["Pete", "Marry"]
# hm2*: enter the names of people to exlude from the keyboard
people_to_exclude = input("enter names separated by spaces").split()
trip_people_list = me_and_my_friend.union(
 my_friends, 
 my_best_friend_friends
)
trip_people_list = trip_people_list.difference(people_to_exclude)
print(len(trip_people_list), "are going along:")
# for participant in trip_people_list:
 # print(participant)
# hm1: 6 are going along:
# 1. Jane
# 2. Dorin
# 3. Radj
c = 1
for participant in trip_people_list:
 print(f"{c}. {participant}")
 c += 1
