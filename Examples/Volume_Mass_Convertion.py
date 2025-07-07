import requests
import json

url = "https://23.api3.lotus-uems.ru/sthe/api/v2.0/task_create"

headers = {
  'Authorization': 'Bearer 12345',
  'Content-Type': 'application/json'
}

payload = {
  "method": "flow_conversion",
  "data": {
    "V": 2500,
    "Vmode": "normal",
    "UserInput": {
      "flow_name": "Dried gas",
      "t_in": 20,
      "t_out": 45,
      "P_ab": 5101.325,
      "G": 4629,
      "components": [
        {
          "name": "Nitrogen / N2 / N2",
          "fraction": 0.002
        },
        {
          "name": "Methane / C1 / CH4",
          "fraction": 0.881
        },
        {
          "name": "Ethane / C2 / C2H6",
          "fraction": 0.117
        }
      ],
      "property_package": "prsv",
      "fraction_type": "mass",
      "P_drop": 50,
      "distillation": [
        {"temperature": 100, "fraction": 0.005},
        {"temperature": 110, "fraction": 0.012},
        {"temperature": 120, "fraction": 0.014},
        {"temperature": 130, "fraction": 0.025},
        {"temperature": 140, "fraction": 0.054}
      ]
    }
  }
}

response = requests.post(url, headers=headers, json=payload)

response.text
