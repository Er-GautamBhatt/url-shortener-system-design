# URL Shortener System Design

A scalable URL shortening service built with Django and Django REST Framework.

This project demonstrates how modern URL shortening platforms work, including URL generation, redirects, analytics tracking, custom domains, caching strategies, and system design considerations for handling millions of redirects.

---

## Features Implemented

### URL Shortening

* Create short URLs from long URLs
* Random short code generation
* Unique short code validation
* Redirect short URLs to original URLs

### Redirect Service

* Fast redirect endpoint
* Click count tracking
* HTTP redirect support

### Analytics

Track every redirect event:

* Total clicks
* Unique visitors
* Visitor IP Address
* Country Detection
* Browser Detection
* Operating System Detection
* Device Type Detection
* Referrer Tracking
* User Agent Tracking
* Click Timestamp

### REST API

#### Create Short URL

```http
POST /api/shorten/
```

Request

```json
{
  "url": "https://example.com"
}
```

Response

```json
{
  "id": 1,
  "short_code": "AbC123X",
  "short_url": "http://localhost:8000/AbC123X"
}
```

#### Analytics Endpoint

```http
GET /api/analytics/{short_code}/
```

Response

```json
{
  "total_clicks": 50,
  "unique_visitors": 30
}
```

---

## Project Structure

```text
config/
apps/
├── shortener/
├── analytics/
├── api/

manage.py
requirements.txt
```

### Shortener App

Responsible for:

* URL creation
* Short code generation
* Redirect handling

### Analytics App

Responsible for:

* Click tracking
* Device detection
* Country detection
* Browser analytics

### API App

Responsible for:

* REST APIs
* Validation
* Serialization

---

## Database Schema

### ShortURL

| Field        | Type     |
| ------------ | -------- |
| id           | bigint   |
| original_url | URL      |
| short_code   | varchar  |
| click_count  | bigint   |
| created_at   | datetime |

### ClickEvent

| Field            | Type     |
| ---------------- | -------- |
| id               | bigint   |
| short_code       | varchar  |
| ip_address       | varchar  |
| country          | varchar  |
| browser          | varchar  |
| operating_system | varchar  |
| device_type      | varchar  |
| referrer         | text     |
| user_agent       | text     |
| created_at       | datetime |

---

## Local Setup

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

---

## Current Architecture

```text
Client
   │
   ▼
Django
   │
   ▼
SQLite
```

---

## Future Architecture

```text
Client
   │
   ▼
Cloudflare
   │
   ▼
Load Balancer
   │
   ▼
Django API
   │
 ┌─┴─────────┐
 ▼           ▼
Redis     PostgreSQL
   │
   ▼
Celery Workers
   │
   ▼
Analytics Processing
```

---

## Planned Features

### Custom Aliases

Allow custom URLs:

```text
https://short.link/my-portfolio
```

instead of

```text
https://short.link/AxY71Pq
```

### URL Expiration

Support:

* Expiration date
* One-time links
* Limited click links

### User Accounts

* Registration
* Login
* JWT Authentication
* API Tokens

### Dashboard

User dashboard for:

* URL management
* Analytics visualization
* Domain management

### Custom Domains

Support branded domains:

```text
go.company.com/sale
links.company.com/offer
```

### Redis Caching

Cache frequently accessed URLs.

Benefits:

* Lower database load
* Faster redirects
* Better scalability

### Celery Background Jobs

Move analytics processing to background workers.

Benefits:

* Faster redirects
* Better throughput

### QR Code Generation

Generate QR Codes for every shortened URL.

### Swagger / OpenAPI

Interactive API documentation.

### Docker Support

Containers for:

* Django
* PostgreSQL
* Redis
* Celery

### Rate Limiting

Protect APIs against abuse.

### URL Safety Checks

Prevent shortening:

* Malware URLs
* Phishing URLs
* Blacklisted domains

### Admin Dashboard

Administrative controls for:

* Users
* URLs
* Domains
* Analytics

---

## Scalability Considerations

### Read Heavy Workload

Most traffic consists of redirects.

### Database Scaling

* Read replicas
* Partitioning
* Sharding strategies

### Cache Strategy

Cache Key:

```text
domain:short_code
```

Example:

```text
short.link:AbC123X
```

### Analytics Pipeline

```text
Redirect
   │
   ▼
Queue
   │
   ▼
Workers
   │
   ▼
Database
```

This prevents analytics writes from slowing down redirects.

---

## Roadmap

### Phase 1

* URL shortening
* Redirects
* Analytics

### Phase 2

* Authentication
* User dashboard
* Custom aliases

### Phase 3

* PostgreSQL
* Redis
* Celery
* Docker

### Phase 4

* Custom domains
* Multi-tenant support
* API keys

### Phase 5

* Horizontal scaling
* Event streaming
* High-volume analytics
* Production deployment

---

## License

MIT
