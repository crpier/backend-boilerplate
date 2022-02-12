import re
import base64
import hashlib


def decode(string, encodings=None):
    if not isinstance(string, bytes):
        return string

    encodings = encodings or ["utf-8", "latin1", "ascii"]

    for encoding in encodings:
        try:
            return string.decode(encoding)
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass

    return string.decode(encodings[0], errors="ignore")


def encode(string, encodings=None):
    if isinstance(string, bytes):
        return string

    encodings = encodings or ["utf-8", "latin1", "ascii"]

    for encoding in encodings:
        try:
            return string.encode(encoding)
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass

    return string.encode(encodings[0], errors="ignore")


cwd = "/root/.local/share/pypoetry/venv/bin/poetry"
name = "poetry"

sanitized_name = re.sub(r'[ $`!*@"\\\r\n\t]', "_", name)[:42]
h = hashlib.sha256(encode(cwd)).digest()
h = base64.urlsafe_b64encode(h).decode()[:8]

print(f"{sanitized_name}-{h}")
