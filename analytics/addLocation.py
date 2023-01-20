import json
from postcodes import aus

with open('./jobsCleaned.json') as json_file:
    json_data = json.load(json_file)

# loop through the JSON data and set the latitude and longitude of each location
    for item in json_data:
        if (len(item["education"]) == 0): 
            item["education"] = ["None"]
                              
        for loc in aus: 
            item["occ"] = ["1"]
            if item["city"] == loc[1]:
                if (loc[3] == 0 or loc[4] == 0):
                    continue
                item["latitude"] = loc[3]
                item["longitude"] = loc[4]
                item["state"] = loc[2]
                break; 


with open("./jobsCleaned.json", "w") as f:
    json.dump(json_data, f, indent=4)