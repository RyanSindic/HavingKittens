Amnt_Cats = 1
temp_months = 0
all_months = [0]
generation = 1
first_pregnancy = 1
total = 0
temp_num = 0
print("in how many months do you want to look")
month = int(input())

def NewCat(Current_Month,Last_Month):



while temp_months < month:
    temp_months = temp_months + 1

    all_months.append(temp_months)
print(all_months)
for submonth in all_months:
    if submonth%6 == 0:
        #print("submonth " + str(submonth))
        generation = generation * 6
        temp_num = submonth
        while temp_num <= month:
            print(total)
            total = total + generation
            temp_num = temp_num + 4
        #print(total)

#total = total + 6*int(month)
#print(generation)
print(total)
