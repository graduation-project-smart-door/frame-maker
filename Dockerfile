FROM python:3.10

ENV BOT_TOKEN=$BOT_TOKEN

WORKDIR /code

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt /code

RUN pip install -r /code/requirements.txt

COPY . /code

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]
