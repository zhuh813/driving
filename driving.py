country = input('請問是哪國人: ')
age = input("輸入年齡: ")
age = int(age)

if country == '臺灣' or country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照') 	

elif country == '美國':
	if age >= 16:
		print('你可以考駕照')	
	else:
		print('你還不能考駕照')
else:
	print('只能輸入台灣(臺灣)或美國')
