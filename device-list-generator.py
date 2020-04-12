import requests,os

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME']
BROWSERSTACK_ACCESS_KEY = os.environ['BROWSERSTACK_ACCESS_KEY']


response = requests.get('https://api-cloud.browserstack.com/app-automate/devices.json', auth=(BROWSERSTACK_USERNAME,BROWSERSTACK_ACCESS_KEY))
# print(response.json())

devices = response.json()

# print(devices)
ios_device = '['
android_device = '['
for device in devices:
	if(device['os'] == 'ios'):
		ios_device= ios_device+'{ "devices":"'+device['device']+'-'+device['os_version']+'" },'

	else:
		android_device = android_device+'{ "devices":"'+device['device']+'-'+device['os_version']+'" },'



android_device = android_device + ']'
ios_device = ios_device + ']'



f = open("android_device.json","w")
f.write(android_device.replace(",]","]"))
f.close()

f = open("ios_device.json","w")
f.write(ios_device.replace(",]","]"))
f.close()

