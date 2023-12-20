import os
import subprocess

# Execution sans params
script_dir = os.path.dirname(__file__)
script_absolute_path = os.path.join(script_dir, "Files/script.sh")

subprocess.call(['bash', script_absolute_path])

# execution avec params
param_script_absolute_path = os.path.join(script_dir, "Files/parm.sh")
subprocess.call(['bash', param_script_absolute_path, 'param1 param2'])
