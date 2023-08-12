# start airflow web services.
WEB_PROCESS_IDS=(`ps -ef | grep "airflow-webserver" | grep -v 'grep' | awk '{print $2}'`)
if [ ${#WEB_PROCESS_IDS[@]} -gt 0 ]; then
  echo "Airflow webserver is running!"
else
  airflow webserver --port 8080 -D
  sleep 10
  echo "Airflow webserver has run!"
fi

# start airflow scheduler.
SCHEDULER_PROCESS_IDS=(`ps -ef | grep "airflow scheduler" | grep -v 'grep' | awk '{print $2}'`)
if [ ${#SCHEDULER_PROCESS_IDS[@]} -gt 0 ]; then
  echo "Airflow scheduler is running!"
else
  airflow scheduler -D
  sleep 3
  echo "Airflow scheduler has run!"
fi

# start airflow triggerer.
TRIGGERER_PROCESS_IDS=(`ps -ef | grep "airflow triggerer" | grep -v 'grep' | awk '{print $2}'`)
if [ ${#TRIGGERER_PROCESS_IDS[@]} -gt 0 ]; then
  echo "Airflow triggerer is running!"
else
  airflow triggerer -D
  sleep 3
  echo "Airflow triggerer has run!"
fi
