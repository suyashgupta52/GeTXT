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
            # thread 1
            thread = threading.Thread(None, target=dataCleaning._cleaning, daemon=True)
            thread.start()
            threads.append(thread)
            var._debug and print("A Thread => ", threading.active_count())
            
            # Thread 2
            sleep(var._sleep_time_small) #small time  
            thread = threading.Thread(None, target=dataCollection._collect, args=(['Admiration', 'Adoration', 'Aesthetic Appreciation', 'Amusement', 'Anger', 'Anxiety', 'Awe', 'Awkwardness', 'Boredom', 'Calmness', 'Confusion', 'Craving', 'Disgust', 'Empathetic pain', 'Entrancement', 'Excitement', 'Fear', 'Horror', 'Interest', 'Joy', 'Annoyed', 'Nostalgia', 'Relief', 'Romance', 'Sadness', 'Satisfaction', 'Surprise'],), daemon=True)
            thread.start()
            threads.append(thread)
            var._debug and print("A Thread => ", threading.active_count())                    
            
            # Thread 2
            sleep(var._sleep_time_small) #small time  
            thread = threading.Thread(None, target=dataCollection._collect, args=(["Call center Reviews", "New Product Review", "Product Complaints", "Customer Service Center","Customer HelpCenter", "Amazon Product Reviews", "Service Reviews", "Company’s Reputation", "Product Comment", "Marriage", "Birthday", "Happy", "Sad", "Alone","Fear"],), daemon=True)
            thread.start()
            threads.append(thread)
            var._debug and print("A Thread => ", threading.active_count())                    
            
            # Thread 2
            sleep(var._sleep_time_small) #small time  
            thread = threading.Thread(None, target=dataCollection._collect, args=(["Good News", "Bad News", "Deaths", "Covid Deaths", "Depressed", "Unhappy", "Lost Job"],), daemon=True)
            thread.start()
            threads.append(thread)
            var._debug and print("A Thread => ", threading.active_count())                    
            
            # Main Thread
            
            # sleep(var._sleep_time_small) #small time                                      
            # var._debug and print("Running Thread: ", threading.current_thread())          
            # dataCollection._collect(["Good News", "Bad News", "Deaths", "Covid Deaths", "Depressed", "Unhappy", "Lost Job"])        
            # var._debug and print("A Thread => ", threading.active_count())                                
        
            var._active_print and print("Main Thread to Work:")
            sleep(var._sleep_time_small) #small time                          
            dataCleaning._cleaning()
            var._debug and print("A Thread => ", threading.active_count())                                
            
            # All Joins
            sleep(var._sleep_time_small) #small time  
            var._active_print and print("Running Main Thread: ", threading.current_thread())      
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
        var._active_print and print("Running Main Outer Thread: ", threading.current_thread())      
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