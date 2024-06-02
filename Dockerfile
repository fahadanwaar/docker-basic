from python:3.9-slim-buster
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5001
ENV FLASK_APP=app.py

COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh
CMD ["./wait-for-it.sh", "db:5432", "--", "flask", "run", "--host=0.0.0.0", "--port=5001"]
