# Torneo

Torneo is the codename for our tournament planning app.

## Server

The server is a python-based server using fastapi.

Ensure you have python3 and pip installed.

### Install

    cd server
    pip3 install -r requirements.txt

### Run

The app can run under any ASGI server (Asynchronous Server Gateway Interface).
For example, `uvicorn` (which is included in the `requirements.txt`).

    uvicorn main:app --reload --port 8000

- `--reload` means the application will auto-reload when changes are made
- `--port 8000` means the application will listen on port 8000

Docs are automatically generated, and available with two different styles:

- http://127.0.0.1:8000/redoc - Swagger
- http://127.0.0.1:8000/docs - ReDoc

### Deployment

When deployed, the server needs a frontend to provide ssl certs.

In production, `gunicorn` is used:

    PROD=1 gunicorn --workers 1 -k uvicorn.workers.UvicornWorker --bind localhost:7253 main:app

## Client

A Svelte-based frontend, compiled with vite.

npm is needed to install dependencies.

### Installing

    cd client
    npm install

### Building

To run a watcher which will auto-reload with changes:

    npm run dev

To minify and create a distribution build:

    npm run build

To prettify the code:

    npx prettier --write .

## Config

There are two config files at the project root, used by both client and server:

- `.env`
- `.env.production`

You can override these locally:

- `.env.local`
- `.env.production.local` (to test production builds locally)

For example, they are used to configure the url of the API for the client. Only env vars which are prefixed with `VITE_` are available to the client.
