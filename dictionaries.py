# Dictionaries like as the object in Javascripts as a json format
# Dictionaries work wiht "key":"value" pairs and start with curly{} brackets
from cgi import print_form


employees = {"chef":"joe","ceo":"jonson"}

# Adding in key value pair in existing dictionaries
employees["waiter"] = "Mike"
print(employees)
#update k-v pairs
employees["ceo"] = "jason"
print(employees["ceo"].upper())

stocks_price = {"GOOGLE":[200,320,343],"GME":[2,4,54]}
history = stocks_price["GOOGLE"]
print(f"first day price is: {history[0]}")
#nested dictionaries
# dictionaries can contains another dictionaries. It's valid in python
mydict = {"OUTER":{"INNER":100}}
# access the outer value
print(mydict["OUTER"])
# access the inner value
print(mydict["OUTER"]["INNER"])

myKey = {'key1':1000,'key2':200,'key3':300,'key4': 500}
# access only keys
print("The keys are", myKey.keys())
# access only value
print("The vulues are ",myKey.values())
# show the K-V pairs and it will be print as a tuples
print(myKey.items())