''' tuples similar as the dictionaries but there are a bit difference. 
     List in muteable and start with [] 
    where tuples is immuteable and start with ()
'''
my_list = [2,3,5,65]
my_tuples = (3,53,53)

my_list[0] = 'New' # will change the value in list
# won't change the vule in tupes and display errors
# my_tuples[0] = 1  # won't change the vule in tupes and display errors

print(my_list)
print(my_tuples)
my_tuple =  (1, 2, 3, 4, 5)
print(my_tuple[4])
# boolean
print(my_tuple[4] <10)