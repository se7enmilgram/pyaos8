#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, json

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class interfaces():

    def get_int(auth):

        url = "https://" + auth.aos8ip + ":4343/api/Interfaces.json?json=1&UIDARUBA=" + auth.uidaruba
        aoscookie = dict(SESSION = auth.uidaruba)
        #print(url_showcommand)
        try:
            r = requests.get(url, cookies=aoscookie, verify=False)
            # showdata = json.loads(r.text)['mac_table_entry_element']
            if r.status_code != 200:
                #print(vars(r))
                print('Status:', r.status_code, 'Headers:', r.headers,
                      'Error Response:', r.reason)

            return r.text
        except requests.exceptions.RequestException as error:
            #print("Error")
            return "Error:\n" + str(error) + " get_interfaces: An Error has occured"
