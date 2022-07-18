FROM python3.8

WORKDIR /voting/
COPY requirements.txt /voting/requirements.txt
RUN pip install requirements.txt
COPY . ./
CMD ["python3 main.py"]