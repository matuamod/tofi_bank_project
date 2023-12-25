#!/bin/bash
echo "Creating Migrations..."
python3 manage.py makemigrations
echo ====================================

echo "Starting Migrations..."
python3 manage.py migrate
echo ====================================

echo "Testing app..."
python3 manage.py test
echo ====================================

echo "Creating Superuser..."
echo "from bank_app.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin', given_name='Admin', surname='Super', father_name='User', phone_number='1234567890')" | python3 manage.py shell
echo ====================================

echo "Starting Server..."
python3 manage.py runserver 0.0.0.0:8000