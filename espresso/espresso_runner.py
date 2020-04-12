import requests,sys
import os,json
import time

device_list = sys.argv[1]
app = sys.argv[2]
test = sys.argv[3]
	
device_array = []
device=0
with open(device_list, "r") as f:
    obj = json.loads(f.read())

print(len(obj))

for devices in obj:
	device_array.append(devices['device'])
	print(devices['device'])
BROWSERSTACK_USERNAME = os.environ["BROWSERSTACK_USERNAME"]
BROWSERSTACK_ACCESS_KEY = os.environ["BROWSERSTACK_ACCESS_KEY"]

print("Device List:"+device_list+"  App:"+app+"  Test:"+test)

response = requests.get('https://api-cloud.browserstack.com/app-automate/plan.json', auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
parallel_limit = response.json()
parallel_limit = parallel_limit['parallel_sessions_max_allowed']

print(response.json())

def running_parallel():
	response = requests.get('https://api-cloud.browserstack.com/app-automate/plan.json', auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
	limit = response.json()
	return(limit['parallel_sessions_running'])


while (running_parallel() < parallel_limit or device != len(obj)):
	if (running_parallel() != parallel_limit):
		if(device<len(obj)):
			print(running_parallel())
			headers = {
			    'Content-Type': 'application/json',
			}
			data = '{"devices": ["'+device_array[device]+'"], "app": "'+app+'", "deviceLogs" : "true", "testSuite": "'+test+'"}'
			response = requests.post('https://api-cloud.browserstack.com/app-automate/espresso/build', headers=headers, data=data, auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
			print(response.json())
			device = device+1
		else:
			print("Device List Complete")
			break;
	else:
		time.sleep(3)
