alembic init -t async alembic 

alembic revision --autogenerate -m "Create tables" 

alembic upgrade head 