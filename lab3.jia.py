# Jia | Lab 3 | Hustle 2026
username = "jiacheng333444"

# Ticket 1
print(len(username))
# 6
# Yes len counted every single character I had

#Ticket 2
print(username[0])
last_index = username[-1]
print(last_index)
# It will print letters B and A and I use -1 because python starts counting at 0

#Ticket 3
greeting = "Welcome to loop,"
intro = greeting + " " + "@" + username + "!"
print(intro)
print(f"{greeting} @{username}!")
# Yes both lines will look identical and the faster way is using f-string because it felt faster

#Ticket 4
# username[0] = "X"
# print(username[0])
print(username.upper)
# i think my username letter is not X
# 'str' object does not support item assignment'str' object does not support item assignment
# I think imutable is can not be changed 

#Ticket 5
feed = ["Jia", "Cheng", "Ouyang"]
print(len(feed))
print(feed[0])
#the length will be 3 and the other print will print jia and i used index 0 to get the first one

#Ticket 6
feed.append("badminton")
print(feed)
# the index will be 3 because the first index starts at 0 

#ticket 7
feed.pop(0)
print(feed)

#ticket 8
profile = {"username": "jc.o101", "followers": 160 + 50, "verified": False }
# print(profile[0])
# I think it will print 160 and i think profile[0] was supposed to print the first index which was username
# KeyError: 0    
# I think its because there is soemthing attached to the variable.

#ticket 9
profile["bio"] = "china"
print(profile)  
profile.get("age")
print(profile)
#i think this will not work 
#it printed nothing for some reason i think its safer because profile could mess up your code 

#ticket 10
print(f"@{username} has {profile['followers']} {"followers"} and {len(feed)} posts. Top post: {feed[0]}")
# I expect jiacheng333444 has 210 followers and 3 posts. Top post: Cheng
# I touched string, dictionary, and lists
# i messe dup my push




