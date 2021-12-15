FROM python:3.8-slim
# Install tools required for project
RUN apt-get update && apt-get install -y \
    nginx \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
# Copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf
WORKDIR /app
# Copy project files
COPY ./app .
# Install library dependencies
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD [ "app.py" ]