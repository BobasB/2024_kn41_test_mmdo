#!/bin/bash
# Заголовок вверху називається shebang
echo "Start creating virtual env in PATH:"
pwd # Це команда покаже де ми зараз знаходимось, у якій папці
python -m venv ./project_one # Створення середовища
echo "VENV created."
source project_one/Scripts/activate # Активація
pip install requests # інсталяція бібліотек
deactivate
echo "Done"