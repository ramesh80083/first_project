class apitext:
    def __int__(self,api_url,body,headers):
        self.api_url=api_url
        self.body=body
        self.headers=headers
    def response(self):
        res= requests.post(self.api_url,self.body,self.headers,data,auth=("admin","FGf6L*8P$lxt"))
        return response.json()
        # object initiated
obj1 =apitext("https://dev85426.service-now.com/api/now/table/incident"),
      body={"caller_id": "ramesh123","description": "money deducted","short_description": "ticket creation testing from postman"},
      {"accept": "application/json","content-type": "application/json"}
obj1.response()
print(obj1.response())
