
### Python 2.7.5
### Ionic 1.2.8
import subprocess, os, sys, glob
from bs4 import BeautifulSoup
### take arguments.. need project name, source
### need to make sure all the files have the same name

# name = raw_input('Enter project name: ')






name = "test"

def change_dir(dir_name):
	os.chdir(os.path.join(os.path.abspath(sys.path[0]), dir_name))
def add_platform():
	subprocess.call(["ionic", "platform", "add", "ios"])	
def start_project(project_name):
	subprocess.call(["ionic", "start", project_name])
def build(): 
	subprocess.call(["ionic", "build", "ios"])
def emulate(): 
	subprocess.call(["ionic", "emulate", "ios", "--target=\"iPad\""])
def serve(): 
	subprocess.call(["ionic", "serve"])
def bower():
	subprocess.call(["bower", "install"])
def copy_tempaltes(dir_name):
	subprocess.call(["rm", "-r", name + "/www"])
	subprocess.call(["cp", "-r", "www", name])

originalWorkingDiretory = os.getcwd()
start_project(name)
change_dir(name)
add_platform()
os.chdir(originalWorkingDiretory)


copy_tempaltes(name)


####TODO: for each image in source
##### add newPage in css --done
##### add newPage's state in route.js
##### add newPage.html
##### add newPage.js
##### add new line for src in newPage.js 

def parse_file_path(full_name):
	basename, extension = os.path.splitext(file_fullname)
	directory, filename = os.path.split(basename)
	return { "directory": directory, "filename": filename, "extension": extension}

def getCSStemplate(file_info):
	return '.background-' + file_info["filename"] + ' {\n' \
				'background-image:url("../img/' + file_info["filename"] + file_info["extension"] + '\");\n' \
				'background-repeat: no-repeat;\n' \
				'background-size: 100%;\n' \
				'width: 1024px;\n' \
				'height: 625px;\n' \
				'position: relative;\n' \
			'}'

for file_fullname in glob.glob(os.path.join(originalWorkingDiretory + "/src", '*.png')):
	file_info = parse_file_path(file_fullname)
	with open("test/www/css/app.css", "a") as myfile:
		myfile.write(getCSStemplate(file_info))

change_dir(name)
bower()
build()
emulate()

#### replace div in index.html
# def body_template():
# 	return 	'\n\t\t\t<body ng-app="starter"> \n\
# 				<ion-side-menus> \n\
# 					<ion-side-menu-content> \n\
# 						<div ng-include src=\"\'partials/menuContent.html\'\" ng-controller=\"MainCtrl\"></div> \n\
# 					</ion-side-menu-content> \n\
# 					<ion-side-menu side=\"right\"> \n\
# 						<div ng-include src=\"\'partials/rightMenu.html\'\"></div> \n\
# 					</ion-side-menu> \n\
# 				</ion-side-menus> \n\
# 			</body>'

# soup = BeautifulSoup(open("test/www/index.html"))
# soup.body.replace_with(BeautifulSoup(body_template()))

#### write index.html file
# html = soup.prettify("utf-8")
# with open("test/www/index.html", "wb") as file:
# 	file.write(html)


####add content to basic files

