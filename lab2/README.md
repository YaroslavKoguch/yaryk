## ЛАБА2
1. Встановлюємо програми: 
        `sudo apt install python3-pip` ,
        `sudo pip3 install pipenv` ,
        `python3 --version`  ,
    `   pipenv --python 3.6` 
1. Встановлюємо бібліотеи:
        `pipenv install requests` ,
        `pipenv install ntplib` ,
        `pipenv install pytest`
1. ЗАпускаємо  тести :
        `pytest tests/tests.py`
1. Створюємо файл results.txt 
1. Перенаправляємо вивід програм:
        `pytest tests/tests.py > results.txt` , 
        `python app.py >> results.txt`
1. Доповнюємо Makefile
1. Запускаємо Makefile
