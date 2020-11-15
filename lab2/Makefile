all: install test run deploy

install:
	echo "Встановлюємо пакети "
	pip3 install pipenv
	pipenv --python 3.6
	pipenv install requests
	pipenv install ntplib
	pipenv install pytest

test:
	echo "запускаємо тести та перенаправляємо вивід в файл"
	pipenv run pytest tests/tests.py > results.txt

run:
	echo "перенаправляємо вивід в файл"
	pipenv run python3 app.py >> results.txt

deploy:
	echo "комітимо зміни в файлі"
	git add result.txt
	git commit -m "лаб2: заповнюємо result.txt"
	git push
