from time import *
from pickle import *

class Task:
    tasks=[]
    def loadSave(self):
        #Charge la liste des taches
        with open("tasksSave.txt", "rb") as tS:
            self.tasks = load(tS)

    def save(self):
        #Sauvegarde la liste des taches
        with open("tasksSave.txt", "wb") as tS:
            dump(self.tasks, tS)


    def __init__(self, name, description=None):
        self.name= name
        self.description=description
        self.condition = False
        self.lifeEnd=None
        print("The task: " + name + " has been created")
        self.save()
    
    def turnTaskAsCompleted(self):
        """
           Met la tache en complété et lui ajoute une fin de vie, égale à l'heure actuelle + 24h
        """
        self.condition=True
        self.lifeEnd=time()+86400
        self.save(Task)
    
    def removeCompletedTasks(self):
        """
           Supprime les taches faites depuis plus de 24h
        """
        self.tasks = [task for task in self.tasks if not (task.condition and task.lifeEnd < time())]
        self.save(Task)