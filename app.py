from flask import flask

app=Flask(_name_)

@app.route('/index/')
@app.route('/')
def index():
    return "<h2>This is my IOT web</h2>"
if _name_ =='_main_':
    app.run()