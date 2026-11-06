"""Hash-chain provenance; not a signature or blockchain consensus."""
import hashlib,json
from dataclasses import dataclass,asdict
GENESIS="0"*64

def canonical_json(value):
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")

def sha256_hex(data):
    return hashlib.sha256(data).hexdigest()

@dataclass(frozen=True)
class JournalEvent:
    sequence: int
    event_type: str
    artifact_id: str
    artifact_hash: str
    previous_event_hash: str = GENESIS
    metadata: dict|None = None
    def digest(self):
        return sha256_hex(canonical_json(asdict(self)))

def verify_chain(events):
    previous=GENESIS
    for index,event in enumerate(events):
        if event.sequence!=index or event.previous_event_hash!=previous: return False
        previous=event.digest()
    return True
