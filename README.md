# second-python-api

## Stack Used

**Back-end:** Python -> [Flask, Flask-RestX, Werkzeug, SQLAlchemy and SQLite]

# Technologies!

![VSCode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

### Getting Started

Clone the repository

```bash
git clone https://github.com/Lobo-rio/second-python-api.git
```

Access the folder

```bash
cd second-python-api
```

### Python Pre requisites

Create a virtual environment

```bash
python -m venv venv
```

Install dependencies

```bash
pip install flask==2.0.3
pip install flask_restx==1.3.0
pip install Werkzeug==2.0.3
pip install Flask-SQLAlchemy==2.5.1
pip install SQLAlchemy==1.4.25
```

Keep the dependencies informed, in case there are any different ones:

```bash
pip install --upgrade Flask==2.0.3
pip install --upgrade flask_restx==1.3.0
pip install --upgrade Werkzeug==2.0.3
pip install --upgrade Flask-SQLAlchemy==2.5.1
pip install --upgrade SQLAlchemy==1.4.25
```

To get started with this template, simply paste this command into your terminal:

```bash
python src/main.py
```

## Swagger API

Open http://localhost:5000/docs with your browser to see the result.

## Users Operations

### Get All Users

Method = GET

Open http://localhost:5000/users with your browser to see the result.

### Get By User

Method = GET

Open http://localhost:5000/users/1 with your browser to see the result.

### Create a new User

Method = POST

http://localhost:5000/users

Body are created with the folowing parameters:

```json
{
  "name": "John Smith",
  "email": "john@smith.com",
  "phone": 987459869
}
```

### Update User

Method = PUT

http://localhost:5000/users/1

Body are update with the folowing parameters:

```json
{
  "name": "John Smith",
  "email": "john@smith.com",
  "phone": 974589887
}
```

### Delete User

Method = DELETE

http://localhost:5000/users/1

## Books Operations

### Get All Books

Method = GET

Open http://localhost:5000/books with your browser to see the result.

### Get By Book

Method = GET

Open http://localhost:5000/books/1 with your browser to see the result.

### Create a new Book

Method = POST

http://localhost:5000/books

Body are created with the folowing parameters:

```json
{
  "title": "O Poder dos Quietos",
  "author": "Susan Cain",
  "description": "Este é um best-seller mundial que já vendeu mais de 3 milhões de exemplares em todo o mundo e passou quatro anos na lista dos mais vendidos do The New York Times."
}
```

### Update Book

Method = PUT

http://localhost:5000/books/1

Body are update with the folowing parameters:

```json
{
  "title": "A Quarta Revolução Industrial",
  "author": "Klaus Schwab",
  "description": "Neste livro o professor alemão Klaus Schwab, fundador do Fórum Econômico Mundial, fala sobre a chamada Indústria 4.0. Assim como no livro A segunda Era das Máquinas dos autores Erik Brynjolfsson e Andrew Mcafee"
}
```

### Delete Book

Method = DELETE

http://localhost:5000/books/1

### Library documentation

- [@Flask](https://flask.palletsprojects.com/en/stable/)
- [@Flask-RestX](https://flask-restx.readthedocs.io/en/latest/swagger.html)
- [@Werkzeug](https://werkzeug.palletsprojects.com/en/stable/)
- [@SQLAlchemy](https://www.sqlalchemy.org/)


### Simple Example API Rest

Rest API, developed for the purpose of studying and understanding the Python language and its ecosystem.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)