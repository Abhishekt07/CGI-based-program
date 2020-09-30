#!/usr/bin/python

import cgi
import subprocess

print("context-type: text/html")
print()



data = cgi.FieldStorage()
user_input = data.getvalue("command")
CMD = user_input.lower()



try:
	output = subprocess.getoutput(CMD)
	if "command not found" in output or "Error" in output:
		print("\n Oops! something went wrong...")
		print("\n Please enter valid command")
	else:
		print("\n")
		print("""<h3 style="color: white">{} </h3>""".format(output))
except:
	print("Error")