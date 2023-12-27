import speedtest
import time

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    st.download()
    st.upload()
    results = st.results.dict()

    download_speed = results["download"]
    upload_speed = results["upload"]
    ping = results["ping"]

    return download_speed, upload_speed, ping

while True:
    try:
        download_speed, upload_speed, ping = test_speed()
        print(f"Download Speed: {download_speed / 1024 / 1024:.2f} Mbps")
        print(f"Upload Speed: {upload_speed / 1024 / 1024:.2f} Mbps")
        print(f"Ping: {ping} ms")

        with open("speed_test_results.txt", "a") as file:
            file.write(f"{time.ctime()}, Download: {download_speed / 1024 / 1024:.2f} Mbps - Upload: {upload_speed / 1024 / 1024:.2f} Mbps - Ping: {ping} ms\n")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    time.sleep(60)
