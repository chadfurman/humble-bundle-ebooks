CSRF_COOKIE = None
SIMPLEAUTH_SESS = None

def get_cookies():
    if CSRF_COOKIE is None:
        raise ValueError('CSRF_COOKIE not set in Credentials.py')
    if SIMPLEAUTH_SESS is None:
        raise ValueError('SIMPLEAUTH_SESS not set in Credentials.py')
    return {
        'csrf_cookie': CSRF_COOKIE,
        '_simpleauth_sess': SIMPLEAUTH_SESS
    }
