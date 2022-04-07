# Introduction


There are 2 files which we use

* bash script to capture server logs
* python api to visualise logs

# Bash Script


Bash script provide us these logs

* datetime 
* Every core log
* Free Ram Log
* Used Ram log
* cache log


# Python (Fast API)


We are using this api only to visualise logs you can get the documentation of api by going on ```/docs``` route

with ```/get_logs``` api you can get the urls according to the dates to visualise the graph

![Api response](./attachments/Screenshot%202022-04-07%20at%202.42.55%20PM.png)

Graph for ```http://127.0.0.1:8000/GetGraph/sample_2022_04_06.log```

![Api response](./attachments/Screenshot%202022-04-07%20at%202.53.38%20PM.png)