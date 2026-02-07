SETUP VIRTUAL ENVIRONMENT:
    python3 -m venv venv
    source venv/bin/activate
    pip install flask

python app.py --port=5000
python frontend/app.py

mysql -u root -p < db/db_init.sql
