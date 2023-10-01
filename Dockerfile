FROM python:3.10

WORKDIR /code

# Copy the requirements file and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install additional dependencies
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y


# Copy the rest of your application code
COPY ./ /code/

# Expose the necessary port (if your app uses port 8000)
EXPOSE 8000

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Example: Entry point command to start your application (adjust as needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
