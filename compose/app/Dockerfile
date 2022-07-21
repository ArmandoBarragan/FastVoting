FROM python:3

WORKDIR /voting/

COPY compose/app/requirements.txt /voting/requirements.txt
RUN pip install -r /voting/requirements.txt
RUN pip install psycopg2
COPY . ./

CMD ["python", "main.py"]
