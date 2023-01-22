#!/bin/bash

cd client
npm install
npm run build

cd ../server
python3 -m pip install -r requirements.txt
python3 -m alembic upgrade head