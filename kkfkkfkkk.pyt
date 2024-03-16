name = input('saxeli : ')
last_name = input('gvari : ')
age = (input('asaki : '))
address = input('misamarti : ')

list = []

list.append(name)
list.append (last_name)
list.append(age) 
list.append(address)

full_name = list[0:2]
age_lastname = list[-2:-5]
age_fullname = list[-2:-5]
lastageaddress = list[1:4]

print (full_name, age_fullname, age_lastname, lastageaddress)