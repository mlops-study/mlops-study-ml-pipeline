AIRFLOW_HOME=~/airflow

# kill airflow processes
base_name=`basename "${0}"`
echo "base_name = ${base_name}"
PROCESS_IDS=(`ps -ef | grep 'airflow' | grep -v 'grep' | grep -v "${base_name}" | awk '{print $2}'`)
echo "PROCESS_IDS = (${PROCESS_IDS})"
if [ ${#PROCESS_IDS[@]} -gt 0 ]; then
  for pid in $PROCESS_IDS; do
    kill -9 ${pid}
    echo "${pid} process has ended."
  done
else
  echo "No processes are running."
fi

sleep 3

# delete *.pid in the directory of ~/airflow.
PROCESS_ID_FILES=(`ls ${AIRFLOW_HOME} | grep ".pid"`)
echo "PROCESS_ID_FILES = (${PROCESS_ID_FILES})"
if [ ${#PROCESS_ID_FILES[@]} -gt 0 ]; then
  for file in $PROCESS_ID_FILES; do
    rm -f "${AIRFLOW_HOME}/${file}"
    echo "${file} file has deleted."
  done
fi

sleep 1
