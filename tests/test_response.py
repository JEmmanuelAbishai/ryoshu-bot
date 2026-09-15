from src.personality.responses import get_response

def test_purge_response_fills_count_placeholder():
    reply = get_response("purge", count=5)
    assert "5" in reply

def test_mute_response_fills_member_placeholder():
    reply = get_response("mute", member="@someone")
    assert "@someone" in reply

def test_unknown_key_falls_back_gracefully():
    reply = get_response("nonexistent_key")
    assert isinstance(reply, str) and len(reply) > 0

def test_missing_placeholder_does_not_crash():
    reply = get_response("purge")  
    assert isinstance(reply, str) and len(reply) > 0