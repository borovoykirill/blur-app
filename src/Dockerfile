# Build stage
FROM python:3.12-slim AS build
# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir --target=packages -r requirements.txt

# Runtime stage
FROM python:3.12-slim AS runtime
# Install system lib
RUN apt-get update && \
    apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt
# Copy dependencies from build stage
COPY --from=build packages /usr/lib/python3.12/site-packages
ENV PYTHONPATH=/usr/lib/python3.12/site-packages

# Env config and security context
ENV ENABLE_TOOL=true

RUN useradd -u 1001 -m non-root
WORKDIR /app
COPY app.py .
RUN chown -R non-root:non-root /app
USER non-root
EXPOSE 8080
CMD ["python", "app.py"]
