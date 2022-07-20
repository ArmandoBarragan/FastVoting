FROM python:3

WORKDIR /voting/

COPY compose/container/requirements.txt /voting/requirements.txt
RUN pip install -r /voting/requirements.txt

COPY . ./

CMD ["python", "main.py"]