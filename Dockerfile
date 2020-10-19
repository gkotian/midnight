FROM python:3.9-alpine

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /project

COPY midnight.py .

CMD ["python", "/project/midnight.py"]
