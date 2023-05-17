# **_Python program to send OpenWeatherMap(OWM) data to Fogwing_** 

This repository contains a Python program, that allows you to retrieve weather data from the OpenWeatherMap API and send it to the Fogwing IoTHub API. The program is compatible with any Python environment and can be executed without any specific restrictions.

>**Note:** This program is specific to send OpenWeatherMap (OWM) to Fogwing. It may require additional modifications and configurations to work properly with your specific use case.

### Pre-requisites:
- [Python 3.10](https://www.python.org/)
- [pip 23.1.2](https://pip.pypa.io/en/stable/)

## **OpenWeatherMap to Fogwing Client Program**

To run the `OWMToFogwingClient.py` program, follow the step-by-step instructions below:

### **Step 1: Clone the Repository**
- Clone the [fogwing-thirdpatry-integration-python](https://github.com/factana/fogwing-thirdpatry-integration-python) repository containing the program code to your local machine.

### **Step 2: Install Libraries**
- Install all the required libraries using pip and the requirements.txt file provided using follwing command.
    - `pip install -r requirements.txt`

### **Step 3: Update Credentials**
- Locate the **credentials.json** file in **fogwing-thirdpatry-integration-python** repository, open the file and you will find sections for OWM and Fogwing credentials,update the respective fields with your valid OWM and Fogwing credentials.

>**Note:** Ensure that you provide valid OWM and Fogwing IoTHub credentials in the **credentials.json** file for successful data transmission.

### **Step 4: Run the Program**
- Run the Python script using your preferred Python environment. 
- The program will start executing, and the output will be displayed in the terminal.

>**Note:** If everything goes according to the instructions mentioned above, you should see `{'statusCode': 201, 'message': 'Created', 'description': 'The Request Has Succeeded', 'data': 'Successfully published'}` message displayed in the terminal. In case of any errors or issues, an error message will be shown instead.

### **Step 7. Analyze Your Data on the Fogwing Platform**
- Now you are ready to analyze your data at [Fogwing Platform](https://portal.fogwing.net/) portal, you can check all the data within the data storage in the portal.
  
## **Where to Find Help and Resources for Fogwing**
- [Fogwing Open APIs Docs.](https://api.fogwing.net/)
- [OpenWeatherMap API Docs.](https://openweathermap.org/api)
- [Fogwing Platform Forum.](https://community.fogwing.io/)
- [Fogwing Platform Docs.](https://docs.fogwing.io/)
 

## Please visit https://www.fogwing.io/industrial-iot-platform/ for more information about Fogwing Industrial IoT Platform. ##
