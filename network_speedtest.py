import speedtest
from datetime import datetime
import os



def run_speedtest():

    #create timestamp for speedtest log at moment of test
    timestamp = datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")
    try:
        
        #build log directory
        home = os.path.expanduser("~")
        log_dir = os.path.join(home,"Documents","network_speedtest")
        log_file_path = os.path.join(log_dir, "speedtest.log")

        #test if log directory exists and make it if it does not
        if not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
            
        #create timestamp for speedtest log at moment of test
        #timestamp = datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")
        
        st = speedtest.Speedtest()
        st.get_best_server()#get the best server
        
        #conversion from bits to Mbps
        download = st.download() / 10**6
        upload = st.upload() / 10**6
        
        #log results to file
        with open(log_file_path, "a") as f:
            f.write(f"{timestamp} - Download: {download:.2f} Mbps, Upload: {upload:.2f} Mbps\n")
            print(f"Test complete: {download:.2f} Mbps down / {upload:.2f} Mbps up")
            
    except Exception as e:
        error_msg = f"[{timestamp}] Speedtest failed: {e}"
        print(error_msg)
        # Note: This will only work if log_dir was successfully created
        if os.path.exists(log_dir):
            with open(log_file_path, "a") as f:
                f.write(error_msg + "\n")


if __name__ == "__main__":
    run_speedtest()
