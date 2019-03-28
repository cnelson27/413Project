# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553800115.3854015
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
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
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        cart = context.get('cart', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
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
        __M_writer('Checkout')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def site_center():
            return render_site_center(context)
        form = context.get('form', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        settings = context.get('settings', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <form method="post">\r\n        <table class="table table-striped table-bordered address_table">\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n        </table>\r\n        <span class="checkoutTotal">Total: $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cart.total ))
        __M_writer('</span>\r\n        <script\r\n            src="https://checkout.stripe.com/checkout.js" class="stripe-button"\r\n            data-key="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( settings.STRIPE_PUBLISHABLE_KEY ))
        __M_writer('"\r\n            data-amount="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( cart.total * 100 ))
        __M_writer('"\r\n            data-name="Demo Site"\r\n            data-description="Widget"\r\n            data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\r\n            data-locale="auto"\r\n            data-zip-code="auto">\r\n        </script>\r\n    </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"29": 0, "42": 1, "47": 3, "57": 3, "63": 3, "69": 5, "79": 5, "80": 8, "81": 8, "82": 10, "83": 10, "84": 13, "85": 13, "86": 14, "87": 14, "93": 87}}
__M_END_METADATA
"""
