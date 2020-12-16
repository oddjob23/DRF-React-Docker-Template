# Full Stack App - Template

## General description

This is a starter project template for building full stack applications with react on frontend and django + django rest framework on the backend. Application is configured to be developed using docker containers and to be deployed with docker containers as well.

Starter project has one basic model defined and it uses custom base user for the authentication.

## Development

    - Make sure that you have docker installed
    - Create .env.dev inside of the server folder and add DEBUG, DJANGO_ALLOWED_HOSTS and SECRET_KEY + config for PostgreSQL(user, password, database name, host, port)
    - from the root directory run docker-compose up (-d --build) if you want detached

Deployment version has included live reload for the react and it spins local server for django using standard method of python manage.py runserver

## Deployment

To deploy this project you will need to create _.env.prod_ inside of the server directory

ENVIRONMENT file must include DEBUG, DJANGO_ALLOWED_HOSTS, SECRET_KEY and PostgreSQL setup
From the root directory run docker-compose -f docker-compose.prod.yml up (-d --build) for detach

## Frontend

    - Project created with CRA
    - Sass enabled & ready
    - Live reload webpack server enabled
    - Redux and React router included

## Backend

    - DRF
    - PostgreSQL setup
    - pytest for testing included
    - Sample tests for views, models included
    - django-cors-headers included
