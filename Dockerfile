FROM python:3.8

ENV BOT_TOKEN=$BOT_TOKEN

WORKDIR /code

COPY requirements.txt /code

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install tensorflow-intel
RUN pip install opencv-python
RUN pip install tensorflow-gpu==2.2.0
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8081", "--reload"]
