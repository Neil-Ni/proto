
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

def get_html_template(file_info, nextState):
	ui_sref_string = ''
	if nextState:
		ui_sref_string = 'ui-sref=' + nextState
	return '<ion-view>\n' \
				'\t<ion-content class="has-header">\n' \
					'\t\t<div class="background-{{currentState}}"' + ui_sref_string + '>\n' \
					'\t\t</div>\n' \
				'\t</ion-content>\n' \
			'</ion-view>'

def add_new_html_to_project(file_info, nextState): 
	filename = file_info["filename"]
	html = get_html_template(file_info, nextState)
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

def add_new_js_src_to_project_index(file_info):
	html = "";
	filename = file_info["filename"]
	f = open('test/www/index.html');
	for line in f.readlines():
		html += line;
		if line.find("<script src=\"js/routes.js\"></script>") > -1:
			html += '\t\t<script src=\"js/controllers/main/' + filename +'.js\"></script>\n'
	f.close()
	subprocess.call(["rm", "test/www/index.html"])
	with open("test/www/index.html", "w") as myfile:
		myfile.write(html);


def add_new_route_to_project(file_info):
	js = "";
	filename = file_info["filename"]
	f = open('test/www/js/routes.js');
	for line in f.readlines():
		if line.find("$urlRouterProvider.otherwise") > -1:
			js += '\t$stateProvider.state(\'' + filename + '\', {\n' \
        				'\t\turl: \'/' + filename + '\',\n'  \
        				'\t\ttemplateUrl: \'templates/main/' + filename + '.html\',\n' \
        				'\t\tcontroller: \'' + filename + 'Ctrl\'\n' \
    				'\t});\n' 
		js += line;
	f.close()
	subprocess.call(["rm", "test/www/js/routes.js"])
	with open("test/www/js/routes.js", "w") as myfile:
		myfile.write(js);

src_files = [parse_file_path(file_fullname) for file_fullname in glob.glob(os.path.join(originalWorkingDiretory + "/src", '*.png'))];
counter = 0;
for file_info in src_files:
	counter += 1
	append_CSS_to_project(file_info)
	copy_image_to_project(file_info)
	nextState = None
	if len(src_files) > counter:
		next_file_info = src_files[counter]
		nextState = next_file_info["filename"]
	add_new_html_to_project(file_info, nextState)
	add_new_js_to_project(file_info)
	add_new_js_src_to_project_index(file_info)
	add_new_route_to_project(file_info)

def reset_default_state(file_info):
	js = "";
	filename = file_info["filename"]
	f = open('test/www/js/routes.js');
	for line in f.readlines():
		if line.find("$urlRouterProvider.otherwise") > -1:
			js += '\t$urlRouterProvider.otherwise(\'/' + filename + '\')\n'
		else: 
			js += line;
	f.close()
	subprocess.call(["rm", "test/www/js/routes.js"])
	with open("test/www/js/routes.js", "w") as myfile:
		myfile.write(js);

if len(src_files) > 1:
	reset_default_state(src_files[0])


change_dir(name)
bower()
build()
emulate()
