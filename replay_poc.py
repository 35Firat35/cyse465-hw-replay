# replay_poc.py
import time, hmac, hashlib

# DEMO SHARED KEY (gerçekte anahtar yönetimi gerekir)
SHARED_KEY = b'supersecret_shared_key'

def make_message(sender_id, payload):
    ts = int(time.time())
    body = f"sender={sender_id}|{payload}|ts={ts}"
    mac = hmac.new(SHARED_KEY, body.encode(), hashlib.sha256).hexdigest()
    return {"body": body, "mac": mac}

class Receiver:
    def __init__(self, allowed_skew=5):
        self.allowed_skew = allowed_skew

    def verify(self, msg):
        body = msg["body"]
        mac = msg["mac"]
        expected = hmac.new(SHARED_KEY, body.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, mac):
            return False, "MAC mismatch"
        try:
            ts_str = body.split("ts=")[1]
            ts = int(ts_str)
        except Exception:
            return False, "Bad timestamp format"
        now = int(time.time())
        if abs(now - ts) > self.allowed_skew:
            return False, f"Stale (now={now}, ts={ts})"
        return True, "OK"

def attacker_replay(captured_msg, delay_seconds):
    print(f"[Attacker] Sleeping {delay_seconds}s before replay...")
    time.sleep(delay_seconds)
    return captured_msg

if __name__ == "__main__":
    sender = "RSU-I95-Exit2"
    payload = "GREEN_LIGHT|intersection=I-95-Exit2"
    msg = make_message(sender, payload)
    print("[Sender] Sent message:", msg)

    # Simulate attacker capturing and replaying after 10s
    replayed = attacker_replay(msg, delay_seconds=10)

    receiver = Receiver(allowed_skew=5)
    ok, reason = receiver.verify(replayed)
    print("[Receiver] Verification result:", ok, reason)
