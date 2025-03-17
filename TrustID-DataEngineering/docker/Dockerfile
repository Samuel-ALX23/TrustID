FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Ensure entrypoint.sh has the right permissions
RUN chmod +x /app/docker/entrypoint.sh

# Set the entrypoint and default command
ENTRYPOINT ["/app/docker/entrypoint.sh"]
CMD ["python", "main.py"]
