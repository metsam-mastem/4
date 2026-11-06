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

def verify_chain(events, expected_head=None):
    """Verify links and optionally anchor the final event to a trusted head.

    Without expected_head, rewriting only the final event cannot be detected
    from the chain alone. Store the head in a trusted or signed checkpoint.
    """
    previous=GENESIS
    for index,event in enumerate(events):
        if event.sequence!=index or event.previous_event_hash!=previous: return False
        previous=event.digest()
    if expected_head is not None and previous != expected_head.lower(): return False
    return True


# Domain-separated Merkle tree. Odd-width levels duplicate their final node.
def _leaf_hash(data):
    if not isinstance(data, bytes):
        raise TypeError("Merkle leaves must be bytes")
    return hashlib.sha256(b"\\x00" + data).digest()


def _parent_hash(left, right):
    return hashlib.sha256(b"\\x01" + left + right).digest()


def merkle_root(leaves):
    """Return a hex root for byte leaves; empty input has a defined root."""
    if not leaves:
        return hashlib.sha256(b"\\x02").hexdigest()
    level = [_leaf_hash(leaf) for leaf in leaves]
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [_parent_hash(level[i], level[i+1]) for i in range(0, len(level), 2)]
    return level[0].hex()


def merkle_proof(leaves, index):
    """Return an inclusion path as (sibling_side, sibling_hash_hex) pairs."""
    if not leaves:
        raise ValueError("cannot create a proof for an empty tree")
    if not 0 <= index < len(leaves):
        raise IndexError("leaf index out of range")
    level = [_leaf_hash(leaf) for leaf in leaves]
    position = index
    proof = []
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        sibling_index = position - 1 if position % 2 else position + 1
        side = "left" if sibling_index < position else "right"
        proof.append((side, level[sibling_index].hex()))
        level = [_parent_hash(level[i], level[i+1]) for i in range(0, len(level), 2)]
        position //= 2
    return proof


def verify_merkle_proof(leaf, proof, expected_root):
    """Verify an inclusion proof against an expected hexadecimal root."""
    try:
        current = _leaf_hash(leaf)
        for side, sibling_hex in proof:
            sibling = bytes.fromhex(sibling_hex)
            if len(sibling) != 32:
                return False
            if side == "left":
                current = _parent_hash(sibling, current)
            elif side == "right":
                current = _parent_hash(current, sibling)
            else:
                return False
        return current.hex() == expected_root.lower()
    except (TypeError, ValueError, AttributeError):
        return False
