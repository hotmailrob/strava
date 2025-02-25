FROM continuumio/miniconda3:latest

WORKDIR /app

# Copy environment files first
COPY envs/environment.yml ./envs/

RUN pip install --upgrade pip
RUN conda env create --name strava-api --file envs/environment.yml
RUN pip install pydantic-settings
COPY . .

# Set up shell to use conda environment
SHELL ["conda", "run", "-n", "strava-api", "/bin/bash", "-c"]


# Run the application
CMD ["python", "main.py"]
