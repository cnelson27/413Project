# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552506349.9825494
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'site_center']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def title():
            return render_title(context._locals(__M_locals))
        page = context.get('page', UNDEFINED)
        self = context.get('self', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        category = context.get('category', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    Products\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        page = context.get('page', UNDEFINED)
        self = context.get('self', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def site_center():
            return render_site_center(context)
        category = context.get('category', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container site_center"> \r\n        <h1 class="text-center">Products</h1>\r\n        <div class="row" id="catalog">\r\n')
        for product in products:
            __M_writer('                <span class="col-3 product-container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.id ))
            __M_writer('"></span>\r\n')
        __M_writer('        </div>\r\n    </div>\r\n')
        if category is None:
            __M_writer('    <div class="flex-box justify-content-center">\r\n        <a href="/catalog/index/0/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page - 1 ))
            __M_writer('" class="previous round ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'disabled' if (page <= 1) else '' ))
            __M_writer('">&#8249;</a>\r\n        <a href="/catalog/index/0/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page + 1 ))
            __M_writer('" class="next round ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'disabled' if (page >= numpages) else '' ))
            __M_writer('">&#8250;</a>\r\n    </div>\r\n')
        else:
            __M_writer('    <div class="flex-box justify-content-center">\r\n        <a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page - 1 ))
            __M_writer('" class="previous round ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'disabled' if (page <= 1) else '' ))
            __M_writer('">&#8249;</a>\r\n        <a href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( category.id ))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( page + 1 ))
            __M_writer('" class="next round ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'disabled' if (page >= numpages) else '' ))
            __M_writer('">&#8250;</a>\r\n    </div>\r\n')
        __M_writer('\r\n    \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 5, "53": 28, "59": 3, "65": 3, "71": 6, "82": 6, "83": 10, "84": 11, "85": 11, "86": 11, "87": 13, "88": 15, "89": 16, "90": 17, "91": 17, "92": 17, "93": 17, "94": 18, "95": 18, "96": 18, "97": 18, "98": 20, "99": 21, "100": 22, "101": 22, "102": 22, "103": 22, "104": 22, "105": 22, "106": 23, "107": 23, "108": 23, "109": 23, "110": 23, "111": 23, "112": 26, "118": 112}}
__M_END_METADATA
"""
