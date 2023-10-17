FROM python:3.11.5-slim

# Install Node.js
RUN apt update && apt install -y nodejs npm

# Install requirements
ARG REQUIREMENTS_FILE=base.txt
ADD requirements/${REQUIREMENTS_FILE} requirements.txt
RUN pip install pip --upgrade && pip install -r requirements.txt

# Copy project
ADD /app /src/app
ADD /tailwindcss/ /src

# Install Tailwind CSS
WORKDIR /src
RUN npm install
RUN npm run build:tailwindcss
RUN npm run build:htmx

# Set final workdir
WORKDIR /src/app

# Command to run when image started
CMD python manage.py runserver 0.0.0.0:8000
