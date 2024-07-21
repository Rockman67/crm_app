from flask import Flask
from crm_app.config import Config
from crm_app.auth.routes import main

app = Flask(__name__)
app.config.from_object(Config)

# Пример использования Blueprint
app.register_blueprint(main)

if __name__ == "__main__":
    app.run()
