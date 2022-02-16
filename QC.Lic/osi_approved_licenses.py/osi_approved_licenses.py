#!/usr/bin/env python

import requests


ENDPOINT = 'https://api.opensource.org/licenses/osi-approved'

r = requests.get(ENDPOINT)
r.raise_for_status()
print(r.json())
