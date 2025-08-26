import requests 
import json
#api endpoint(example:public API for random uses)
url="https://randomuser.me/api/?results=5"
#fetch data from API
response=requests.get(url)
#check if request was successful
if response.status_code==200:
    data=response.json()
    print("API DATA FETCHED SUCCESSFULLY!\n")
    #print fetched data
    print(json.dumps(data,indent=4))
    #prcoess data(extract only name and emals)
    users=[]
    for user in data['results']:
        users.append({"name":f"{user['name']['first']}{user['name']['last']}",
                      "email":user['email']})
        #saved process data to json
    with open("users.json","w")as f:
        json.dump(users,f,indent=4)

    print("\n Processed user data saved to users.json")

 
else:
    print(f"Error:Unable to fetch data (Status code:{response.status_code})")

