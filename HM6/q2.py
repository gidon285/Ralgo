import gspread
import pandas as pd
from fairpy.items import fair_division_under_cardinality_constraints as fducc
import json

account = gspread.service_account("C:\\Users\\gidon\\OneDrive\\Desktop\\Ralgo\\HM6\\algorithmsq2-1a1003d9fd9d.json")
spreadsheet = account.open("test")
sheet = spreadsheet.worksheet("Sheet1")
df = pd.DataFrame(sheet.get_all_records())

agents_evaluation ={}
agent_names = []
catagories = []
items = dict()
temp_item = set()

# 3 agents
for i in range(0,3):
    agent = df.loc[i]['agents_names']
    agent_names.append(agent)
    evaluation = json.loads("\""+str(df.loc[i]['evaluation'])+"\"")
    agents_evaluation[agent] = evaluation


# 2 catagories
for i in range(0,2):
    category = df.loc[i]['catagories']
    catagories.append(category)
    # x items in each category
    for j in range(0, df.loc[0]['items']):
        temp_item.add(df.loc[j][category])
    items[category] = temp_item
    temp_item = set()

d = fducc.Data(catagories,agents_evaluation,items)
ans = fducc.ef1_algorithm(agent_names,d)
sheet1.update("G1", "Player X")
