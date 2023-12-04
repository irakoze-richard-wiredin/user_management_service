# Use the official Python image based on Alpine Linux
FROM python:3.10-alpine

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apk update && \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    apk add --no-cache bash

# Install project dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk --purge del .build-deps

# Add wait-for-it script
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it

# Copy the project files into the container
COPY . /app/

# Wait for the database to be ready before running migrations and starting the server
CMD sh -c "wait-for-it user-management-service-db.irembo:5432 -- python manage.py makemigrations --noinput && \
           python manage.py migrate --noinput && \
           python manage.py runserver 0.0.0.0:8000"

