FROM python:3.14.0a4-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY weather_reviewer.py .

CMD ["python", "weather_reviewer.py"]