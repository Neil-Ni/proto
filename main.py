
### Python 2.7.5
### Ionic 1.2.8
import subprocess, os, sys
from bs4 import BeautifulSoup

### take arguments.. need project name, source
### need to make sure all the files have the same name


name = raw_input('Enter project name: ')

### if the project folder does not exist
subprocess.call(["ionic", "start", name]);

originalWorkingDiretory = os.getcwd();
os.chdir(os.path.join(os.path.abspath(sys.path[0]), name))
subprocess.call("ls", shell=True)

subprocess.call(["ionic", "platform", "add", "ios"])
subprocess.call(["ionic", "build", "ios"])
# subprocess.call(["ionic", "emulate", "ios", "--target=\"iPad\""])

os.chdir(originalWorkingDiretory)

#### replace div
def body_template():
	return 	'\n\t\t\t<body ng-app="starter"> \n\
				<ion-side-menus> \n\
					<ion-side-menu-content> \n\
						<div ng-include src=\" \' partials/menuContent.html\'\" ng-controller=\"MainCtrl\"></div> \n\
					</ion-side-menu-content> \n\
					<ion-side-menu side=\"right\"> \n\
						<div ng-include src=\"\'partials/rightMenu.html\'\"></div> \n\
					</ion-side-menu> \n\
				</ion-side-menus> \n\
			</body>'

soup = BeautifulSoup(open("test/www/index.html"))
soup.body.replace_with(BeautifulSoup(body_template()))


#### write file
html = soup.prettify("utf-8")
with open("test/www/index.html", "wb") as file:
	file.write(html)




