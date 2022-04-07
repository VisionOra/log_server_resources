#!/bin/bash -e

process=$(ps aux | grep  'get_linux_logs.sh'| wc -l)

echo $process
# Checking if process is running or not
if [ $process -gt 3 ]
  then
    # Running process if not running
    echo "Logging script already running"
    
else
    # this script is only for ubuntu server
    while true; do
        # filename
        file_name="logs/serverLogs_$(date '+%Y_%m_%d').log"
        # Checking if file exists
        if [ ! -f $file_name ]; then
          # If not exists then make a file and add headers
          echo -e  "datetime $(free -m | grep total | sed -E 's/^    (.*)/\1/g' | tr -s ' ' | tr ' ' '\t')\tcores" >> $file_name
        fi
        # Getting core utilisation
        core_load=$(mpstat -P ALL 1 1 | awk '/Average:/ && $2 ~ /[0-9]/ {print $3}' | tr '\n' ',')
        # logging ram utilisation and core utilisation
        echo -e "$(date '+%Y-%m-%d %H:%M:%S') $(free -m | grep Mem: | sed 's/Mem://g' | tr -s ' ' | tr ' ' '\t') \t $core_load" >> $file_name
        # Sleep
        sleep 5
    done
    
fi


