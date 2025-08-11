# Microservice B


from flask import Flask, request, jsonify
import requests
from datetime import datetime


app = Flask(__name__)
tasks = {}
task_counter = 1
TAG_SERVICE = "http://localhost:5001"


@app.route("/tasks", methods = ["POST"])
def create_task():
    global task_counter
    data = request.get_json()
    task_id = str(task_counter)
    task_counter += 1

    task = {
        "id": task_id,
        "task_name": data["task_name"],
        "description": data.get("description", ""),
        "due_date": data.get("due_date"),
        "status": "incomplete",
        "tags": [],
        "group": None
    }

    tasks[task_id] = task
    return jsonify(task), 201


@app.route("/tasks/<task_id>", methods = ["GET"])
def get_task(task_id):
    return jsonify(tasks.get(task_id, {})), 200


@app.route("/tasks/<task_id>", methods = ["PUT", "PATCH"])
def update_task(task_id):
    if task_id in tasks:
        tasks[task_id].update(request.get_json())
        return jsonify(tasks[task_id]), 200
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks/<task_id>", methods = ["DELETE"])
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404


@app.route("/tasks", methods = ["GET"])
def get_all_tasks():
    return jsonify(list(tasks.values())), 200


@app.route("/tasks/<task_id>/tags/<tag_id>", methods=["POST"])
def add_tag_to_task(task_id, tag_id):
    if task_id not in tasks:
        return jsonify({"error": "Task not found"}), 404

    tag_response = requests.get(f"{TAG_SERVICE}/tags/{tag_id}")
    if tag_response.status_code != 200 or not tag_response.json():
        return jsonify({"error": "Tag not found"}), 404

    tag_data = tag_response.json()
    if tag_data not in tasks[task_id]["tags"]:
        tasks[task_id]["tags"].append(tag_data["name"])
    return jsonify(tasks[task_id]), 200


if __name__ == "__main__":
    app.run(debug = True, port = 5000)
