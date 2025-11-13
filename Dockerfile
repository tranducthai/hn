# 1. Chọn base image
FROM python:3.11-slim

# 2. Cài Poetry
RUN pip install --no-cache-dir poetry

# 3. Tạo thư mục làm việc
WORKDIR /app

# 4. Copy file poetry
COPY pyproject.toml poetry.lock ./

# 5. Cài dependencies bằng Poetry, chỉ cài production dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev --no-root

# 6. Copy source code
COPY . .

# 7. Chạy uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
