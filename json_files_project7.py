import json
#read json files
with open("data.json",'r') as f:
    data=json.load(f)
    print("Original Data:")
    print(data)
#modify data(example:add a new key)
data["status"]="processed"
#write to a new json file
with open("upload_data.json","w")as f:
    json.dump(data,f,indent=4)

print("\n Updated JSON saved!")