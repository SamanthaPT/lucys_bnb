# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    (r'^$', 'index.index'),
	(r'^book_room$', 'index.book'),
	(r'^our_rooms$', 'index.rooms'),
	(r'^location$', 'index.location'),
	(r'^activities$', 'index.activities'),
	(r'^contact$', 'index.contact'),
	(r'^about_us$', 'index.about_us'),
	(r'^s$', 'index.sendmail'),
    )
