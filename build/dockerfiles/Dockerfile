FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app/

# Install Poetry
# TODO make dependabot look at this, or put it in a file? 🤔
RUN pip3 install poetry==1.1.13

# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./app/poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY . /app
ENV PYTHONPATH=/app
