people =[
    {"name":"rabii","city":"sfax"},
    {"name":"may","city":"tunis"},
    {"name":"catrina","city":"berlin"},
    {"name":"anita","city":"LA"}
]

def fn(people):
    return people["name"]
    # return people.name  ma temchich haka

people.sort(key=fn)

print (people)