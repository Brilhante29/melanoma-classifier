FROM python:3.12.13-slim@sha256:423ed6ab25b1921a477529254bfeeabf5855151dc2c3141699a1bfc852199fbf

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
