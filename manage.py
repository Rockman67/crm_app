from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from flask import Flask

app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
