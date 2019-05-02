import json

paths = ['/Users/luhao/Desktop/Indeed_jobsite/Indeed_jobsite/Indeed_jobsite/Monster.json',
         '/Users/luhao/Desktop/Indeed_jobsite/Indeed_jobsite/Indeed_jobsite/Reed.json',
         '/Users/luhao/Desktop/Indeed_jobsite/Indeed_jobsite/Indeed_jobsite/CVLibrary.json',
         '/Users/luhao/Desktop/Indeed_jobsite/Indeed_jobsite/Indeed_jobsite/Glassdoor1.json',
         '/Users/luhao/Desktop/Indeed_jobsite/Indeed_jobsite/Indeed_jobsite/Indeed.json',
         '/Users/luhao/Desktop/Indeed_jobsite/Indeed_jobsite/Indeed_jobsite/Independentjobs.json',
         '/Users/luhao/Desktop/Indeed_jobsite/Indeed_jobsite/Indeed_jobsite/Totaljobs.json']

singledes_collection = []
with open(paths[2], encoding='utf-8') as f:
    file = json.loads(f.read())
for dic in file:
    singledes_collection.append(dic['description'])

filtered_single_collection = [x for x in singledes_collection if x]
print(len(filtered_single_collection))

for x in filtered_single_collection:
    if x =='':
        print('empty description found')
