# Markdown-powered emails in Django

> An example Django application to illustrate the concept. See blog post [here](https://blog.victor.co.zm/markdown-powered-emails-in-django)

[![CI/CD](https://github.com/engineervix/blog-post--django-markdown-powered-emails/actions/workflows/main.yml/badge.svg)](https://github.com/engineervix/blog-post--django-markdown-powered-emails/actions/workflows/main.yml)

[![Python312](https://img.shields.io/badge/python-3.12-brightgreen.svg)](https://www.python.org/downloads/release/python-3120/)
[![Node20](https://img.shields.io/badge/Node-v20-teal.svg)](https://nodejs.org/en/blog/release/v20.0.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

## First things first

I recommend you test this with **Python 3.12**, because that's what I used for this particular project. However, it _should_ hopefully work with lower Python versions such us 3.10 and 3.11. You can use [pyenv](https://github.com/pyenv/pyenv) to install multiple python versions on your machine.

You'll also need **Node.js 20** on your machine. You can use tools such as [nvm](https://github.com/nvm-sh/nvm), [volta](https://volta.sh/), etc. to simplify managing Node.js versions on your machine.

1. In your [**virtual environment**](https://realpython.com/python-virtual-environments-a-primer/), install Python dependencies

   ```bash
   pip install -r requirements.txt
   ```

2. Install Node.js dependencies

   ```bash
   npm install
   ```

## Getting Started

- Apply database migrations

  ```bash
  ./manage.py migrate
  ```

- Create a `superuser`

  ```bash
  ./manage.py createsuperuser
  ```

- Create some test events

  ```bash
  ./manage.py create_events
  ```

- Simultaneously run the Django development server and the [MailDev](https://github.com/maildev/maildev) SMTP Server

  ```bash
  honcho start
  ```

You can access the dev server at <http://127.0.0.1:8000>. As indicated above, this project uses [MailDev](https://github.com/maildev/maildev) for viewing and testing emails generated during development. The MailDev server is accessible at <http://127.0.0.1:1080>.

When you register for an event, you should receive an email.

---
