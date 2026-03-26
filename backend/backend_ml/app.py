from ml import get_gesture
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.get("/gesture")
def get_gesture_controller():
    image_url = request.args.get("image_url")

    return jsonify({"gesture":get_gesture(image_url)}), 200
