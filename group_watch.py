# -*- coding: utf-8 -*-
import urllib2
import json

group_id = '23180482' # ID группы Вконтакте
count = '10' # Кол-во записей, мах = 1000
offset = 0


jsObj=open("user_list.txt", "r") 
file_user_list=json.load(jsObj) 
print(file_user_list) 
jsObj.close() 

jsObj=open("changes.txt", "r") 
changes=json.load(jsObj) 
print(changes) 
jsObj.close() 


data = {u'response': {u'count': 0, u'users': [0]}}
out_list = []



while data['response']['users'] != []:
        urlpage = 'https://api.vk.com/method/groups.getMembers?group_id='+ group_id +'&sort=id_asc&count='+ count +'&offset=' + str(offset)
        u = urllib2.urlopen(urlpage)
        page = u.read()

        data = json.loads(page)
        offset = offset + 10
        #print data
        for x in data['response']['users']:
                out_list.append(x)
                if x not in file_user_list:
                        print 'new'
                        changes.append('new '+ str(x))
        


for x in file_user_list:
        if x not in out_list:
                print 'left'
                changes.append('left '+ str(x))
print out_list


output=open("user_list.txt", "w") 
json.dump(out_list, output)
output.close()

output=open("changes.txt", "w") 
json.dump(changes, output)
output.close()


