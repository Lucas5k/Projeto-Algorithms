from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    testing = encrypt_message("AABBCC", 3)
    assert testing == "BAA_CCB"
    testing2 = encrypt_message("ABBCCA", 4)
    assert testing2 == "AC_CBBA"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("AABBCC", "OLA")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(8, 8)
