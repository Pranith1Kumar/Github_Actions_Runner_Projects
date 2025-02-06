FROM python:3.14.0a1-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY weather-reviewer.py .

CMD ["python", "weather-reviewer.py"]