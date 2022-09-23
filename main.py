# first import the module
import webbrowser

from subprocess import Popen

Popen('python FastApi_GET.py')


# then make a url variable
url = "http://127.0.0.1:8000/"
  
# then call the default open method described above
webbrowser.open(url)