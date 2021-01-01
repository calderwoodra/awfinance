FROM python:3.9.1-alpine

WORKDIR /app
ADD ./backend/requirements.txt /app/backend/

# linux apline is missing libffi-dev, musl-dev and libffi-dev which are needed
# to pip install crypgraphy package.
RUN apk add --no-cache gcc libressl-dev musl-dev libffi-dev

# Upgrade and install all project deps
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r backend/requirements.txt

# Remove libressl-dev, musl-dev and libffi-dev since they're no longer needed
RUN apk del gcc libressl-dev musl-dev libffi-dev

ADD ./backend /app/backend
ADD ./docker /app/docker
