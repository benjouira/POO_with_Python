people =[
    {"name":"rabii","city":"sfax"},
    {"name":"may","city":"tunis"},
    {"name":"catrina","city":"berlin"},
    {"name":"anita","city":"canada"}
]

#  first methode
def fn(people):
    return people["name"]
    # return people.name  ma temchich haka

people.sort(key=fn)

# Lambda methode
people.sort(key= lambda x : x["city"])


print (people)



