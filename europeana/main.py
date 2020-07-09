from europeana.api import EuropeanaAPI
from europeana.edm import *
from europeana.utils import url2img
#from EuAPI.EuropeanaAPI import EuropeanaAPI


def main():

  eu = EuropeanaAPI('xCQ6FUorp')


  
  #print(help(eu.search))
  #r = eu.search('Amsterdam',  n = 249, sort = 'score',  theme = 'nature')
  
  #r = eu.search('Amsterdam',  n = 249, sort = {'term':'score','order':'asc'},  theme = 'nature')

  r = eu.search('Amsterdam', n = 5,sort = {'term':'score','order':'asc'},  what = 'painting')
  #print(r['success'])
  print(r.success)
  #print(r.api_response)

  if r.success:

    for i,edm in enumerate(r.edm_items):

      if edm.title:
        print(edm.title.lang)


