
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
# start_project(name)
# change_dir(name)
# add_platform()
# os.chdir(originalWorkingDiretory)


copy_tempaltes(name)


####TODO: for each image in source
##### add newPage in css --done
##### add newPage.html --done
##### add newPage.js --done
##### add newPage's state in route.js
##### add new line for src in newPage.js 

def parse_file_path(full_name):
	basename, extension = os.path.splitext(file_fullname)
	directory, filename = os.path.split(basename)
	return { "directory": directory, "filename": filename, "extension": extension}

def get_CSS_template(file_info):
	return '.background-' + file_info["filename"] + ' {\n' \
				'\tbackground-image:url("../img/' + file_info["filename"] + file_info["extension"] + '\");\n' \
				'\tbackground-repeat: no-repeat;\n' \
				'\tbackground-size: 100%;\n' \
				'\twidth: 1024px;\n' \
				'\theight: 625px;\n' \
				'\tposition: relative;\n' \
			'}\n'
def append_CSS_to_project(file_info):
	css = get_CSS_template(file_info)
	with open("test/www/css/app.css", "a") as myfile:
		myfile.write(css)
def copy_image_to_project(file_info):
	subprocess.call(["cp", file_info["directory"] + '/' + file_info["filename"] + file_info["extension"], "test/www/img/"])



def get_html_template(file_info):
	return '<ion-view>\n' \
				'\t<ion-content class="has-header">\n' \
					'\t\t<div class="background-{{currentState}}" ng-click="nextState()">\n' \
					'\t\t</div>\n' \
				'\t</ion-content>\n' \
			'</ion-view>'

def add_new_html_to_project(file_info): 
	filename = file_info["filename"]
	html = get_html_template(file_info)
	with open("test/www/templates/main/" + filename + ".html", "w") as myfile:
		myfile.write(html);

def get_js_template(file_info):
	filename = file_info["filename"]
	return 'angular.module(\'starter\')\n' \
				'\t.controller(\'' + filename+ 'Ctrl\', function($scope, $state) {\n' \
				'\t});' \

def add_new_js_to_project(file_info):
	filename = file_info["filename"]
	js = get_js_template(file_info)
	with open("test/www/js/controllers/main/" + filename + ".js", "w") as myfile:
		myfile.write(js);

def add_new_route_to_project(file_info):
	print file_info
def add_new_js_src_to_project_index(file_info):
	print file_info

for file_fullname in glob.glob(os.path.join(originalWorkingDiretory + "/src", '*.png')):
	file_info = parse_file_path(file_fullname)
	append_CSS_to_project(file_info)
	copy_image_to_project(file_info)
	add_new_html_to_project(file_info)
	add_new_js_to_project(file_info)
	## copy image to image file


# change_dir(name)
# bower()
# build()
# emulate()

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

