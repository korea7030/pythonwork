import json
import requests
import lxml.html
from bs4 import BeautifulSoup


url = "https://patents.google.com/xhr/query?url=country%3DWO%26language%3DKOREAN%26type%3DPATENT%26" \
      "oq%3Dcountry%3AWO%2Blanguage%3AKOREAN%2Btype%3APATENT%2B%26page%3D"

req = requests.get(url+str(0))
total_page = json.loads(req.text)['results']['total_num_pages']

for page in range(0, total_page+1):
    print(url+str(page))
    req = requests.get(url + str(page))
    json_data = json.loads(req.text)['results']['cluster'][0].get('result')

    # print(json_data)
    content_url = "https://patents.google.com/patent/"

    publication_numbers = []
    publication_numbers_en = []
    for data in json_data:
        # print(data['patent']['publication_number'])
        publication_numbers.append(content_url + data['patent']['publication_number'])
        publication_numbers_en.append(content_url + data['patent']['publication_number']+'/en')

    patent_req = None
    for i in range(len(publication_numbers)):
        print(publication_numbers[i])
        patent_req_ko = requests.get(publication_numbers[i])
        patent_req_ko.encoding = 'utf-8'
        patent_req_en = requests.get(publication_numbers_en[i])
        patent_req_en.encoding = 'utf-8'

        if (patent_req_ko.status_code == 200):
            patent_ko_content = lxml.html.fromstring(patent_req_ko.text)
            abstract_ko = patent_ko_content.find_class('abstract')[0].text
            description_ko = patent_ko_content.find_class('description')[0].text_content()
            claims_ko = patent_ko_content.find_class('claims')[0].text_content()

            print(abstract_ko)

            with open(publication_numbers[i].split('/')[-1]+"_ko.tsv", 'w+') as f:
                f.write(abstract_ko+'\t'+description_ko+'\t'+claims_ko+'\n')

        if (patent_req_en.status_code == 200):
            patent_en_content = lxml.html.fromstring(patent_req_en.text)
            abstract_en = patent_en_content.find_class('abstract')[0].text
            description_en = patent_en_content.find_class('description')[0].text_content()
            claims_en = patent_en_content.find_class('claims')[0].text_content()

            with open(publication_numbers[i].split('/')[-1] + "_en.tsv", 'w+') as f:
                f.write(abstract_en + '\t' + description_en + '\t' + claims_en + '\n')

