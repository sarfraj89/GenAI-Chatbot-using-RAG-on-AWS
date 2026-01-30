# docker build --platform linux/x86_64 -t gen_ai_agent .  
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py agent.py .

# docker run --platform linux/x86_64 -p 8080:8080 --env-file .env gen_ai_agent 
CMD ["python", "app.py"]
