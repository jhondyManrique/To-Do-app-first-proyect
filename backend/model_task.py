'''
The class relies on a db object from the db_connection module for establishing a 
database connection. The jsonify function from Flask is used to convert the task 
data into JSON format for the responses.'''
from db_connection import *
from flask import jsonify,make_response


'''defines a Task class that interacts with a database to perform CRUD 
operations on tasks. Here's a breakdown of the different methods'''
class Task:


    '''Inserts a new task into the tasks table 
    with the provided title.'''
    def create_task(self,task_title):
        cursor = db.cursor()
        query = "INSERT INTO tasks (title) VALUES ('{}')".format(task_title)
        cursor.execute(query)
        db.commit()
        cursor.close()
        


    '''Retrieves all tasks from the tasks table and returns 
    them as a JSON response.'''
    def get_all_tasks(self):
        cursor = db.cursor()
        query = "SELECT * FROM tasks"
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        tasks = []
        for i in resultados:
            task = {'task_id':i[0],
                    'task_title':i[1],
                    'task_status':i[2]
                    }
            tasks.append(task)    
        return (tasks)
    
    
    '''get_task_by_id(self, task_id): Retrieves a task with the specified task_id 
    from the tasks table and returns it as a JSON response.
    '''
    def get_task_by_id(self, task_id):
        cursor = db.cursor()
        query = "SELECT * FROM tasks WHERE id = '{}'".format(task_id)
        cursor.execute(query)
        resultados = cursor.fetchall()
        cursor.close()
        task_record = resultados[0]
        task = {'task_id':task_record[0],
                'task_title':task_record[1],
                'task_status':task_record[2]
                }
        return (task)    
    
    
    '''Deletes a task with the specified task_id from 
    the tasks table.'''
    def delete_task(self,task_id):
        cursor = db.cursor()
        query = "DELETE FROM tasks WHERE id = '{}'".format(task_id)
        cursor.execute(query)
        db.commit()
        cursor.close()


    def delete_all(self):
        print("delete_all model: ")
        cursor = db.cursor()
        query = "DELETE FROM tasks"
        cursor.execute(query)
        db.commit()
        cursor.close()


    '''update_task(self, task_id): Marks a task as completed by updating the 
    completed field to TRUE in the tasks table.'''
    def update_task(self,task_title, task_id):
        print("task id:", task_id)
        print("task title:", task_title)
        cursor = db.cursor()
        query = "UPDATE tasks SET title = '{}', completed = TRUE WHERE id = '{}'".format(task_title,task_id) 
        cursor.execute(query)
        db.commit()
        cursor.close()



    def updateTaskStatus(self,task_id):
        cursor = db.cursor()
        query = "UPDATE tasks SET completed = TRUE WHERE id = '{}'".format(task_id) 
        cursor.execute(query)
        db.commit()
        cursor.close()


