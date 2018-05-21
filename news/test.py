import os, json

class article(object):
    def __init__(self):
        self.file_dir = os.getcwd() + '/..' + '/files'
        self.filename = os.listdir(self.file_dir)

    def get_json_content(self):
        content_dict = {}
        for i in self.filename:
            fle = self.file_dir + '/' + i
            with open(fle) as f:
                content_dict[i[:-5]] = json.load(f)
        return content_dict

    def get_title(self):
        a = self.get_json_content()
        return [item['title'] for item in a.values()]

test = article()

a = test.get_json_content()
#a = test.get_title()
a_dict = {}
for key,value in a.items():
    a_dict[key]=value['title']

print(a_dict)
print(a_dict.keys())
