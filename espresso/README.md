## Espresso-BrowserStack-AppAutomate-Parallel 

[Espresso](https://developer.android.com/training/testing/espresso)Integration with Browserstack

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)

Running and Controlling and Parallel Test on BrowserStack App-Automate Frameworks (Espresso, XCUITest, EarlGrey))

## Setup

- Clone the repo
- Python setup 
- Upload App and Test App on [BrowserStack]()
- Update `espresso_runner.py` with your [BrowserStack Username and Access Key](https://www.browserstack.com/accounts/settings)
- To generate lastest `device.json` run [device-list Generator](https://github.com/RathilVasani/Bstack-AppAutomate-Parallel)

## Run Test 

- To run test  execute `python espresso_runner.py <os-device.json> <app-url/CustomID> <test_url/CustomID>`

## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/java#setting-os-and-browser)
* You can export the environment variables for the Username and Access Key of your BrowserStack account

  ```
  export BROWSERSTACK_USERNAME=<browserstack-username> &&
  export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
  ```
## Additional Resource
- [Running Espresso Test with BrowserStack](https://www.browserstack.com/app-automate/espresso/get-started)
- [BrowserStack Espresso REST APIs](https://www.browserstack.com/app-automate/rest-api?framework=espresso)

