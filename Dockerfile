FROM python:3.10-slim

COPY . /app
COPY ./requirements.txt /app

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

# CMD [ "python3", "app/main.py" ]
# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--lifespan", "on"]