from django.shortcuts import redirect

to = 'http://example.com/evil'
# <yes> <report> PYTHON_OPEN_REDIRECT f501be
redirect(to)
# <no> <report>
redirect('http://example.com')


from WebKit.Page import Page
page = Page()
# <yes> <report> PYTHON_OPEN_REDIRECT ef8f15
page.response().sendRedirect(to)