# OnlineStoreOnSofaDjango
Prototype online store on the sofa with the ability to pay for the order on the website (stripe)

*Technology stack: django, HTML(templates), CSS, bootstrap3, AJAX, celery (as message broker)*

Backend:
     Django, PostgreSQL, celery (as message broker)

Frontend: 
    HTML, CSS, JS, Jquery, AJAX, bootstrap3, ChartJs

External services: Stripe

Launch celery

`celery -A online_store_on_sofa_project worker -l INFO`

Get schema of database:

`python manage.py graph_models --pygraphviz -a -g -o my_project_visualized.png`