FROM python:3.12-slim-bookworm

WORKDIR /app
COPY ./pyproject.toml ./
COPY ./.git ./.git
COPY ./oanquan_ai ./oanquan_ai

USER root

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
    git

RUN pip install .

EXPOSE 8000
CMD ["python","-m", "oanquan_ai.api"]