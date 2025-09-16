# Sooji Kim
# CS5700 Fall25
# HW 4
# 14 September 2025

# Client for requesting html/json from a server

import http.client
import sys

def get_resource(resource):

    conn = http.client.HTTPConnection('localhost', 8070)
    conn.request('GET', resource)
    response = conn.getresponse()
    data = response.read()

    status_code = response.status
    content_type = response.headers.get('content-type')
    content = data.decode('utf-8')

    print(f"Response Status Code: {status_code}")
    print(f"Content Type: {content_type}")
    print("Response Content:")
    print(content)

    conn.close()

get_resource(sys.argv[1])