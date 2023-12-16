# social.py
class User:
 def __init__(self, nickname, rating, friends = 0, posts = 0, comments = 0):
  self.nickname = nickname
  if 0.0 <= rating <= 5.0:
   self.rating = rating
  else:
   self.rating = 0
  if friends < 0:
   self.friends = 0
  else:
   self.friends = friends
  if posts < 0:
   self.posts = 0
  else:
   self.posts = posts
  if comments < 0:
   self.comments = 0
  else:
   self.comments = comments
 def __str__(self):
  return f"{self.nickname:>8} {self.rating:6} {self.friends:7} {self.posts:5} {self.comments:8}"
 def like(self):
  if self.ratingOk() and self.rating <= 4.0:
   self.rating += 1
 def dislike(self):
  if self.ratingOk()  and self.rating >= 1.0:
   self.rating -= 1
 def ratingOk(self):
  return 0.0 <= self.rating <= 5.0
# hm1: add properties "friends", "posts", "comments" - default = 0 - ints
# * upgrade __str__() -> to reflect the changes
# HW2: if/else - secure the like(), dislike() —> 0.0 .. 5.0
# * "friends", "posts", "comments" - if/else minimum 0
users = [] # list - empty
users.append(User("Marry", 1.0, 2))
users.append(User("John", 3.5, 3, 2, 1))
users.append(User("Kate", 5.0, 1, 2))
users[1].like()
users[1].like()
users[0].dislike()
users[0].dislike()
#for i in range(len(users)):
# print(users[i])
print("nickname rating friends posts comments")
for u in users:
 print(u)