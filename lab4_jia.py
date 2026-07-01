# Jia Cheng Ouyang | Lab 4 | Hustle

#Ticket 1
ages =  [17, 11, 23, 9, 13]

for age in ages:
    if age >= 13:
        print(f"{age} Access Granted")
    else:
        print(f"{age} Access Denied")
        # I think 17 23 13 will have access granted and 11 9 will be denied
        # I think it holds the age

#Ticket 2
keep_going = "yes"

while keep_going == "yes":
    keep_going = input("Are you 13 or above?")
    if keep_going == "yes":
        input("What is your age?")
        if age >= 13:
            print("Very Good!")
    else: 
        print("That's no good!")
    keep_going = input("Do you want to check another age?")
# I think it just doesnt run the code and skips to do you want to check another age
# because like it keeps checking and running until you say no for loop only run once

#Ticket 3
#while True: 
   #age = input("Enter your select age or type stop to exit code")
   #if input == "exit":
        #break
   
  # age = int(age)
    
  # if age >= 13:
        #print(f"{age} access granted")
  # else:
        #print(f"{age} access denied")
        #the loop does not end whatsoever
        # i think this one just keeps going and was a little more buggy for me

# Ticket 4
def can_access(age):
   return age >= 13

for age in ages:
    if can_access(age):
        print(f"{age} - Access Granted")
    else:
        print(f"{age} - Access Denied")
    #Im like returning my function instead of using age >= 13
    # its eeasier 

# Ticket 5
signups =[22, 10, 15, 8, 19, 13]

def signup_report(signups):
    approved = 0

    print("--- StreamPass Signup Report---")

    for number, age in enumerate(signups, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} - Access granted")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} - Too Young")
    
    print(f"\nApproved: {approved} out of {len(signups)}")

signup_report(signups)
# I think uh 4 out of 6 approved
# I used functions, loops, strings, paremeters, condtionals, lists



  


