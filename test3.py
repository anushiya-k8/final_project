import json
 
 
# JSON string
employee ='{"id":"09", "name": "Nitin", "department":"Finance"}'
 
# Convert string to Python dict
#employee_dict = json.loads("static/walletchain.json",encoding="utf-8")
#print(employee_dict)
 
#print(employee_dict['Hash'])


#json_object = json.dumps("static/walletchain.json", indent = 4)
#print(json_object)


import pandas as pd

myjson = json.loads("static/walletchain.json")
'''myjson= {'data': [{'ID': 'da45e00ca',
   'name': 'June_2016',
   'objCode': 'ased',
   'percentComplete': 4.17,
   'plannedCompletionDate': '2021-04-29T10:00:00:000-0500',
   'plannedStartDate': '2020-04-16T23:00:00:000-0500',
   'priority': 4,
   'asedectedCompletionDate': '2022-02-09T10:00:00:000-0600',
   'status': 'weds'},
  {'ID': '10041ce23c',
   'name': '2017_Always',
   'objCode': 'ased',
   'percentComplete': 4.17,
   'plannedCompletionDate': '2021-10-22T10:00:00:000-0600',
   'plannedStartDate': '2021-08-09T23:00:00:000-0600',
   'priority': 3,
   'asedectedCompletionDate': '2023-12-30T11:05:00:000-0600',
   'status': 'weds'},
   {'ID': '10041ce23ca',
   'name': '2017_Always',
   'objCode': 'ased',
   'percentComplete': 4.17,
   'plannedCompletionDate': '2021-10-22T10:00:00:000-0600',
   'plannedStartDate': '2021-08-09T23:00:00:000-0600',
   'priority': 3,
   'asedectedCompletionDate': '2023-12-30T11:05:00:000-0600',
   'status': 'weds'}]}'''

reff = pd.json_normalize(myjson['data'])
df = pd.DataFrame(data=reff)
print(df)
