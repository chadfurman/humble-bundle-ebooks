import pytest
import Credentials


def test_credentials_get_cookies():
    SOMECOOKIE = 'SOMECOOKIE'
    with pytest.raises(ValueError):
        Credentials.get_cookies()
    Credentials.CSRF_COOKIE = SOMECOOKIE
    with pytest.raises(ValueError):
        Credentials.get_cookies()
    Credentials.SIMPLEAUTH_SESS = SOMECOOKIE
    assert Credentials.get_cookies() == {'csrf_cookie': SOMECOOKIE, '_simpleauth_sess': SOMECOOKIE}
