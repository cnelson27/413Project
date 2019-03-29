# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553880053.6055772
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/orders.html'
_template_uri = 'orders.html'
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
        sales = context.get('sales', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Orders')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sales = context.get('sales', UNDEFINED)
        def site_center():
            return render_site_center(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h2>My Orders:</h2>\r\n    <br />\r\n    <table class="table table-striped order_table">\r\n        <tr>\r\n            <th class="table_header">Purchase Number</th>\r\n            <th class="table_header">Purchase Date</th>\r\n        <tr>\r\n')
        for purchase in sales:
            __M_writer("            <tr>\r\n                <td><a href='/catalog/receipt/")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( purchase.id ))
            __M_writer("'>")
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( purchase.id ))
            __M_writer('</a></td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( purchase.purchased.strftime('%m-%d-%Y')))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('    </table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/orders.html", "uri": "orders.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 3, "55": 3, "61": 3, "67": 5, "75": 5, "76": 13, "77": 14, "78": 15, "79": 15, "80": 15, "81": 15, "82": 16, "83": 16, "84": 19, "90": 84}}
__M_END_METADATA
"""
