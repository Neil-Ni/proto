
### Python 2.7.5
import subprocess
import os
import sys

### take arguments.. need project name, source
### need to make sure all the files have the same name


name = raw_input('Enter project name: ')

subprocess.call(["ionic", "start", name]);

originalWorkingDiretory = os.getcwd();
os.chdir(os.path.join(os.path.abspath(sys.path[0]), name))
subprocess.call("ls", shell=True)



subprocess.call(["ionic", "platform", "add", "ios"])
subprocess.call(["ionic", "build", "ios"])
subprocess.call(["ionic", "emulate", "ios", "--target='iPad'"])
