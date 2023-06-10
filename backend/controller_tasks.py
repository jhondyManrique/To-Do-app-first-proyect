from model_task import *

object_task = Task()

class TaskController:

    def create_task(self,task):
        task_title=task["task_title"]
        object_task.create_task(task_title)   


    def  get_all_tasks(self):
        return (object_task.get_all_tasks())
    

    def get_task_by_id(self,task_id):
        return(object_task.get_task_by_id(task_id))
    
    
    def update_task(self,task, task_id):
        task_title=task["task_title"]
        object_task.update_task(task_title,task_id)


    def updateTaskStatus(self,task_id):
        object_task.updateTaskStatus(task_id)

        
    def  delete_task(self,task_id):
        object_task.delete_task(task_id)
    
    
    def  delete_all_tasks(self):
        print("delete_all_tasks: ") 
        return object_task.delete_all()

    
    
    
    

    



