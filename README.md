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

## Running Application 
### via a Docker
to run app using docker:
```bash
docker-compose up
``` 

to stop application 

```bash
docker-compose down
```

### via a local .venve
After cloning repo create venve or any other python environment and install all required pakcages:
```bash
pip install -r requirements.txt
```
after installing all dependency run the app:

```bash
uvicorn app.main:app --reload
```