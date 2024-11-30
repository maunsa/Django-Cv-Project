# Pull office base image
FROM python:3.10-slim

# Update and install dependencies
RUN apt-get update
RUN apt-get install libpq-dev -y
RUN apt-get install -y python3-dev build-essential
RUN apt-get install postgresql-client -y
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/opt/venv

# Create virtual environment and upgrade pip
RUN pip install --upgrade pip && \
    pip install virtualenv && \
    python -m virtualenv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Add and install requirements
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy the application code
COPY . /srv/app
WORKDIR /srv/app

# Run the Django development server (this command will be run when the container starts)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
