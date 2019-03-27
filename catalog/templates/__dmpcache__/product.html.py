# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553718407.0910606
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/product.html'
_template_uri = 'product.html'
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
        product = context.get('product', UNDEFINED)
        featured = context.get('featured', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        thumbnails = context.get('thumbnails', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context)
        product = context.get('product', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.name ))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        product = context.get('product', UNDEFINED)
        featured = context.get('featured', UNDEFINED)
        def site_center():
            return render_site_center(context)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        thumbnails = context.get('thumbnails', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="container row">\r\n        <div class="col-1 thumbnail_div">\r\n')
        for url in thumbnails:
            __M_writer('                <div class="thumbnail_pic">\r\n                    <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( url ))
            __M_writer('" alt="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.name ))
            __M_writer(' Image" />\r\n                </div>\r\n')
        __M_writer('        </div>\r\n        <div class="col-4 featured_pic">\r\n            <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( featured ))
        __M_writer('" alt="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.name ))
        __M_writer(' Image" />\r\n        </div>\r\n        <div class="col-7 product_details">\r\n            <h1>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.name))
        __M_writer('</h1>\r\n            <p><b>Price:</b> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.price))
        __M_writer('</p>\r\n            <p><b>Quantity In Stock:</b> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.quantity ))
        __M_writer('</p>\r\n            <form method="post">\r\n                <table class="buyTable">\r\n                    ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form.as_table() ))
        __M_writer('\r\n                </table>\r\n            <input class="btn btn-primary buyBtn" type="submit" value="Buy Now">\r\n            </form>\r\n            <br />\r\n            <p><b>Category:</b> <a href=\'/catalog/index/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.category.id))
        __M_writer("'>")
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( product.category.name ))
        __M_writer('</a></p>\r\n            <p><b>Description:</b> ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.description))
        __M_writer('</p>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 3, "53": 32, "59": 3, "67": 3, "73": 5, "84": 5, "85": 8, "86": 9, "87": 10, "88": 10, "89": 10, "90": 10, "91": 13, "92": 15, "93": 15, "94": 15, "95": 15, "96": 18, "97": 18, "98": 19, "99": 19, "100": 20, "101": 20, "102": 23, "103": 23, "104": 28, "105": 28, "106": 28, "107": 28, "108": 29, "109": 29, "115": 109}}
__M_END_METADATA
"""
