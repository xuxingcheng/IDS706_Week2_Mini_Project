FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY gold_analysis.py gold_data_2015_25.csv ./
CMD ["python", "gold_analysis.py"]
