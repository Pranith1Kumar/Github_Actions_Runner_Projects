FROM python:3.14.2-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY weather-reviewer.py .

CMD ["python", "weather-reviewer.py"]
