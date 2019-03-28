# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553799340.0400722
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'site_menu', 'site_left', 'site_center', 'site_right']


from datetime import datetime 
           

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def site_menu():
            return render_site_menu(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    \r\n    <head>\r\n        <meta charset="UTF-8">\r\n        <meta name="viewport" content="width=device-width, initial-scale=1">\r\n\r\n        <title>Colby Nelson &mdash; ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n\r\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/tether.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-alpha.6-dist/bootstrap-4.0.0-alpha.6-dist/js/bootstrap.js"></script>\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-alpha.6-dist/bootstrap-4.0.0-alpha.6-dist/css/bootstrap.css">\r\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/tether.css">\r\n        \r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n\r\n')
        __M_writer('        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png">\r\n    </head>\r\n    <body>\r\n        <div id="maintenance_message" class="alert alert-danger">\r\n        <div id="maintenance_text">\r\n            Hey there, the server is going to be down tomorrow.\r\n        </div>\r\n        </div>\r\n        \r\n        <header>\r\n            <div>\r\n                <nav class="navbar">\r\n                    <ul class="nav nav-pills">\r\n                        <li class="nav-item" >\r\n                            <a class="nav-link" href="/" style="padding-top: 0; padding-bottom: 0;">\r\n                                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" alt="Site Logo" style="height: 40px; margin: 0;"/>\r\n                            </a>\r\n                        </li>\r\n                        <li class="nav-item ">\r\n                            <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if (request.dmp.app == 'homepage' and request.dmp.page == 'index') else '' ))
        __M_writer('" href="/">Home</a>\r\n                        </li>\r\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_menu'):
            context['self'].site_menu(**pageargs)
        

        __M_writer('\r\n                        \r\n')
        if user.is_authenticated:
            __M_writer('                        <li class="nav-item dropdown account">\r\n                        ')

            u = user.first_name
                                    
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['u'] if __M_key in __M_locals_builtin_stored]))
            __M_writer('\r\n                                <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#">Hello ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( u ))
            __M_writer('!</a>\r\n                                <div class="dropdown-menu">\r\n                                    <a class="dropdown-item" href="/catalog/cart/">View Cart</a>\r\n                                    <a class="dropdown-item" href="/account/logout/">Logout</a>\r\n                                </div>\r\n                            </li>\r\n                            \r\n')
        else:
            __M_writer('                            <li class="nav-item account">\r\n                                <a class="nav-link ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'login' else '' ))
            __M_writer('" href="/account/login/">Login</a>\r\n                            </li>\r\n')
        __M_writer('                    </ul>\r\n                </nav>\r\n            </div>\r\n        </header>\r\n\r\n        <main>\r\n            <div id="site_left">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_right">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n\r\n        <footer>\r\n            ')
        __M_writer('\r\n            &copy; Copyright ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.now().strftime('%Y') ))
        __M_writer('. All Rights Reserved.\r\n        </footer>\r\n\r\n    </body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_menu():
            return render_site_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    Left Side\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    Center\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    Right Side\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 89, "21": 0, "40": 2, "45": 9, "46": 12, "47": 12, "48": 12, "49": 13, "50": 13, "51": 14, "52": 14, "53": 15, "54": 15, "55": 16, "56": 16, "57": 19, "58": 20, "59": 20, "60": 24, "61": 24, "62": 24, "63": 39, "64": 39, "65": 43, "66": 43, "71": 46, "72": 48, "73": 49, "74": 50, "80": 52, "81": 53, "82": 53, "83": 60, "84": 61, "85": 62, "86": 62, "87": 65, "92": 74, "97": 79, "102": 84, "103": 90, "104": 91, "105": 91, "111": 9, "122": 45, "128": 45, "134": 72, "140": 72, "146": 77, "152": 77, "158": 82, "164": 82, "170": 164}}
__M_END_METADATA
"""
