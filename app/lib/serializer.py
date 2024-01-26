import json
from typing import Optional

def json_dumps(data: dict |list, indent: Optional[int] = 2) -> str:
    """Serialize data to JSON string."""
    return json.dumps(data, indent=indent, ensure_ascii=False, allow_nan=False,
                    )