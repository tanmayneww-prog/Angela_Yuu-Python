# Using the random module to generate random numbers and make random selections.
import random
print(random.random() ) #return bw 0 and 1 .Including 0 but not 1
print(random.uniform(1,12)) #return bw 1 and 12
print(random.triangular(1,12,5)) #return bw 1 and 12 with mode 5



# HEADS OR TAILS
heads_tails = random.randint(0,1)
print(heads_tails) #return 0 or 1
if heads_tails ==0 :
    print("Heads")
else:
    print("Tails")    



# Selecting a random element from a list.
# METHOD 1
# import random
# friends = ["tanmay" , "john ", "sam" , "kuran"] 
# print(random.choice(friends))   



# METHOD 2
# import random
# friends = ["tanmay" , "john ", "sam" , "kuran"] 
# random_index = random.randint(0,3)
# print(friends[random_index])

# NESTED LIST
first = [ "1" , "2"]
second = ["3" , "4"]
combined = [ first , second]
print(combined)