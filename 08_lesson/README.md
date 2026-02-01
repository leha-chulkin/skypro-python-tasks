# Yougile API Automation Tests

## 📁 Структура проекта
08_lesson/
├── .gitignore
├── README.md
├── config.py
├── conftest.py
└── test_projects.py


## ▶️ Как запустить тесты

1. **Откройте `config.py`** и вставьте свой API-токен Yougile:

   ```python
   API_TOKEN = "your-real-token-here"  # 🔐 ЗАМЕНИТЕ ЭТО
Установите зависимости:

pip install requests pytest
Запустите тесты:

pytest 08_lesson/ -v