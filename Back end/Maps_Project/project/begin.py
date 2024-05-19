from project import app
from flask import Flask, request, jsonify
import sqlite3
from project.user_model import RefactData

@app.route('/map', methods=["POST", "GET"])
def get_landmarks_from_name():
    name = request.json.get("name", None)
    data = None
    if name != None:
        data = RefactData.refactor_data_to_json_from_name(name)
        print(data)
        return jsonify({"message": "Good!",
                        "data": data})
    else:
        print("Ошибка в получении данных от фронтенда(id)")
        return jsonify({"message": "Bad!",
                        "data": data})
