import time

def stress_test():
    start_time = time.time()
    
    # Perform a simple computational task
    total = 0
    for i in range(10**7):
        total += i**2
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"Stress test completed in {elapsed_time:.2f} seconds.")
    
stress_test()