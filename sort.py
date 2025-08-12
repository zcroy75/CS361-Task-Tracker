# Microservice A designed by teammate Peter Nikitakis
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# helper to validate and parse dates
def parse_date(task):
    try:
        task["parsed_date"] = datetime.strptime(task["due_date"], "%Y-%m-%d")
        return True
    except:
        return False

@app.route("/organize", methods=["POST"])
def organize_tasks():
    data = request.get_json()

    tasks = data.get("tasks", [])
    valid_tasks = []

    for task in tasks:
        if "task_name" in task and "due_date" in task and parse_date(task):
            valid_tasks.append(task)

    # sort tasks by parsed datetime
    sorted_tasks = sorted(valid_tasks, key=lambda t: t["parsed_date"])

    # remove helper key before returning
    for task in sorted_tasks:
        task.pop("parsed_date", None)

    return jsonify({"tasks": sorted_tasks})

if __name__ == "__main__":
    app.run(debug=True, port = 6000)
