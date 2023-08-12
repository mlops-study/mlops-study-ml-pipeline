# stop airflow processes.
base_name=`basename "${0}"`
PROCESS_IDS=(`ps -ef | grep 'airflow' | grep -v 'grep' | grep -v "${base_name}" | awk '{print $2}'`)
echo "PROCESS_IDS = (${PROCESS_IDS})"
if [ ${#PROCESS_IDS[@]} -gt 0 ]; then
  for PID in $PROCESS_IDS; do
    kill -15 ${PID}
    echo "${PID} process has ended."
  done
else
  echo "No processes are running."
fi
