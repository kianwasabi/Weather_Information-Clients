import requests
import json
class Process():
    def __init__(self, server_ip):
        self.server_ip = server_ip
        self.keys, self.methods, self.routes, self.request_keys, self.response_keys = self._RequestRecipe()
    def __str__(self):
        return (f"server_ip = {self.server_ip},routes = {self.routes}, keys = {self.keys}, methods = {self.methods}, requests = {self.request_keys}, responses = {self.response_keys}")
    def _Request(self, route, request_key, request_value, key, methode):
        url = "http://"+self.server_ip+route
        payload = json.dumps(
            {
            "Request_Data": {
                request_key : request_value}
            })
        headers = {
            'Key': key,
            'Content-Type': 'application/json'
        }
        response = requests.request(methode, url, headers=headers, data=payload)
        print("╔════════════════════════════════════════════════════════════════╗")
        print(headers)
        print(payload)
        print("╚════════════════════════════════════════════════════════════════╝")
        return response
    def _RequestRecipe(self): 
        route = "/api/post/requestrecipe/"
        request_key = "request"
        request_value = "Please send back my recipe."
        key = "0120"
        methode = "POST"
        response = self._Request(route,request_key,request_value,key,methode)
        self._ServerResponeinTerminal(response)
        response_payload = response.json()
        keys         = list(response_payload["Response_Data"]["key"].values())
        methods      = list(response_payload["Response_Data"]["method"].values())
        routes       = list(response_payload["Response_Data"]["route"].values())
        request_keys  = list(response_payload["Response_Data"]["request"].values())
        response_keys = list(response_payload["Response_Data"]["response"].values())
        return keys, methods, routes, request_keys, response_keys
    def _ServerResponeinTerminal(self, message):
        print("╔════════════════════════════════════════════════════════════════╗")
        print(message.headers)
        print(message.text)
        print("╚════════════════════════════════════════════════════════════════╝")   
    def RunRecipe(self):
        for idx in enumerate(self.urls):
            self._Request(self.routes[idx],self.request_keys[idx],)

# def func(url_list,method_list,key_list,requestkey_list,responsekey_list):
#     '''
#     :return: none
#     '''
#     for idx, item in enumerate(url_list):
#         payload=0
#         headers=0
#         if(str(key_list[idx])[len(str(key_list[idx]))-3] == "1"): 
#             d = dict.fromkeys(requestkey_list[idx],1)
#             print(dict)
#             payload = json.dumps(
#                 {  
#                     "Request_Data": {
#                         d
#                     }
#                 })
#         if((str(key_list[idx])[len(str(key_list[idx]))-3]) == "2"): 
#             payload = json.dumps(
#                 {  
#                     "Respone_Data": {
#                         {key:"" for key in responsekey_list[idx]}
#                     }
#                 })       
#         headers = {
#             'Key': key_list[idx],
#             'Content-Type': 'application/json'
#         }
#         #Server response (recived recipe)
#         #response = requests.request(method_list[idx], url_list[idx], headers=headers, data=payload) 
#         print(method_list[idx])
#         print(url_list[idx])
#         print(payload)
#         print(headers)

    #def _RequestRecipe(self): 
        # url = "http://"+self.server_ip+"/api/post/requestrecipe/"
        # payload = json.dumps(
        #     {
        #     "Request_Data": {
        #         "Request": "Please send back my recipe. "}
        #     })
        # headers = {
        #     'Key': '0120',
        #     'Content-Type': 'application/json'
        # }
        # response = requests.request("POST", url, headers=headers, data=payload)
        # response_payload = response.json()
        # key_list         = list(response_payload["Response_Data"]["key"].values())
        # method_list      = list(response_payload["Response_Data"]["method"].values())
        # route_list       = list(response_payload["Response_Data"]["route"].values())
        # requestkey_list  = list(response_payload["Response_Data"]["request"].values())
        # responsekey_list = list(response_payload["Response_Data"]["response"].values())
        # url_list = []
        # for route in route_list: 
        #     url_list.append('http://'+self.server_ip+route)
        # return key_list, method_list, route_list, requestkey_list, responsekey_list, url_list

            #    for idx, item in enumerate(self.urls):
            # payload = json.dumps(
            #     {
            #     "Request_Data": {
            #         self.requests[idx]: ""}
            #     })
            # headers = {
            #     'Key': self.keys[idx],
            #     'Content-Type': 'application/json'
            # }
            # response = requests.request(self.methods[idx], self.urls[idx], headers=headers, data=payload)
