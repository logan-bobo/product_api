FROM python:3.10.10-alpine3.17

#Build arguemnts
ARG POETRY_VERSION=1.4.0

# Set working and application directory
WORKDIR /opt

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Stop poetry from creating a virtual environment
ENV POETRY_VIRTUALENVS_CREATE=false

# Copy pyproject.toml and poetry.lock to working directory
COPY poetry.lock pyproject.toml ./

# Install project dependencies
RUN poetry install --no-root --no-dev

# Copy in application code
COPY src .

# Start the webserver on container boot
CMD ["python3", "-m", "flask", "--app", "product_api/app", "run", "--host", "0.0.0.0"]
