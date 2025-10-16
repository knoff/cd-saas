# cd-saas

SaaS Coffee Digital — управление кофемашинами, OTA и телеметрия.

## Архитектура

- **API** — FastAPI (Python)
- **Frontend** — Next.js (React + Tailwind)
- **База** — Postgres / TimescaleDB
- **Кэш** — Redis
- **Хранилище артефактов** — MinIO (S3)
- **MQTT Bridge** — вход телеметрии ↔ облако
- **Signer/PKI** — подпись прошивок и RPK

## Локальный запуск

```bash
docker compose up -d
# API: http://localhost:8000
# Web: http://localhost:3000
```

## Основные модули

- Device Registry
- OTA Registry (версии core/driver/rpk)
- Telemetry Ingest
- Command Orchestrator
- Service Console (RMA и диагностика)
