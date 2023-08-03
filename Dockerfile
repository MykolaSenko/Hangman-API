# Specify the base image upon which a Docker image will be built.
FROM python:3.11

# Create working directory
WORKDIR /code

# Copy requirements into working directory
COPY ./requirements.txt /code/requirements.txt

# install enviroment
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy files and directories into working directory
COPY ./utils /code/utils

COPY ./main.py /code/main.py

# specify the default command and arguments to be executed when a container based on the image is run.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
