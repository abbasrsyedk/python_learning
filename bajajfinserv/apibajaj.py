import requests
import json
import base64

stringpwd = "rskabbas@outlook.com"
string1 = stringpwd.encode("ascii")
result = base64.b64encode(string1)
result1 = result.decode("ascii")

headers = {
    'Name': 'R S K ABBAS',
            'Email': 'rskabbas@outlook.com',
            'College': 'Vellore Institue of Technology-AP,Amaravati',
            'StudentId': '18BEC7011',
            'FileName': 'apibajaj.py',
            'Password': result1
}

response = requests.put(url="https://prod-24.centralindia.logic.azure.com/workflows/78d6df0ed1384ee0b7d04918f1a32b85/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=i6gXuS7-5_fFVf-0u8M4UfymINDULCMifsscfN5cPKM",
                        headers=headers, data=''.join(format(ord(i), '08b') for i in open('apibajaj.py').read()))

print(response.status_code)
print(response.content)
