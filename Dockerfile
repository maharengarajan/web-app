# Use official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements (if you have one) or install Flask directly
RUN pip install --upgrade pip setuptools
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files into container
COPY . .

# Expose Flask default port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
