import os
import debugger
debugger.set_settings(show_time=True)
debugger.debug('PRINTING OS TYPE')
print(os.name)
debugger.debug('Getting user')
print(os.getlogin)
debugger.warn('May be error with user')
while True:
	
	a = int(input('Делимое: '))
	print('поделить')
	b = int(input('Делитель: '))
	try:
		answ = a / b
		print(answ)
	except Exception as e:
		debugger.fatal(e)