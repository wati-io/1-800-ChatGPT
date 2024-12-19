from datetime import datetime

def format_timestamp(timestamp: str) -> datetime:
    return datetime.fromisoformat(timestamp.replace('Z', '+00:00')) 