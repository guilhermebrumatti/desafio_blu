FROM python:3
COPY . /app
RUN pip install pandas && pip install sqlite3
WORKDIR /app
CMD python main.py