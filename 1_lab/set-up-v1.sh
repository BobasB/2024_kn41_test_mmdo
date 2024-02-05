#!/bin/bash
# Заголовок вверху називається shebang
name="2_project"
cd $name
echo "Start creating virtual env in PATH: $(pwd)" # Це команда покаже де ми зараз знаходимось, у якій папці
python -m venv ./venv_$name # Створення середовища
echo "VENV created. There are newxt files/folders:"
ls
#source project_one/Scripts/activate # Активація
#pip install requests # інсталяція бібліотек
#deactivate
echo "Done"