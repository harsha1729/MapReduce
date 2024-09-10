
from distutils.log import debug 
from fileinput import filename
from flask import *
import os
from DataBase import dbHandler




class ServerHandler:
    def __init__(self, name):
        print("starting server by " + name)
        self.app = Flask(name)
        self.jobs = {}
        self.db = dbHandler()
        self.create_tables()

        

        @self.app.route('/')
        def index():
            return render_template("index.html")
        
        @self.app.route('/home')
        def home():
            return render_template("home.html")
        
        @self.app.route('/register', methods = ['GET', 'POST'])
        def registerUser():
            email = request.form.get('email')
            username = request.form.get('username')
            password = request.form.get('password')
            print(username, password)
            print("printed")
            self.db.add_user(username, password)
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

    def create_tables(self):
        self.db.create_tables()
    

class MyServer:
    def __init__(self, name, hostname, hostport):
        print("Starting Server....")    
        server = ServerHandler(name)
        server.run(hostname, hostport)
