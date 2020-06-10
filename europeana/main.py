from europeana.api import EuropeanaAPI
from europeana.responses import Description
#from EuAPI.EuropeanaAPI import EuropeanaAPI


def main():

  eu = EuropeanaAPI('xCQ6FUorp')


  
  #print(help(eu.search))
  #r = eu.search('Amsterdam',  n = 249, sort = 'score',  theme = 'nature')
  
  #r = eu.search('Amsterdam',  n = 249, sort = {'term':'score','order':'asc'},  theme = 'nature')

  r = eu.search('Amsterdam', n = 100,sort = {'term':'score','order':'asc'},  theme = 'nature')
  #print(r['success'])
  print(r.success)

  if r.success:
    for edm in r.edm_items:


      # print(edm.dcTitleLangAware)
      # number of languages
      # print(len(edm.dcTitleLangAware.keys()))
      # languages
      # print(edm.dcTitleLangAware.keys())

      #print(edm.dcDescriptionLangAware)
      if edm.dcDescriptionLangAware:
        #print(len(edm.dcDescriptionLangAware.keys()))
        #print(edm.dcDescriptionLangAware.keys())
        d = Description(edm.dcDescriptionLangAware)
        print(d.lang)

        for l in d.lang:
          print(d[l][0])
        #print(d[])



      # print(edm.edmPlaceLabelLangAware)



  # print(r.api_response.keys())
  # print(r.api_response['error'])

  #print(r.keys())

  #print(r['n'])
  #print(len(r['items']))
  #print(r['totalResults'])


  # print('total number of results: {}'.format(r.totalResults))
  # print('parameters: {}'.format(r.params))
  # print('number of EDM objects: {}'.format(r.num_items))

  # for edm in r.edm_items[:10]:
  #   print(edm.thumbnail_url)
  #   # print(edm.id)
  #   # record_response = eu.record(edm.id)

  # countries = {}
  # for edm in r.edm_items:
  #   if edm.country not in countries.keys():
  #     countries.update({edm.country:1})
  #   else:
  #     countries[edm.country] += 1


  # years = {}
  # for edm in r.edm_items:
  #   if edm.year not in years.keys():
  #     years.update({edm.year:1})
  #   else:
  #     years[edm.year] += 1

  # print(countries)
  # print(years)

      
  #img_id = '/2064107/Museu_ProvidedCHO_Museum_of_English_Rural_Life__University_of_Reading_4966'
  #record_response = eu.record(img_id)
