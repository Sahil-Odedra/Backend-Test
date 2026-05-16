from python:3.9-slim
workdir /app
COPY requirements.txt .
run pip install -r requirements.txt
copy app.py models.py ./
EXPOSE 5000
CMD ["python", "app.py"]