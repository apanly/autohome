#!/bin/bash
`ps -ef | grep '/home/www/virpython/bin/uwsgi -s /tmp/uwsgi.sock' | awk '{print $2}' | xargs kill -9`
RELEASE_VERSION=`cat /home/www/config/RELEASE_VERSION_GA`
cd /home/www/release/$RELEASE_VERSION/src/cmdb/
/home/www/virpython/bin/uwsgi -s /tmp/uwsgi.sock -w manage:app -p 4   --chmod-socket=662  --buffer-size=32768  --post-buffering=1