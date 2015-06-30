import os
from django.contrib import admin
from signalqueue.utils import SQ_ROOT

admin.site.index_template = os.path.join(SQ_ROOT, 'templates/admin/index_with_queues.html')
admin.site.app_index_template = os.path.join(SQ_ROOT, 'templates/admin/app_index.html')

import signalqueue.models

class EnqueuedSignalAdmin(admin.ModelAdmin):
    list_display  = ('queue_name', 'createdate', 'enqueued', 'value')
    list_filter   = ('queue_name', 'createdate')
admin.site.register(signalqueue.models.EnqueuedSignal,EnqueuedSignalAdmin)
