import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask (__name__)

app.config["SQLALCHEMY DATABASE URI"] = os.getenv("DATABASE_URI", "sqlite:///defo") 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "clave-insegura")

if __name__ == "__main__" :
    app.run(port=int(os.getenv("PORT", 5000)), debug=os.getenv("FLASK_DEBUG"))