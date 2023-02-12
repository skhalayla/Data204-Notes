#%%
import requests

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

#print(post_codes_req.status_code)
#print(post_codes_req.headers)
#print(post_codes_req.content)

post_codes_dict = post_codes_req.json()
print(post_codes_dict["result"]) #now working w it as a dict

#data = {"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]} #wont work bc expects a json string but we have provided a dictionary
#correction:
data = json.dumps({"postcodes": ["OX49 5NU", "M32 0JG", "NE30 1DP"]})
headers = {'Content-Type': 'application/json'}

post_multi_req = requests.post('https://api.postcodes.io/postcodes/', headers=headers, data=data)

print(post_multi_req.json()) #add [result][0][query] after json() to produce (iforgot)

#%%


import requests

pokemon = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

print(pokemon.headers) # exmaple of what u can retrieve

print(pokemon.content) # bc giving weird format, if use .json() instead, will give in nice dict format. if use type, will c that its been loaded into a nice dict

