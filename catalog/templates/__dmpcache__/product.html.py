# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553538108.5491474
_enable_loop = True
_template_filename = 'C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/product.html'
_template_uri = 'product.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['site_center']


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
        product = context.get('product', UNDEFINED)
        thumbnails = context.get('thumbnails', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        featured = context.get('featured', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        product = context.get('product', UNDEFINED)
        thumbnails = context.get('thumbnails', UNDEFINED)
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        featured = context.get('featured', UNDEFINED)
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
        __M_writer('\r\n                </table>\r\n            <input class="btn btn-primary buyBtn" type="submit" value="Buy Now">\r\n            </form>\r\n')
        __M_writer("            <br />\r\n            <p><b>Category:</b> <a href='/catalog/index/")
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
{"filename": "C:/Users/Colby Nelson/dmp_projects/Project1/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "41": 1, "46": 32, "52": 3, "63": 3, "64": 6, "65": 7, "66": 8, "67": 8, "68": 8, "69": 8, "70": 11, "71": 13, "72": 13, "73": 13, "74": 13, "75": 16, "76": 16, "77": 17, "78": 17, "79": 18, "80": 18, "81": 21, "82": 21, "83": 27, "84": 28, "85": 28, "86": 28, "87": 28, "88": 29, "89": 29, "95": 89}}
__M_END_METADATA
"""
