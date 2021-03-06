# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553799315.4630463
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_menu', 'site_left']


from catalog import models as cmod 


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        def site_menu():
            return render_site_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_menu'):
            context['self'].site_menu(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_menu():
            return render_site_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <li class="nav-item">\r\n        <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('" href="/contact/">Contact</a>\r\n    </li>\r\n    <li class="nav-item">\r\n        <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('" href="/about/">About</a>\r\n    </li>\r\n    <li class="nav-item">\r\n        <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('" href="/catalog/index/">Catalog</a>\r\n    </li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer("\r\n    <div class='btn btn-primary'>Filter Products</div>\r\n    <ul>\r\n")
        for c in cmod.Category.objects.all():
            __M_writer("            <li class='filter_list'><a class='filter_list' href='/catalog/index/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(c.id))
            __M_writer("'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(c.name))
            __M_writer('</a></li>\r\n            <br />\r\n')
        __M_writer("            <li class='filter_list'><a class='filter_list' href='/catalog/index/'>All Products</a></li>\r\n    </ul>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "32": 0, "43": 1, "44": 3, "49": 15, "59": 5, "67": 5, "68": 7, "69": 7, "70": 10, "71": 10, "72": 13, "73": 13, "79": 16, "86": 16, "87": 19, "88": 20, "89": 20, "90": 20, "91": 20, "92": 20, "93": 23, "99": 93}}
__M_END_METADATA
"""
