import subprocess


def lambda_handler(event, context):
   # This lambda_handler, which is written in python2.7, 
   # will invoke python3 script with virtualenv-ed 
   # python3 interpreter. Add proper argument according to 
   # your script. 
   # For example myrobot.py takes additional 
   # argument, say N, and run the script N number of times. 
   # It is just for demo purpose. 
   args = ("venv/bin/python3.4", "myrobot.py", "1")
   popen = subprocess.Popen(args, stdout=subprocess.PIPE)
   # Link subprocess's output to current process output
   # So you can see stdout result on AWS Console's log section.
   popen.wait()
   output = popen.stdout.read()
   print(output)
