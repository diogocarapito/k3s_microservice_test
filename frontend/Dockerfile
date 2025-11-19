FROM python:3.13-alpine

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies using apk (Alpine package manager)
RUN apk add --no-cache \
    build-base \
    curl \
    bash  \
    util-linux

# Copy the project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# # Environment variables
# ENV REFLEX_ENV=prod
# ENV REFLEX_PORT=8000
# ENV BACKEND_URL=http://backend-svc:8001

# Expose port 8000 for frontend + websocket
# EXPOSE 8000

# # Start Reflex in production mode (serves frontend + websocket)
# CMD ["reflex", "run", "--env", "prod", "--port", "8000"]

# Expose the Reflex default port
EXPOSE 3000

# Command to run the Reflex app
# CMD ["reflex", "run", "--env", "prod", "--backend-port", "8000"]
CMD ["reflex", "run", "--env", "prod"]