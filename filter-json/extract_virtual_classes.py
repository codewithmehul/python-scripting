import json

data = ""
with open('sample.metadata.json') as json_file:
    data = json.load(json_file)

classes = [v for k,v in data.items() if k == "classes"]
out_dict = {}
out_dict['classes_with_virtual_attributes'] = []
for c in classes:
    if type(c) is dict:
        for k, v in c.items():
            out_class_dict = {}
            out_class_dict['name'] = v['name']
            classes_with_attributes = [dict(name = cattr['name'], id = cattr['id'] ) for cattr in v['attributes'] if cattr['virtual'] == True]
            if classes_with_attributes:
                out_class_dict['attributes'] = classes_with_attributes
                out_dict['classes_with_virtual_attributes'].append(out_class_dict) 

with open('out.json', "w") as out_json_file:
    json.dump(out_dict, out_json_file)
