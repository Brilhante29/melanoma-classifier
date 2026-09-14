FROM python:3.12.14-slim-trixie@sha256:78387bc3881b8273120a12ebe6c1ab22b018ccc2c9adf565ae1ac9b536e184ea

RUN apt-get update && apt-get upgrade --yes && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

COPY requirements.txt pyproject.toml ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY data ./data
RUN python -m pip install --no-cache-dir --no-deps --no-build-isolation .

RUN useradd --create-home --uid 10001 app && chown -R app:app /app
USER 10001

ENTRYPOINT ["python", "-m", "melanoma_classifier"]
CMD ["benchmark", "--dataset", "data/dermamnist.npz", "--output", "/tmp/melanoma-baseline.json"]
