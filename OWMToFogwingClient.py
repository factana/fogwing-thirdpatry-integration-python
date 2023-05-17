import requests
import json
import logging


class FogwingOWMClient:
    """
    This class is used to send OpenWeatherMap (OWM) data to Fogwing.
    """
    def __init__(self):
        """
        Initializes the class instance by setting class-level attributes:
        """
        # Read the API credentials from the credentials file
        with open("credentials.json", "r") as cred_file:
            cred = json.loads(cred_file.read())

        # OWM Credentials
        owp_cred = cred.get("OWP_CRED")
        self.owp_api_url = owp_cred.get("API_URL")
        self.owp_api_key = owp_cred.get("API_KEY")
        self.city = owp_cred.get("CITY_NAME")

        # Fogwing Credentials
        fw_cred = cred.get("FW_CRED")
        self.fw_api_url = fw_cred.get("API_URL")
        self.fw_acc_id = fw_cred.get("ACCOUNT_ID")
        self.fw_api_key = fw_cred.get("API_KEY")
        self.edge_eui = fw_cred.get("EDGE_EUI")

    def get_owm_data(self):
        """
        This method gets the weather data for the specified city from OWM.
        :returns: Weather data if the request is successful, None otherwise.
        :rtype: Dict/None
        """
        try:
            params = {'q': self.city, 'appid': self.owp_api_key}
            response = requests.get(self.owp_api_url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception(f"Error getting OWM data: {response.text}")
        except Exception as ex:
            logging.error(ex)
            return None

    def send_data_to_fogwing(self, owmdata):
        """
        This method sends the OWM data to Fogwing.
        :param owmdata: OpenWeatherMap data.
        :returns: Fogwing API response
        :rtype: Dict
        """
        try:
            header = {"accountID": self.fw_acc_id, "apiKey": self.fw_api_key, "edgeEUI": self.edge_eui}
            response = requests.post(self.fw_api_url, data=json.dumps(owmdata), headers=header)
            fw_response = response.json()
            if response.status_code == 201:
                return fw_response
            else:
                return f"Error sending data to Fogwing: {fw_response}"
        except Exception as ex:
            logging.error(ex)


if __name__ == "__main__":
    client = FogwingOWMClient()
    owm_data = client.get_owm_data()
    if owm_data:
        print(client.send_data_to_fogwing(owm_data))
