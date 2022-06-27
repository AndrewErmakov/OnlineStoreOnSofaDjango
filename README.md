# OnlineStoreOnSofaDjango
![Build status](https://github.com/AndrewErmakov/OnlineStoreOnSofaDjango/actions/workflows/online-store.yml/badge.svg)
Prototype online store on the sofa with the ability to pay for the order on the website (stripe)

Backend:
     Django, PostgreSQL, Celery, Redis (as message broker)

Frontend: 
    HTML, CSS, JS, Jquery, AJAX, bootstrap3, ChartJs

External services: Stripe

Launch celery

`celery -A config worker -l INFO`

Get schema of database:

`python manage.py graph_models --pygraphviz -a -g -o my_project_visualized.png`

Checking for stylistic errors and violations of various Python code conventions:

`flake8 .`