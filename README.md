# network_speedtest
A simple network speedtest utilizing the speedtest-cli library. 
Test results are stored in the speedtest.log file in C:\Users\%USERNAME%\Documents\network_speedtest directory. 
Results of each speedtest are timestamped at the time the test is run. 
The script can be used to create a scheduled task for regular monitoring of network speeds


Troubleshooting.
When running the script the first time you may recieve an error message that the speedtest module is not installed. 
run the command "pip install speedtest-cli" to resolve the problem. 

On certain Linux systems you may recieve an error when trying to install the module. 
Run the command "pip install speedtest-cli --break-system-packages" 
