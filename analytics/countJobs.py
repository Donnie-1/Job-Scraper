import json


with open('../jobscraper/jobscraper/jobs3000.json') as json_file:
    json_data = json.load(json_file)
    
    job = json_data[1]

    languages = {"python": 0, "java ": 0, "c#": 0, "c++": 0, "javascript": 0, "ruby": 0, "typescript": 0, "rust": 0, "shell": 0, "node": 0} 
    cloud = {"aws": 0, "azure": 0, "gcp": 0, "redhat": 0}
    devops = {"kubernetes": 0, "ci/cd": 0, "jenkins": 0, "docker": 0, "ansible": 0, "terraform": 0, "nagios": 0, "prometheus": 0}
    ai = {"tensorflow": 0, "pytorch": 0, "scikit-learn": 0, "scikit": 0, "caffe": 0, "opencv": 0, "genism": 0}
    database = {"mysql": 0, "postgresql": 0, "mongoDB": 0, "mongo": 0, "Cassandra": 0, "Elasticsearch": 0, "Firebase": 0, "Redis": 0, "sqllite": 0, "oracle": 0, "sql server": 0, "sql": 0}
    education = {"degree": 0, "tertiary": 0}
    soft_skills = {"communication": 0, "teamwork": 0, "leadership": 0, "proactive": 0, "problem solve": 0, "work ethic": 0}   
    web_frameworks = {"react": 0, "angular": 0, "vue": 0, "express": 0, "laravel": 0}
    data_analytics = {"matplotlib": 0, "powerbi": 0, "pandas": 0, "numpy": 0, "tableau": 0, "power bi": 0, "qlikview": 0, "d3": 0}
    
    tech = [languages, cloud, devops, ai, database, education, soft_skills, web_frameworks, data_analytics]
    names = ["languages", "cloud", "devops", "ai", "database", "education", "soft_skills", "web_frameworks", "data_analytics"]

    categories = { "languages": languages, "cloud": cloud, "devops": devops, "ai": ai, "database": database, "education": education, "soft_skills": soft_skills, "web_frameworks": web_frameworks, "data_analytics": data_analytics}

    array = []
    for job in json_data:
        for key, value in job.items():
            if isinstance(value, list):
                for element in value:
                    if element not in categories[key]:
                        categories[key][element] = 1
                    else:
                        categories[key][element] += 1
                       
    for job in json_data:
        if ("graduate" in job["title"] or "Graduate" in job["title"]) and "Sydney" in job["location"]:
            array.append( "https://www.seek.com.au/" + job["link"])

    print(array)

# with open('categories.json', 'w') as json_file:
#     json.dump(categories, json_file)

# with open('categories.json', 'r') as json_file:
#     json_data = json.load(json_file)
#     json_data = json.dumps(json_data, indent=4)
#     print(json_data)