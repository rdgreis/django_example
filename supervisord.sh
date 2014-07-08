#!/bin/sh
# Amazon Linux AMI startup script for a supervisor instance
#
# chkconfig: 2345 80 20
# description: Autostarts supervisord.

# Source function library.
. /etc/rc.d/init.d/functions

supervisorctl="/usr/bin/supervisorctl"
supervisord="/usr/bin/supervisord"
name="supervisor-python"

[ -f $supervisord ] || exit 1
[ -f $supervisorctl ] || exit 1

RETVAL=0

start() {
     echo -n "Starting $name: "
     $supervisord
     RETVAL=$?
     echo
     return $RETVAL
}

stop() {
     echo -n "Stopping $name: "
    $supervisorctl shutdown
     RETVAL=$?
     echo
     return $RETVAL
}

case "$1" in
         start)
             start
             ;;

         stop)
             stop
             ;;

         restart)
             stop
             start
             ;;
esac

exit $REVAL