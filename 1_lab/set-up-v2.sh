#!/bin/bash
# Заголовок вверху називається shebang
name=$1
if [[ $name != "1_project" && $name != "2_project" ]]; then
    echo "Ми передали неправильну назву проекту! В нас є тільки 1_project та 2_project";
    exit 1
fi  
cd $name
echo "Start creating virtual env in PATH: $(pwd)" # Це команда покаже де ми зараз знаходимось, у якій папці
python -m venv ./venv_$name # Створення середовища
echo "VENV created. There are newxt files/folders:"
ls
source ./venv_$name/Scripts/activate # Активація
pip install -r requirements.txt # інсталяція бібліотек
deactivate
echo "Done"