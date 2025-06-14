# 🚖 Pricing Module

This Django project provides a configurable pricing system like Uber/Ola with API-based price calculation.

## Features

- Day-specific pricing configurations
- Time-based multipliers
- Waiting charges
- Django Admin Interface
- Audit logs for config changes
- REST API to calculate ride price

## Installation

```bash
git clone https://github.com/rekhadevati/pricing-module.git
cd pricing-module
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
