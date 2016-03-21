# -*- coding: utf-8 -*-
"""
Created on Wed Mar 02 15:09:14 2016

@author: Administrator

•Imports the libraries necessary to run the application
•Takes an image file and passes it to the main() function
•Gets credentials to run the Vision API service
•Reads the image and creates a request, encoding the image in base64
•Sends the request as a JSON request object to the service
•Parses the response for the first label description and displays it to the user.

"""

import argparse
import base64
import httplib2

from apiclient.discovery import build
from oauth2client.client import GoogleCredentials

def main(photo_file) :
    ## 2. Authenticating
    API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'
    http = httplib2.Http()
    print http 
    
    credentials = GoogleCredentials.get_application_default()
    ##.create_scoped(['https://www.googleapis.com/auth/cloud-platform'])
    ## 
    
    print credentials 
    credentials.authorize(http)

    service = build('vision', 'v1', http, discoveryServiceUrl = API_DISCOVERY_FILE)
    
    ##### 
    
    ## 3. Constructing the Request 
    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.image().annotate(body={'requests': [{'image': {'content': image_content},'features': [{'type': 'LABEL_DETECTION','maxResults': 1,}]}]})
      
      
      ## Parsing the Respnse
      
    response = service_request.execute()
    label = response['response'][0]['labelAnnotations'][0]['description']
    print 'Found Label : %s for %s ' % (label, photo_file)
    return 0

## 1. Running Application
if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help = 'The image you \'d like to label.')
    args = parser.parse_args()
    main(args.image_file)
    

    