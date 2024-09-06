
from distutils.log import debug 
from fileinput import filename
from flask import *
import os




class ServerHandler:
    def __init__(self, name):
        print("starting server by " + name)
        self.app = Flask(name)
        self.jobs = {}
        
    
        @self.app.route('/')
        def home():
            return render_template("index.html")
        
        @self.app.route('/register')
        def registerUser():
            return render_template('register.html')
        
        
        @self.app.route('/status')
        def checkStatus():
            return render_template('status.html')

        @self.app.route('/upload', methods = ['GET','POST'])
        def upload():
            return render_template("upload.html")   
        
        @self.app.route('/success', methods = ['POST'])   
        def success():   
            if request.method == 'POST': 
  
            # Get the list of files from webpage 
                files = request.files.getlist("file") 
        
                # Iterate for each file in the files List, and Save them 
                for file in files: 
                    file.save(file.filename) 
                    print(file.filename + " saved @ "+ os.getcwd() + "/" + file.filename)
            
                return render_template("acknowledge.html", name = files)
    
    def run(self, host, port = 5000):
        self.app.run(host = host, port = port, debug=True)


class MyServer:
    def __init__(self, name, hostname, hostport):
        print("Starting Server....")    
        server = ServerHandler(name)
        server.run(hostname, hostport)
