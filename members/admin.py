from django.contrib import admin
from django.urls import reverse
from members.models import Form,Order,Person
from django.db import models
from django.forms import TextInput, Textarea
#from django.core import urlresolvers
from django.utils.html import format_html
import re
from django.utils.safestring import mark_safe
#from django.conf.locale.en import formats as en_formats

#en_formats.DATETIME_FORMAT = "d m Y"
#en_formats.DATE_FORMAT = "d m"
def admin_fecha(self, obj):
        return obj.fecha.strftime('%Y-%m-%d')

def reverse_foreignkey_change_links(model, get_instances, description=None, get_link_html=None, empty_text='(None)'):
    if not description:
        description = model.__name__ + '(s)'

    def model_change_link_function(_, obj):
        instances = get_instances(obj)
        if instances.count() == 0:
            return empty_text
        output = ''
        links = []
        for instance in instances:
            change_url = reverse('admin:%s_change' % model._meta.db_table, args=(instance.id,))
            links.append('<a href="%s">%s</a>' % (change_url, str(instance)))
        return format_html(', '.join(links))

    model_change_link_function.short_description = description
    model_change_link_function.allow_tags = True
    return model_change_link_function

class CSSAdminMixin(object):
    class Media:
        css = {
            'all': ('css/fancy.css',)
        }

class OrderAdmin(admin.ModelAdmin,CSSAdminMixin):   
    formfield_overrides = {
        models.FloatField: {'widget': Textarea(attrs={'size':'8', 'style': 'text-align:right;border-top:none;border-left:none;border-right:none;border-radius:0;background:transparent;', }), },
        models.DateTimeField: {'widget': Textarea(attrs={'rows':1,'cols':10})},
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':80})},
        models.CharField: {'widget': Textarea(attrs={'rows':1, 'cols':80})},
        #models.TextField: {'widget': Textarea(attrs={'size':'4', 'style': 'text-align:right;border-top:none;border-left:none;border-right:none;border-radius:0;background:transparent;', }), },
    }

    #def pedido(self,obj):
    #    return obj.num_pedido
    #pedido.short_description = '#'
    
    #@admin.display(description='Birth decade')
    #def admin_fecha(self, obj):
    #    return obj.fecha.strftime("%d.%b.%Y")
    #admin_fecha.short_description = 'Fecha'
    
    search_fields = ['cliente']
    list_display = ['num_pedido','fecha','cliente','email','total','total_pagado','order','elementos_list']
    readonly_fields = ['cliente','fecha','elementos_list','image','externa']
    fields = ('cliente','fecha','elementos_list','image','externa')
    #def forms(self,obj):
    #    return ",".join([k.rut for k in obj.form_set.all()])

    #def e_list = reverse_foreignkey_change_links(Form, lambda obj:Form.objects.filter(order=obj.num_pedido))

    def order(self,obj):
            output = re.sub('\|','<br><br>',obj.order_items) #.replace('|',"<br><br><br>")
            return mark_safe(output)
    order.short_description = "Detalle"
    order.allow_tags = True

    def image(self,obj):
            return mark_safe('<span style="color: green;"><img src="/static/img/logo.svg"/ height="20"> imagen</span>')
    def externa(self,obj):
            return mark_safe('<img src="https://www.cobsandcogs.cl/wp-content/themes/cobsandcogs/images/logo-white.svg"/>')
    def elementos_list(self,obj):
        elementos  = Form.objects.filter(order=obj.num_pedido)
        if elementos.count() == 0:
            return '(None)'
        output = '<br><br> '.join([str(elemento.apellido_paterno)+' '+str(elemento.nombre)+' '+str(elemento.rut) for elemento in elementos])    
        return mark_safe(output)
    elementos_list.short_description = 'Miembros'
    elementos_list.allow_tags = True

        

class OrderInline(admin.TabularInline):
    model = Order



class FormAdmin(admin.ModelAdmin):
    #model = Forms
    #inlines=[OrdersInline]
    list_display = ['order','rut','get_detail']
    fields = ['num_pedido','rut']
    def get_detail(self,obj):
        return obj.order.total_pagado
    #list_filter = ['standard',] # ACA DEBO FILTRAR POR PRODUCTO año etc
    def __str__(self):
        return self.name


class PersonAdmin(admin.ModelAdmin):
    #model = Forms
    #inlines=[OrdersInline]
    formfield_overrides = {
        models.FloatField: {'widget': Textarea(attrs={'size':'8', 'style': 'text-align:right;border-top:none;border-left:none;border-right:none;border-radius:0;background:transparent;', }), },
        models.DateTimeField: {'widget': Textarea(attrs={'rows':1,'cols':10})},
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':80})},
        models.CharField: {'widget': Textarea(attrs={'rows':1, 'cols':30})},
        #models.TextField: {'widget': Textarea(attrs={'size':'4', 'style': 'text-align:right;border-top:none;border-left:none;border-right:none;border-radius:0;background:transparent;', }), },
    }
    list_display = ['person_rut','person_apaterno','person_amaterno','person_nombres']
    search_fields = ['person_apaterno']
    fields = ['person_rut',('person_apaterno','person_amaterno','person_nombres')]
    #def get_detail(self,obj):
     #   return obj.order.total_pagado  

#    orders = models.ForeignKey(Orders)

class FormSummary(admin.ModelAdmin):
    fields = ['productos_field']

# Register your models here.
admin.site.register(Form,FormAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Person,PersonAdmin)