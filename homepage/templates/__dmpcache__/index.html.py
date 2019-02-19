# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1549311399.2705524
_enable_loop = True
_template_filename = 'C:/Users/cnels/dmp_projects/Project1/homepage/templates/index.html'
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
        self = context.get('self', UNDEFINED)
        utc_time = context.get('utc_time', UNDEFINED)
        def site_center():
            return render_site_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
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
        __M_writer('\r\n    Homepage\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        utc_time = context.get('utc_time', UNDEFINED)
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="site_center">\r\n        <h3>Congratulations -- you\'ve successfully created a new DMP app!</h3>\r\n        <h4 class="utc-time">Current time in UTC: ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( utc_time ))
        __M_writer('</h4>\r\n\r\n        <p>\r\n            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget interdum nunc. Nam diam tellus, ultricies vel egestas sit amet, lacinia id orci. Nulla tempor nunc a faucibus porttitor. Mauris elit justo, luctus sit amet ultricies quis, efficitur nec purus. Mauris non ultrices nunc. Curabitur varius pharetra placerat. Vestibulum vel justo ac odio lacinia vulputate id ac dolor. Integer id luctus mi, non tincidunt eros. Quisque consectetur, tortor ut consectetur hendrerit, dolor ligula fringilla velit, vel ultrices ligula eros ac orci. Maecenas pharetra ullamcorper erat, eget porta felis auctor in. Nulla non suscipit tellus.\r\n        </p>\r\n        <p>\r\n            In varius finibus augue, non iaculis ex placerat quis. Cras id orci vitae sem egestas viverra. Quisque vehicula, elit a porta rutrum, lacus elit commodo tortor, nec ultrices magna enim sit amet tellus. Curabitur lacinia nulla a tortor pellentesque vehicula. Mauris non efficitur quam. In convallis tortor leo, nec commodo magna aliquam a. Nullam auctor et nulla at convallis. Fusce id lectus porttitor, lobortis nisl quis, rutrum erat.\r\n        </p>\r\n        <p>\r\n            Etiam lacinia bibendum nibh eget consequat. Duis lacinia, lorem blandit vulputate fermentum, risus quam semper eros, sit amet ullamcorper elit nulla a turpis. Nullam non sodales tellus. Quisque id arcu at sem dictum sagittis eu eget est. Maecenas nec sapien pretium, porttitor velit id, pulvinar risus. Nam sit amet augue in nisi laoreet egestas nec in nibh. Nam porttitor tortor vitae tellus tempor accumsan. Aliquam ac neque consectetur, accumsan leo vel, fringilla enim. Suspendisse eleifend lacinia tortor, quis porttitor lectus varius vel. Nunc congue, urna eget elementum porttitor, justo ligula maximus augue, sit amet imperdiet est leo vitae massa. Proin lacus leo, tristique in auctor id, lacinia id massa. Integer quis augue turpis. Aliquam vitae laoreet neque.\r\n        </p>\r\n        <p>\r\n            Phasellus facilisis lectus id posuere dapibus. Mauris ex erat, vulputate vel sapien vitae, consequat iaculis ante. Pellentesque interdum dapibus ex elementum maximus. Vivamus mattis dolor vitae massa molestie commodo. Aenean tincidunt commodo bibendum. Donec scelerisque, urna nec pretium vehicula, purus odio viverra neque, sed tempor odio dolor nec lorem. Aliquam risus est, tempus dapibus suscipit sollicitudin, finibus id ligula. Duis venenatis vestibulum arcu et dictum. Nam ac justo sit amet ipsum facilisis imperdiet. Fusce dapibus congue ex, non tincidunt elit. Mauris maximus tempor scelerisque. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nullam at lacus non mi hendrerit fringilla interdum eget tellus.\r\n        </p>\r\n        <p>\r\n            Ut quis bibendum arcu. Mauris massa nunc, hendrerit sit amet augue et, fermentum efficitur velit. Integer ullamcorper imperdiet porttitor. Maecenas pharetra eget nulla sed dignissim. Curabitur lacinia velit tortor, at scelerisque lacus condimentum vel. Duis vitae arcu gravida felis venenatis placerat eu eget ex. Cras nec maximus tellus, id fermentum elit. Duis maximus varius turpis eget pellentesque. Donec viverra ex purus, ac scelerisque massa mollis eget. Pellentesque vel sem et nisl posuere malesuada. In non faucibus quam. Sed nec malesuada tellus, at hendrerit quam. Fusce ornare leo non viverra egestas.\r\n        </p>  \r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/cnels/dmp_projects/Project1/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 5, "50": 27, "56": 3, "62": 3, "68": 6, "76": 6, "77": 9, "78": 9, "84": 78}}
__M_END_METADATA
"""
