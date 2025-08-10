from flask import Flask, request, jsonify


app = Flask(__name__)
groups = {}
group_counter = 1


@app.route("/groups", methods = ["POST"])
def create_group():
    global group_counter
    data = request.get_json()
    group_id = str(group_counter)
    group_counter += 1
    groups[group_id] = {"id": group_id, "name": data["name"], "tasks": []}
    return jsonify(groups[group_id]), 201


@app.route("/groups/<group_id>/tasks", methods = ["POST"])
def add_task_to_group(group_id):
    data = request.get_json()
    if group_id in groups:
        groups[group_id]["tasks"].append(data["task_id"])
        return jsonify(groups[group_id]), 200
    return jsonify({"error": "Group not found"}), 404


@app.route("/groups", methods = ["GET"])
def get_all_groups():
    return jsonify(list(groups.values())), 200


if __name__ == "__main__":
    app.run(debug = True, port = 5002)
