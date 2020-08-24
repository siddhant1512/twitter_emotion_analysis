from name import *
from twiii import *

print("----------TWITTER SENTIMANT ANALYSIS-------------")
print("""USER'S CHOICE FINDING THE TWEETS BY----
        1 - QUERY
        2 - USERNAME""")

choice = int(input("ENTER THE CHOICE (1 OR 2) = "))


if(choice==1):
    a = input("ENTER THE QUERY = ")
    query(a)
else:

    d = input("ENTER THE USERNAME = ")
    name(d)





