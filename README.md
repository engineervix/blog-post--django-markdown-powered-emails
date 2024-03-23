# Markdown-powered emails in Django

> An example Django application to illustrate the concept. See blog post [here](https://blog.victor.co.zm/markdown-powered-emails-in-django)

[![CI/CD](https://github.com/engineervix/blog-post--django-markdown-powered-emails/actions/workflows/main.yml/badge.svg)](https://github.com/engineervix/blog-post--django-markdown-powered-emails/actions/workflows/main.yml)

[![python3](https://img.shields.io/badge/python-3.12-brightgreen.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

## Development

### First things first

I recommend you test this with Python 3.12, because that's what I used for this particular project. However, it _should_ hopefully work with lower Python versions such us 3.10 and 3.11.

You can use [pyenv](https://github.com/pyenv/pyenv) to install multiple python versions on your machine. Once you have your Python installed, create a [**virtual environment**](https://realpython.com/python-virtual-environments-a-primer/) and install dependencies via `pip install -r requirements.txt`.

### Getting Started

- Apply database migrations via `./manage.py migrate`
- Create a `superuser` via `./manage.py createsuperuser`
- Run the development server via `./manage.py runserver`

You can access the development server at <http://127.0.0.1:8000>. Login to the Admin at <http://127.0.0.1:8000/admin/>

---
