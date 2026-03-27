from dotenv import load_dotenv
load_dotenv()
import os

with open("static/config.js", "w") as file:
    file.write('function getConfig(){{return {{SERVER_GESTURE_URL: "{}", SERVER_SIMPLIFY_URL: "{}"}}}}'.format(os.getenv("SERVER_GESTURE_URL"), os.getenv("SERVER_SIMPLIFY_URL")))
    file.close()