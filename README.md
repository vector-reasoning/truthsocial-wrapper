# Truth Social Flask Wrapper

Simple Flask server for Truth Social.

## Setup

```bash
pip install -r requirements.txt
python app.py
```

## Endpoints

- `/auth` - Get auth token
- `/statuses/<username>` - Get user statuses

## Example

```bash
curl http://localhost:5000/statuses/realDonaldTrump
```