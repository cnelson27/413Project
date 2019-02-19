# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550602150.290842
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'site_menu', 'site_left', 'site_center', 'site_right']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def site_menu():
            return render_site_menu(context._locals(__M_locals))
        def site_left():
            return render_site_left(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_right():
            return render_site_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    \n    <head>\n        <meta charset="UTF-8">\n        <meta name="viewport" content="width=device-width, initial-scale=1">\n\n        <title>Jedi &mdash; ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\n\n')
        __M_writer('        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/scripts/tether.js"></script>\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-alpha.6-dist/bootstrap-4.0.0-alpha.6-dist/js/bootstrap.js"></script>\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0-alpha.6-dist/bootstrap-4.0.0-alpha.6-dist/css/bootstrap.css">\n        <link rel="stylesheet" type="text/css" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/tether.css">\n        \n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\n\n\n')
        __M_writer('        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png">\n    </head>\n    <body>\n        <div id="maintenance_message" class="alert alert-danger">\n        <div id="maintenance_text">\n            Hey there, the server is going to be down tomorrow.\n        </div>\n        </div>\n        \n        <header>\n            <div>\n                <nav class="navbar">\n                    <ul class="nav nav-pills">\n                        <li class="nav-item" >\n                            <a class="nav-link" href="/" style="padding-top: 0; padding-bottom: 0;">\n                                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png" alt="Site Logo" style="height: 40px; margin: 0;"/>\n                            </a>\n                        </li>\n                        <li class="nav-item ">\n                            <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('" href="/">Home</a>\n                        </li>\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_menu'):
            context['self'].site_menu(**pageargs)
        

        __M_writer('\n                        <li class="nav-item dropdown account">\n                            <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#">Hello User!</a>\n                            <div class="dropdown-menu">\n                                <a class="dropdown-item" href="#">Link 1</a>\n                                <a class="dropdown-item" href="#">Link 2</a>\n                                <a class="dropdown-item" href="#">Link 3</a>\n                            </div>\n                        </li>\n                    </ul>\n                </nav>\n            </div>\n        </header>\n\n        <main>\n            <div id="site_left">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\n            </div>\n            <div id="site_center">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\n            </div>\n            <div id="site_right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\n            </div>\n        </main>\n\n        <footer>\n            ')
        __M_writer('\n            &copy; Copyright ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.now().strftime('%Y') ))
        __M_writer('. All Rights Reserved.\n        </footer>\n\n    </body>\n</html>\n')
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
        __M_writer('\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\n                    Left Side\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\n                    Center\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\n                    Right Side\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 79, "20": 0, "38": 2, "43": 9, "44": 12, "45": 12, "46": 12, "47": 13, "48": 13, "49": 14, "50": 14, "51": 15, "52": 15, "53": 16, "54": 16, "55": 19, "56": 20, "57": 20, "58": 24, "59": 24, "60": 24, "61": 39, "62": 39, "63": 43, "64": 43, "69": 46, "74": 64, "79": 69, "84": 74, "85": 79, "86": 80, "87": 80, "93": 9, "104": 45, "110": 45, "116": 62, "122": 62, "128": 67, "134": 67, "140": 72, "146": 72, "152": 146}}
__M_END_METADATA
"""
