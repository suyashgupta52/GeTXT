try:
    from Modules import DataCleaning, DataCollection
    import threading
    import var
    from time import sleep
except Exception as e:
    exit("Exception: " + str(e))

# Driver Function
if __name__ == '__main__':    
    var._debug and print("App Starting...")
    # Data Collection 
    dataCollection =  DataCollection()
    dataCleaning = DataCleaning()
    threads = []
    while True:
        var._debug and print("Active Threads => ", threading.active_count())
        try:
            thread = threading.Thread(None, target=dataCleaning._cleaning)
            thread.start()
            threads.append(thread)
            var._debug and print("Active Threads => ", threading.active_count())
            sleep(var._sleep_time_small) #small time  
            thread = threading.Thread(None, target=dataCollection._collect, args=(["Call center Reviews", "New Product Review", "Product Complaints", "Customer Service Center","Customer HelpCenter", "Amazon Product Reviews", "Service Reviews", "Company’s Reputation", "Product Comment"],))
            thread.start()
            threads.append(thread)
            var._debug and print("Active Threads => ", threading.active_count())
            sleep(var._sleep_time_small) #small time  
        except KeyboardInterrupt:
            var._debug and print("Keyboard Interrupt")
            break    
        except Exception as e:
            var._debug and print("App Error:  ", e)
        var._debug and print("Active Threads => ", threading.active_count())
        sleep(var._sleep_time_small) #small time  
        for thread in threads:
            var._debug and print("Active Thread Left => ", threading.active_count())
            sleep(var._sleep_time_small) #small time  
            thread.join()
            
        sleep(var._sleep_time_small) #small time  
        var._debug and print("Active Threads => ", threading.active_count())
        
        sleep(var._sleep_time_small) #small time  
        print("Threads Running: ", threading.enumerate())
        
        sleep(var._sleep_time_small) #small time  
        var._debug and print("Running Thread: ", threading.current_thread())      \
        # Check ENV
        if var._deployment_env == False:
            var._debug and print("Developer Environment!!")
            break  
    var._debug and print("App Closed.")