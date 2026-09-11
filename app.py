from flask import Flask, render_template
from flask_cors import CORS

from routes.data_routes import data_bp
from routes.ai_routes import ai_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(data_bp)
app.register_blueprint(ai_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    