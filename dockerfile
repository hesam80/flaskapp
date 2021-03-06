from python:3.9

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt  /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install flask_session

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]