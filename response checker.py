import requests
import time

# Get user input for URL and number of requests
url = input("Enter the URL of the website to test: ")
num_requests = int(input("Enter the number of requests to send: "))

# Send requests and measure response time
total_time = 0
for i in range(num_requests):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    total_time += (end_time - start_time)
    print(f'Request {i+1}: {end_time - start_time:.3f} seconds')

# Calculate and print average response time
avg_time = total_time / num_requests
print(f'Average response time: {avg_time:.3f} seconds')


print("This code is written by Md Ibrahim Adham Aomy")