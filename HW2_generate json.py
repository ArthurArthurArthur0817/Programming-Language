import json

# 程式工程師的薪水資訊
salary_info = {
    "AR/VR Engineer": 158292,
    "Security Engineer": 165505,
    "Machine Learning Engineer": 158307,
    "Data Engineer": 155990,
    "NLP.Engineer": 160227,
    "Mobile Engineer": 160227,
    "Blockchain Engineer": 156527,
    "Backend Engineer": 157295,
    "Database Engineer": 157148,
    "Search Engineeer": 160392
}

# 熱門的程式語言資訊
Top10_popular_languages = ["Python", "JavaScript", "Java", "TypeScript", "C#","Go","HTML","C++","Ruby","C"]

# 最受需求的技能資訊
most_demand_skill = ["Go","Ruby on Rails","Scala","Ruby","React Native","Kotlin","Typescript","Kafka","React","Node.Js"]

# 程式工程師最常使用的語言資訊
engineer_using_languange =  {
    "Security Engineer": ["Web"],
    "Search Engineeer": ["Python","R","SQL"],
    "NLP.Engineer": ["Python"],
    "Mobile Engineer": ["Kotlin","Java"],
    "Machine Learning Engineer": ["Python"],
    "AR/VR Engineer": ["Unity"],
    "Backend Engineer": ["Node.Js","JavaScript"],
    "Database Engineer": ["Linux","Shell"],
    "Blockchain Engineer": ["Solidity","JavaScript"],
    "Data Engineer": ["Python","Java"]
}

# 將資訊組織成一個字典
data = {
    "salary_info": salary_info,
    "Top10_popular_languages": Top10_popular_languages,
    "most_demand_skill": most_demand_skill,
    "engineer_using_languange" : engineer_using_languange
}

# 將字典轉換為JSON格式並寫入檔案
with open('engineer_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("資料已成功寫入 engineer_data.json 檔案中。")
