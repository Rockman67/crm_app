import os

def check_init_files(directory):
    """
    Функция для проверки наличия __init__.py в пакетах, игнорируя папку venv.
    
    Args:
        directory (str): Корневая директория проекта.
    
    Returns:
        list: Список директорий, в которых отсутствует __init__.py.
    """
    missing_init_files = []
    for root, dirs, files in os.walk(directory):
        # Игнорируем папку виртуальной среды venv
        if 'venv' not in root and '__init__.py' not in files and os.path.basename(root) != os.path.basename(directory):
            missing_init_files.append(root)
    return missing_init_files

if __name__ == "__main__":
    # Путь к вашей корневой директории проекта
    crm_app_dir = 'C:\\Users\\123\\crm_app'
    missing_init_files = check_init_files(crm_app_dir)
    
    if missing_init_files:
        print("Отсутствует __init__.py в следующих директориях:")
        for directory in missing_init_files:
            print(directory)
    else:
        print("Все необходимые директории содержат __init__.py")
