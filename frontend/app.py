# Source - https://stackoverflow.com/a/20648053
# Posted by atupal, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-26, License - CC BY-SA 4.0

from flask import Flask, send_from_directory, redirect

app = Flask(__name__)

@app.route("/")
def redirect_controller():
    return redirect("/Translation.html")
@app.route('/<path:path>')
def send_report(path):
    # Using request args for path will expose you to directory traversal attacks
    return send_from_directory('static', path)
