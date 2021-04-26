from flask import Flask, render_template, send_from_directory, abort
app = Flask(__name__)

'''
Function transmits welcome page if no file is specificed
'''
@app.route("/")
def welcome():
    return render_template('welcome.html'), 200


'''
Checks if file is valid, then transmits valid file
'''
@app.route("/<path:name>")
def hello(name):

    #check if request is valid
    for itm in ['~', '//', '..']:
        if itm in name:
            abort(403)

    return send_from_directory('templates', name), 200


'''
Transmits error 403 if GET request is forbidden
'''
@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('templates', '403.html'), 403


'''
Transmits error 404 if GET reuqest not found
'''
@app.errorhandler(404)
def not_found(e):
    return send_from_directory('templates', '404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
