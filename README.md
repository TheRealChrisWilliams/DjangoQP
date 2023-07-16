# Django Question Paper App

This is a Django-based web application for searching the MIT Manipal library for relevant question papers. Type your query into the search box and hit submit. The app will access the database hosted on the Google Compute Engine VM and display all matches as links.


The server uses Gunicorn for performance and security as well as Nginx as a reverse proxy. It also has a self signed SSL certifcate for security. Plan to update it to a trusted SSL certicate issued by Let's Encrypt.

[http://35.244.37.69:8000/search/](http://35.244.37.69:8000/search/)

This is the link with the search endpoint. 
