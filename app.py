try:    
    from Modules import DataCleaning, DataCollection    
    import threading
    import var
    from time import sleep
except Exception as e:      
    exit("Exception: " + str(e))

# Driver Function
def _main():
    var._debug and print("App Starting...")
    # Data Collection 
    dataCollection =  DataCollection()
    dataCleaning = DataCleaning()
    threads = []
        
    while True:
        var._debug and print("Threads Running: ", threading.active_count())
        try:
            thread = threading.Thread(None, target=dataCleaning._cleaning, daemon=True)
            thread.start()
            threads.append(thread)
            var._debug and print("A Thread => ", threading.active_count())
            sleep(var._sleep_time_small) #small time  
            thread = threading.Thread(None, target=dataCollection._collect, args=(["Call center Reviews", "New Product Review", "Product Complaints", "Customer Service Center","Customer HelpCenter", "Amazon Product Reviews", "Service Reviews", "Company’s Reputation", "Product Comment"],), daemon=True)
            thread.start()
            threads.append(thread)
            var._debug and print("A Thread => ", threading.active_count())                    
            sleep(var._sleep_time_small) #small time  
            
            dataCleaning._cleaning()
            var._debug and print("A Thread => ", threading.active_count())                    
            sleep(var._sleep_time_small) #small time  
            dataCollection._collect(["Amazon Product Reviews", "Product Reviews", "Call center Reviews", "Company’s Reputation", "Service Reviews", "Company Reviews"])
            var._debug and print("A Thread => ", threading.active_count())                    
            sleep(var._sleep_time_small) #small time  
        except KeyboardInterrupt:
            var._debug and print("Keyboard Interrupt")
            break    
        except Exception as e:
            var._debug and print("App Error:  ", e)
            
        var._debug and print("Active Threads => ", threading.active_count())
        sleep(var._sleep_time_small) #small time  
        
        for thread in threads:
            print(thread.name)
            var._debug and print("Closing Threads:", threading.active_count())
            sleep(var._sleep_time_small) #small time  
            thread.join()
        try:    
            for thread in  threading.enumerate():
                if thread.name != "MainThread":
                    print(thread.name)
                    var._debug and print("Closing Enumerate Threads:",str(thread.name+" ("+threading.active_count()+") "))
                    sleep(var._sleep_time_small) #small time  
                    thread.join()
        except Exception as e:
            print("Eception:",e)
            print(thread.name)
                        
        sleep(var._sleep_time_small) #small time  
        var._debug and print("Active Threads => ", threading.active_count())
        
        sleep(var._sleep_time_small) #small time  
        print("Threads Running: ", threading.enumerate())
        
        sleep(var._sleep_time_small) #small time  
        var._debug and print("Running Thread: ", threading.current_thread())      
        # Check ENV
        if var._deployment_env == False:
            var._debug and print("Developer Environment!!")
            break
            
    for thread in  threading.enumerate():
        if thread.name != "MainThread":            
            var._debug and print("Cleaning Enumerate Threads:",str(thread.name+" ("+threading.active_count()+") "))
            sleep(var._sleep_time_small) #small time  
            thread.join()
    var._debug and print("App Closed.")    
    return "Back to Main!!"


# Main Method
if __name__ == '__main__':
    exit("Exit with " + _main())   