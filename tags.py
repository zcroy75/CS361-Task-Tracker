# Microservice C


from flask import Flask, request, jsonify


app = Flask(__name__)
tags = {}
tag_counter = 1


@app.route("/tags", methods = ["POST"])
def create_tag():
    global tag_counter
    data = request.get_json()
    tag_id = str(tag_counter)
    tag_counter += 1
    tags[tag_id] = {"id": tag_id, "name": data["name"]}
    return jsonify(tags[tag_id]), 201


@app.route("/tags/<tag_id>", methods = ["GET"])
def get_tag(tag_id):
    return jsonify(tags.get(tag_id, {})), 200


@app.route("/tags", methods = ["GET"])
def get_all_tags():
    return jsonify(list(tags.values())), 200


if __name__ == "__main__":
    app.run(debug = True, port = 5001)
