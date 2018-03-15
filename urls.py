#__BEGIN_LICENSE__
# Copyright (c) 2015, United States Government, as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All rights reserved.
#
# The xGDS platform is licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#__END_LICENSE__

from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth.views import login
from django.contrib import auth
from django.views.generic import RedirectView, TemplateView

from django.contrib import admin
import re
admin.autodiscover()

urlpatterns = [url(r'^admin/', include(admin.site.urls)),
               url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
               url(r'^$', RedirectView.as_view(url=settings.SCRIPT_NAME + settings.XGDS_SITE_APP + '/', permanent=False),{}),
               url(r'^accounts/', include('xgds_core.registerUrls')),
               url(r'^favicon\.ico$', RedirectView.as_view(url='/static/' + settings.FAVICON_PATH, permanent=True), {'readOnly': True}),
               url(r'^pycroraptor/', include('geocamPycroraptor2.urls')),
               url(r'^track/', include('geocamTrack.urls')),
               ]

for app in filter(lambda app : re.match(r'^xgds_', app), settings.INSTALLED_APPS):
    urlpatterns.append(url(r'^' + re.escape(app + '/'), include(app + '.urls'), app))

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls)),
                    ]
