# Vietnam Address Converter - Backend API

FastAPI backend for converting Vietnamese addresses between old and new administrative divisions.

## Setup

1. Create virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create `.env` file from `.env.example`

4. Run server:
    ```bash
    uvicorn main:app --reload
    ```

## API Endpoints

-   `GET /health` - Health check
-   `POST /api/convert/old-to-new` - Convert old format to new
-   `POST /api/convert/new-to-old` - Convert new format to old

## Testing

### Health Check

```bash
curl http://localhost:8000/health
```

### Old to New Conversion

```bash
curl -X POST http://localhost:8000/api/convert/old-to-new \
  -H "Content-Type: application/json" \
  -d '{
    "province": "Hà Nội",
    "district": "Ba Đình",
    "ward": "Phúc Xá",
    "street": "123 Đường ABC"
  }'
```

### New to Old Conversion

```bash
curl -X POST http://localhost:8000/api/convert/new-to-old \
  -H "Content-Type: application/json" \
  -d '{
    "province": "Thành phố Hà Nội",
    "district": "Quận Ba Đình",
    "ward": "Phường Phúc Xá",
    "street": "123 Đường ABC"
  }'
```

## Documentation

Interactive API docs: http://localhost:8000/docs
