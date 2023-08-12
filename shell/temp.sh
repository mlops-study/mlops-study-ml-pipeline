#airflow_run
#airflow db init

#is_alive_web_process() {
#  WEB_PROCESS_IDS=(`ps -ef | grep "airflow-webserver" | grep -v 'grep' | awk '{print $2}'`)
#  if [ ${#WEB_PROCESS_IDS[@]} -eq 0 ]; then echo false; else echo true; fi
#}
#
#if [ $(is_alive_web_process) = false ]; then
##  airflow webserver --port 8080 -D
#  echo "Airflow webserver is not running!"
#else
#  echo "Airflow webserver is running!"
#fi


#function assert() {
#    expected=$1
#    actual=$2
#    message=$3
#
#    if [ "$expected" == "$actual" ]; then
#        log_success "assert $expected == $actual"
#        return 0
#    else
#        log_failure "assert $expected == $actual"
#        exit 1
#    fi
#}
#
#assert false
#if [ $(is_alive_web_process) = false ]; then
#fi