# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files and install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Streamlit uses port 8501 by default
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
