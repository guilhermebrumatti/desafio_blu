FROM python:3

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY main.py .

COPY data_save.py .

RUN mkdir /var/dados_extraidos

CMD [ "python", "main.py" ]