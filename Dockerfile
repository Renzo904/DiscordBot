FROM python:3.10-bullseye
EXPOSE 8080
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "botfiles/main.py"]