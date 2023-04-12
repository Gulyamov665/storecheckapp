# from django.forms import SelectMultiple, CheckboxInput
# from django.forms.utils import flatatt
# from django.utils.encoding import force_str
# from django.utils.html import conditional_escape
# from django.utils.safestring import mark_safe
#
#
# class WidgetCheckbox(SelectMultiple):
#     def __init__(self, attrs=None, choices=()):
#         super().__init__(attrs, choices)
#
#     def render(self, name, value, attrs=None, renderer=None):
#         if value is None:
#             value = []
#         has_id = attrs and 'id' in attrs
#         final_attrs = self.build_attrs(attrs, name=name)
#         output = []
#         str_values = {force_str(v) for v in value}
#         for i, (pk, obj) in enumerate(self.choices):
#             cb = CheckboxInput(final_attrs, checktest=lambda value: value in str_values)
#         option_value = force_str(pk, obj)
#         rendered_cb = cb.render(name, option_value)
#         rendered_img = '<img src="{0}" alt="{1}" />'.format(obj.image.url, conditional_escape(obj.name))
#         label_for = flatatt({'for': 'id_%s' % pk})
#         rendered_label = '<label{0}>{1}</label>'.format(label_for, rendered_img)
#         output.append('<li>{0} {1}</li>'.format(rendered_cb, rendered_label))
#
#         return mark_safe('<ul>\n{0}\n</ul>'.format('\n'.join(output)))
