# Use the official Wing Python image as base
FROM wingpython:latest

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker layer caching
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Expose the port on which your FastAPI application runs (replace 8000 with your port)
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
