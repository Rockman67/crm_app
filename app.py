import sys
import os

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from crm_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
