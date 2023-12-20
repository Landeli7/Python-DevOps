import os
import subprocess
import json

script_dir = os.path.dirname(__file__)
json_absolute_path = os.path.join(script_dir, "file.json")

subprocess.call(['echo', json_absolute_path])

with open(json_absolute_path) as json_file:
	content = json_file.read()
	print(content)
	dict = json.loads(content)
	print(dict["name"])
	for key in dict:
		print(key + ":" + dict[key])
