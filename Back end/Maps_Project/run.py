from project import app
from flask_cors import CORS


CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, debug=True)