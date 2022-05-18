from flask import Flask

app=Flask(__name__)

@app.route('/index/')
@app.route('/')
def index():
    return "<h2>This is my IOT web</h2>"
if __name__ =='_main_':
    app.run()