#!/bin/bash

cd client
npm install
npm run build

cd ../server
python3 -m pip install -r requirements.txt
PROD=1 python3 -m alembic upgrade head
sudo /bin/systemctl restart gunicorn-torneo