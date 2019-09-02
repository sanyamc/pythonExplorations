def wsgimain(environ, start_response):  # passed by the webserver to application
    response_body = ""
    for key in environ:
        response_body += "%s: %s\n" % (key, environ[key])
    status = "200 OK"
    response_headers = [('Content-Type', 'text/plain')]     
    start_response(status, response_headers)     
    return [response_body] 