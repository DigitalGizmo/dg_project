Maintenance
============

No database involved.

Virtual envs
-----------
local: workon gizmo

eApps: workon no longer not set up, but app uses .envs/gizmoz


Git updates
-----------

log in as gizmo_user
::
	cd /var/www/gizmo_user/data/www/digitalgizmo.com.vm-host.net
	cd /var/www/gizmo_user/data/www/digitalgizmo.com

git fetch needs password: gizmo_user password

Touch, while in ...www/digitalgizmo.com
::
	touch gizmo/config/wsgi.py

Collect static
----------------
whlie in /var/www/gizmo_user/data
::
	./collect.sh
