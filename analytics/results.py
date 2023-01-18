import json

f = open('../jobscraper/jobs.json')
data = json.load(f)

dict = {"python": 0, "java": 0, "c#": 0, "c++": 0, "javascript": 0, "ruby": 0, "typescript": 0, "rust": 0, "aws": 0, "api": 0}    

for i in data: 
    for j in i['keywords']:
        if j in dict.keys():
            dict[j] += 1

print(dict)
