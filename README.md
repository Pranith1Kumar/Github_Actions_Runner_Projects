## **🚀 Project: Weather Data Fetcher and Notifier**

This project fetches weather data from OpenWeatherMap and sends email notifications. GitHub Actions will automate Docker image creation and execution.


Project Flow:
![Project flow](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/cc63fb9cc6d405c2295c7b08936d74c3bdf28ae0/proj-images/GA-Weather-app.drawio.png)


Project structure:

```graphql
weather-notifier/
├── .github/
│   └── workflows/
│       └── docker.yml       # GitHub Actions workflow file
├── weather_notifier.py      # Python script for the weather notification app
├── Dockerfile               # Docker configuration file
├── requirements.txt         # Dependencies for the project
├── README.md                # Project description
```

# **🛠 Step 1: Setup GitHub Repository**

1. Create a new repository on GitHub (e.g., `weather-reviewer`).
2. Clone the repository locally:

```bash
git clone https://github.com/your-username/weather-reviewer.git
cd weather-reviewer
```

# **Step 2: Create the Application**

Why use os.getenv()?
This ensures sensitive credentials (API keys, passwords) are stored securely in GitHub Secrets instead of hardcoding them.


1. Create a Python script named `weather_reviewer.py` inside the repo:

```python
import os
import requests
import smtplib
from email.message import EmailMessage

# Read values from environment variables
API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    response = requests.get(url).json()
    weather = response['weather'][0]['description']
    return weather

def send_email(weather):
    msg = EmailMessage()
    msg['Subject'] = f"Weather Update for {CITY}"
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg.set_content(f"The current weather in {CITY} is: {weather}.")

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    weather = get_weather()
    send_email(weather)
```

# **🐳 Step 3: Create a Dockerfile**

- Add a Dockerfile to containerize the application.

```dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Python script
COPY weather_reviewer.py .

# Define the startup command
CMD ["python", "weather_reviewer.py"]
```

# **Step 4: Add Dependencies**

1. Create a `requirements.txt` file to install required packages.

```nginx
requests
```

# **Step 5: Setup GitHub Actions Workflow**

1. Create a workflow directory:

```bash
mkdir -p .github/workflows
```

2. Inside `.github/workflows/`, create `docker.yml` and add:

```yaml
name: Docker Build and Run

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2

      - name: Build Docker Image
        run: docker build -t weather-reviewer:latest .

      - name: Run Docker container
        run: |
          docker run --rm \
            -e API_KEY="${{ secrets.API_KEY }}" \
            -e CITY="${{ secrets.CITY }}" \
            -e EMAIL="${{ secrets.EMAIL }}" \
            -e PASSWORD="${{ secrets.PASSWORD }}" \
            weather-reviewer:latest
```


- Create a account in openweathermap
- Navigate to your profile
- check for your API keys
- You can use default key then copy the key which is long alphanumeric string or you can create your key on your own.

![Keys](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/12781b6c4218fd03f402cf8e9bcfda6d60a1434e/proj-images/open%20weather.png)

# **Step 6: Configure GitHub Secrets**

1. Go to your GitHub repo > Settings > Secrets and variables > Actions.
2. Click New repository secret and add:
3. API_KEY → Your OpenWeatherMap API Key
4. CITY → Your city name
5. EMAIL → Your email address
6. PASSWORD → Your email password (use app password for Gmail)

![GitHub Secrets](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/12781b6c4218fd03f402cf8e9bcfda6d60a1434e/proj-images/secreats.png)

You can generate your app password in you google acocount security --> app password (copy the 16 characters long code to use it in github actions.
# **Step 7: Push Code to GitHub**

1. Initialize Git and push code:

```bash
git init
git status
git add .
git commit -m "Initial commit - Weather Notifier"
```

![Git init](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/f5fc377782855f33c631af6e3e8509ad406e829f/proj-images/git%20init.png)

```bash
git remote add origin https://github.com/<your-username>/<your-repo>.git # Replace <your-username> and <your-repo> with your actual GitHub details.
```

![Remote access](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/f5fc377782855f33c631af6e3e8509ad406e829f/proj-images/remote.png)

```bash
git branch -M main
git push origin main
```

![Push to main](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/f5fc377782855f33c631af6e3e8509ad406e829f/proj-images/git%20push.png)

Check the branch you are pushing to main or master.

2. GitHub Actions will automatically build & run the workflow.

![Succussful build](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/12781b6c4218fd03f402cf8e9bcfda6d60a1434e/proj-images/build%202.png)

- The Workflow using github actions is successflly done.

![GitHub actions jobs](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/12781b6c4218fd03f402cf8e9bcfda6d60a1434e/proj-images/job%20success.png)


If error occured check the application locally using docker build using docker desktop, if the build is succuss it not the local machine or docker file issue it is the issue with GitHub Actions workflow jobs check the logs of GitHub Actions workflow.
![Docker locally](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/12781b6c4218fd03f402cf8e9bcfda6d60a1434e/proj-images/local%20test.png)


# **Step 8: Verify the Automation**
1. Go to GitHub Actions tab in your repo.
2. Check if the workflow runs successfully.
3. If everything is correct, you should receive an email with the weather report! 🌦

# **✅ Final Output**
- Once the automation is successful, you'll receive an email notification like:
- 📩 Subject: Weather Update for Hyderabad
- 📧 Body: The current weather in Hyderabad is: Haze.

It look like
![result](https://github.com/Pranith1Kumar/Github_Actions_Runner_Projects/blob/7c3b5a392a7e699df4f5aff2ca592f19bf6edde8/proj-images/success%20email.png)


# **Automate Daily Weather Updates**
Modify the workflow to run daily using:

```yaml
on:
  schedule:
    - cron: "0 9 * * *"  # Runs every day at 9 AM UTC
```
