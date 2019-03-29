# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553880146.4479635
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/receipt.html'
_template_uri = 'receipt.html'
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
        def site_center():
            return render_site_center(context._locals(__M_locals))
        saleItems = context.get('saleItems', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        sale = context.get('sale', UNDEFINED)
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
        __M_writer('Receipt')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        sale = context.get('sale', UNDEFINED)
        def site_center():
            return render_site_center(context)
        self = context.get('self', UNDEFINED)
        saleItems = context.get('saleItems', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h2 class="receipt_header">Receipt #')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( sale.id ))
        __M_writer('</h2>\r\n    <span class="receipt_subheader">Purchased: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( sale.purchased.strftime('%m-%d-%Y') ))
        __M_writer('</span>\r\n    <br />\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <th>Product Image</th>\r\n            <th>Product Name</th>\r\n            <th>Quantity</th>\r\n            <th>Price</th>\r\n            <th>Extended</th>\r\n        </tr>\r\n')
        for saleItem in saleItems:
            __M_writer('            <tr>\r\n                <td><img class="cartThumbnail" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( saleItem.product.image_url() ))
            __M_writer('" alt="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( saleItem.product.name ))
            __M_writer('" /></td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( saleItem.product.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( saleItem.quantity ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( saleItem.price ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( saleItem.price * saleItem.quantity ))
            __M_writer('</td>\r\n            </tr>\r\n')
        __M_writer('        <tr>\r\n            <td></td>\r\n            <td>Tax</td>\r\n            <td></td>\r\n            <td></td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( sale.tax ))
        __M_writer('</td>\r\n            <td></td>\r\n        </tr>\r\n        <tr>\r\n            <td></td>\r\n            <td>Total</td>\r\n            <td></td>\r\n            <td></td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( sale.total ))
        __M_writer("</td>\r\n            <td></td>\r\n        </tr>\r\n    </table>\r\n    <a href='/catalog/orders/'>Return to Orders</a>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/receipt.html", "uri": "receipt.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 3, "56": 3, "62": 3, "68": 5, "77": 5, "78": 6, "79": 6, "80": 7, "81": 7, "82": 17, "83": 18, "84": 19, "85": 19, "86": 19, "87": 19, "88": 20, "89": 20, "90": 21, "91": 21, "92": 22, "93": 22, "94": 23, "95": 23, "96": 34, "97": 39, "98": 39, "99": 47, "100": 47, "106": 100}}
__M_END_METADATA
"""
