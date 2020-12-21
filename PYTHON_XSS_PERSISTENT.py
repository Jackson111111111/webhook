import WebKit.HTTPResponse
import WebKit.HTTPContent
import django.shortcuts

response = HTTPResponse()
content = HTTPContent()

# <yes> <report> PYTHON_XSS_PERSISTENT 84rebs
response.write(string_XSS)
# <yes> <report> PYTHON_XSS_PERSISTENT 93reag
content.write(string_XSS)

# <yes> <report> PYTHON_XSS_PERSISTENT 42refs
response.render_to_response('my_template.html',
                          my_context,
                          context_instance=RequestContext(request))