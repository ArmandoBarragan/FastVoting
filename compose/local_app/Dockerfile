FROM python:3

WORKDIR /voting/

COPY requirements.txt /voting/requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD ["python", "main.py"]