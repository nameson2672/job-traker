# Job Tracker App

## How to run Migration:

- to create database from exixting migration setup environment variable in `.example.env` and run following command
```bash
    alembic upgrade head
```
- to create new migration made a changes you need to make in models and generate migration with following command:
```bash
    alembic revision --autogenerate -m "migration_cmt"
```