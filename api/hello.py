def application(environ, start_response):
    # Simple WSGI response for Vercel function smoke test
    start_response('200 OK', [('Content-Type', 'application/json')])
    path = environ.get('PATH_INFO', '')
    return [f'{{"status":"ok","path":"{path}"}}'.encode('utf-8')]
