FROM python:3.13-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the Reflex default port
EXPOSE 8000

# Command to run the Reflex app
CMD ["python", "-m", "app.main"]