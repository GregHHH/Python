import requests

def strapiLogin(id,password):
    myToken = '<token>'
    myUrl = 'http://146.59.225.32'
    head = {'Authorization: Bearer ${JWT}'}
    response = requests.get(myUrl, headers=head)
    response_json = response.json()
    return response_json['jwt']

