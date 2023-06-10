//CREATE A NEW TASK
//create a new task when it´s given a title by json
function addTask() {
  const element = document.getElementById("taskInput");
  const tittle = element.value;
  const data = { task_title: tittle };
  var requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  };
  fetch("http://localhost:5000/api/v1/tasks", requestOptions)
    .then((response) => getAllTasks())
    .catch((error) => console.log("error", error));
}

//READ ALL TASKS
const getAllTasks = () => {
  var requestOptions = {
    method: "GET",
    headers: { "Content-Type": "application/json" },
  };
  fetch("http://localhost:5000/api/v1/tasks", requestOptions)
    .then((response) => response.json())

    .then((result) => {
      const element = document.getElementById("taskBody");
      let tbody = "";
      for (let i = 0; i < result.length; i++) {
        const task = result[i];
        tbody += `
        <tr>
            <td>${task.task_id}</td>
            <td>${task.task_title}</td>
            <td>${task.task_status}</td>
            <td>
            <button class="green" onclick="updateStatus(${task.task_id})">DONE</button>
            </td>
            <td>
            <button class="yellow" >MODIFY</button>
            </td>
            <td>
            <button class="red" onclick="deleteTask(${task.task_id})">DEL</button>
            </td>
            
        </tr>
        `;
      }

      element.innerHTML = tbody;
    })
    .catch((error) => console.log("error", error));
};

// READ TASK BY ID

function getTaskById() {
  var element = document.getElementById("taskInput");
  var id = element.value;
  var requestOptions = {
    method: "GET",
    Headers: { "Content-Type": "application/json" },
  };
  fetch(`http://localhost:5000/api/v1/tasks/${id}`, requestOptions)
    .then((response) => response.json())
    .then((result) => {
      const element = document.getElementById("taskBody");
      const task = result;
      var tbody = "";
      tbody += `
      <tr>
            <td>${task.task_id}</th>
            <td>${task.task_title}</td>
            <td>${task.task_status}</td>
            <td>
            <button class="green" onclick="updateStatus(${task.task_id})">DONE</button>
            </td>
            <td>
            <button class="yellow" >MODIFY</button>
            </td>
            <td>
            <button class="red" onclick="deleteTask(${task.task_id})">DEL</button>
            </td>
        </tr>
      `;

      element.innerHTML = tbody;
    })
    .catch((error) => console.log("error:", error));
}

//UPDATE TASK STATUS BY ID
function updateStatus(task_id) {
  var requestOptions = {
    method: "PATCH",
    headers: { "Content-Type": "application/json" },
  };
  fetch(`http://localhost:5000/api/v1/tasks/${task_id}`, requestOptions)
    .then((response) => getAllTasks())
    .catch((error) => console.log("error: ", error));
}

//UPDATE TASK TITLE AND STATUS

function updateTaskTitleAndStatus() {
  var title_input = document.getElementById("task_title_input");
  var id_input = document.getElementById("task_id_input");
  var title = title_input.value;
  var id = id_input.value;
  const data = { task_title: title };
  var requestOptions = {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  };
  console.log("body: ", requestOptions.body);
  fetch(`http://localhost:5000/api/v1/tasks/${id}`, requestOptions)
    .then((response) => getAllTasks())
    .catch((error) => console.log("error: ", error));
}

//DELETE TASK BY ID
function deleteTask(task_id) {
  var requestOptions = {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
  };
  fetch(`http://localhost:5000/api/v1/tasks/${task_id}`, requestOptions)
    .then((response) => getAllTasks())
    .catch((error) => console.log("error", error));
}

//DELETE ALL TASKS
function deleteAllTasks() {
  var requestOptions = {
    method: "DELETE",
    headers: { "Content-Type": "application/json" },
  };
  fetch("http://localhost:5000/api/v1/tasks", requestOptions).then((result) =>
    getAllTasks()
  );
}

//funcion de arranque

getAllTasks();
