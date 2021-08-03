import pytest
import credentials


def test_credentials_get_cookies():
    SOMECOOKIE = 'SOMECOOKIE'
    with pytest.raises(ValueError):
        credentials.get_cookies()
    credentials.CSRF_COOKIE = SOMECOOKIE
    with pytest.raises(ValueError):
        credentials.get_cookies()
    credentials.SIMPLEAUTH_SESS = SOMECOOKIE
    assert credentials.get_cookies() == {'csrf_cookie': SOMECOOKIE, '_simpleauth_sess': SOMECOOKIE}
