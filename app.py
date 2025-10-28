import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)



""" #f1
for i in data:
    print(i["title"]) """

""" #f2
x = input("Give me a year")
y = int(x)
for i in data:
    if i["year"] >= y:
        print (i["title"])
 """

""" #f3
x = input("Give me a minimum year")
y = input("Give me a maximum year")
x = int(x)
y = int(y)
for i in data:
    if x >= i["year"] >= y or y >= i["year"] >= x:
        print (i["title"]) """

""" #f4
x = input("Give me a year")
y = int(x)
for i in data:
    if i["year"] == y:
        print (i["title"]) """

""" #f5
x = input("Give me a movie title")
y = x.lower()
for i in data:
    if y in i["title"].lower():
        print (i["title"]) """

""" #f6
x = input("What genre would you like")
for i in data:
    if x in i["genres"]:
        print (i["title"])
  """