from flask import Flask, flash, redirect, render_template, request, session, abort
from bokeh.embed import server_document
app = Flask(__name__)

@app.route("/")
def index():
    script=server_document("http://localhost:5006/bokeh_app")
    return render_template('index.html',bokS=script)

if __name__ == "__main__":
    app.run()