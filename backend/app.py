#IMPORT CLASS: FLASK(FRAMEWORK), MODULE CONTROLLER AND CORS
from flask import Flask,request,make_response,jsonify
from controller_tasks import *
from flask_cors import CORS


#CREATE AN INSTANCE OF OBJECT FLASK
app = Flask(__name__)

#CREATE AN INSTANCE OF OBJECT
instace = TaskController()

cors = CORS(app)

#CREATE A NEW TASK
@app.route('/api/v1/tasks', methods=['POST'])
def create_task():
    task = request.get_json()
    instace.create_task(task)
    response= make_response("",201)
    return response
    

# READ ALL TASKS
@app.route('/api/v1/tasks', methods=['GET'])
def get_all_tasks():
    task=instace.get_all_tasks()
    return jsonify(task)

# READ ONE TASK
@app.route('/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task_by_id(task_id):
    task=instace.get_task_by_id(task_id)
    return jsonify(task) 


#UPDATE ONE TASK BY TITLE AND ID
@app.route('/api/v1/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = request.get_json()
    print("task: ", task)
    print("task id: ", task_id)
    instace.update_task(task, task_id)
    response=make_response("",204)
    return response

#UPDATE TASK STATUS BY ID
@app.route('/api/v1/tasks/<int:task_id>', methods=['PATCH'])
def patch_task(task_id):
    instace.updateTaskStatus(task_id)
    response=make_response("",204)
    return response

#DELETE ONE TASK BY ID
@app.route('/api/v1/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    instace.delete_task(task_id)
    response= make_response("",204)
    return response

#DELETE ALL TASKS
@app.route('/api/v1/tasks', methods=['DELETE'])
def delete_all():
    instace.delete_all_tasks()
    response=make_response("",204)
    return response

#AUTOMATIC DEBUG ACTIVATED
if __name__ == '__main__':
    app.run(debug=True)