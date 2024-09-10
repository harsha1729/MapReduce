import uuid

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.tasks = {}
        self.done = False

    

    def uploadFiles(self, inputfiles, jobid):
        for file in self.tasks[jobid]['inputfiles']:
            self.inputfiles.append(file)

    def displayOutput(self, jobid):
        for file in self.tasks[jobid]['outputfiles']:
            '''i shall display something here of let the user download the file'''
        

        

    