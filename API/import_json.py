import json

cat_dict = {"name":"Pudding", "favourite_fruit":"melon", "breed":"cutie", "age":2}

print(type(cat_dict)) #if print type will be met with class dict

#json.dumps() #serialises json to a formatted string
#json.dump() #how we can create new files. will expect a file name/object to write to.

cat_json_str = json.dumps(cat_dict)
print(type(cat_json_str)) #this type will be a formatted json string. this means cant use any dictionary type methods on it - key:value
print(cat_json_str)

with open("newfile.json", "w") as jsonfile: #expects a file to write to
    #json.dump(cat_dict, jsonfile) #shd be able to c a new file be created now when u run this
    
with open("new_file.json") as jsonfile:
    cat = json.load(jsonfile)
    print(cat["name"])
    print(type(cat)) #will load it into a dictionary format


