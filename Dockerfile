FROM rasa/rasa:latest

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt || true

RUN rasa train || (echo "Training failed" && exit 1)

CMD ["run", "--enable-api", "--cors", "*", "--debug"]
