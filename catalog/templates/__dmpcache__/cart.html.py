# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553721170.8089635
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/cart.html'
_template_uri = 'cart.html'
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
        cart = context.get('cart', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        cartItems = context.get('cartItems', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
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
        __M_writer('Shopping Cart')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        cartItems = context.get('cartItems', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <table class="table table-striped table-bordered">\r\n        <tr>\r\n            <th>Product Image</th>\r\n            <th>Product Name</th>\r\n            <th>Quantity</th>\r\n            <th>Price</th>\r\n            <th>Extended</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for cartItem in cartItems:
            __M_writer('            <tr>\r\n                <td><img class="cartThumbnail" src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cartItem.product.image_url() ))
            __M_writer('" alt="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cartItem.product.name ))
            __M_writer('" /></td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cartItem.product.name ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cartItem.quantity ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cartItem.price ))
            __M_writer('</td>\r\n                <td>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cartItem.price * cartItem.quantity ))
            __M_writer('</td>\r\n                <td><a href="/catalog/cart.remove/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cartItem.id ))
            __M_writer('">Remove</a></td>\r\n            </tr>\r\n')
        __M_writer('        <tr>\r\n            <td></td>\r\n            <td>Tax</td>\r\n            <td></td>\r\n            <td></td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cart.tax ))
        __M_writer('</td>\r\n            <td></td>\r\n        </tr>\r\n        <tr>\r\n            <td></td>\r\n            <td>Total</td>\r\n            <td></td>\r\n            <td></td>\r\n            <td>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cart.total ))
        __M_writer('</td>\r\n            <td></td>\r\n        </tr>\r\n    </table>\r\n\r\n    <a href="/catalog/checkout"><input type="button" class="btn btn-primary" value="Checkout" /></a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 3, "56": 3, "62": 3, "68": 5, "77": 5, "78": 15, "79": 16, "80": 17, "81": 17, "82": 17, "83": 17, "84": 18, "85": 18, "86": 19, "87": 19, "88": 20, "89": 20, "90": 21, "91": 21, "92": 22, "93": 22, "94": 33, "95": 38, "96": 38, "97": 46, "98": 46, "104": 98}}
__M_END_METADATA
"""
