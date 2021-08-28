from threading import Thread

def launch_threads(function, dispatch_param, num_threads):
    threads = []
    for idx in range(num_threads):
        th = Thread(target = function, args = dispatch_param(idx))
        threads.append(th)
    for th in threads:
        th.start()
    for th in threads:
        th.join()

