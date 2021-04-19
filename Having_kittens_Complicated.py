LengthToBirth = 2               #here we initiate our parameters
MinAgeForBirth = 2
MaxAge = 120
Number_Of_Months = int(input("Please enter until which month you would like the simulation to run:  "))
time = 0
total = 0
class cat:                                  #Here we initiate our cat class, this tells our cats how to act
    def __init__(self,age,isPregnant,pregnancy):
        self.age = age
        self.isPregnant = isPregnant
        self.pregnancyLength = pregnancy

Current_cats = [cat(2,True,3)]              #Here we initiate our array with all of the cats inside of it

while time <= Number_Of_Months:             #Here we set up a while loop that loops through all of the months in our given time period

    time = time + 1

    for Cat in Current_cats:                #For each month in our time period we chek up on all of our cats to check multiple parameters
                                            #If the cat is pregnant, and if so how far along is it, and can it give birth, if yes then add
        if Cat.isPregnant == True:          #these new cats to our array and then set its progress to 0. If the cat is not pregnant it
                                            # checks if it can be based on its age and if so sets it to pregnant. It then increases the age
                                            #of all the cats by 1
            if Cat.pregnancyLength == 3:
                Current_cats.extend((cat(0,False,0,),cat(0,False,0,),cat(0,False,0,),cat(0,False,0,),cat(0,False,0,),cat(0,False,0,)))
                Cat.pregnancyLength = 0

            elif Cat.pregnancyLength < 3:
                Cat.pregnancyLength = Cat.pregnancyLength + 1
                #print(Cat.pregnancyLength)

        if Cat.isPregnant == False:
            if Cat.age >= MinAgeForBirth and Cat.age < MaxAge:
                Cat.isPregnant = True

        Cat.age = Cat.age + 1               #then here at the end it counts the amount of cats in the array and then displays them

    total = len(Current_cats) - 1

print(str(total) + ' kittens')
