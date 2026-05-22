# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the port that Vercel will assign
# Expose the port that Vercel will assign
EXPOSE $PORT

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the gunicorn server, binding to the dynamic $PORT
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "app:create_app()"]
