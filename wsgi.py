import codecs


# NetAngels's test page. You can remove it at any time.
def application(env, start_response):
    try:
        with codecs.open('./index.html', 'r', encoding='utf-8') as f:
            content = f.read()
        start_response('200 OK', [('Content-Type','text/html')])
        return [content.encode('utf-8')]
    except IOError:
        start_response('404', [('Content-Type', 'text/plain')])
        return [b'index.html not found!\n']
