from .edm import EDM


class Description(dict):

    def __init__(self,desc,**kw):
        super(Description, self).__init__(desc, **kw)
        
        #print(arg)

        if not isinstance(desc,dict):
            raise ValueError('Europeana API: desc must be a dictionary')
      
        #self = desc.copy()
        self.lang = list(desc.keys())

    # def __str__(self):
    #     return ''


class SearchResponse:
    def __init__(self,response, query, **kwargs):

        # query attributes
        self.query = query
        self.params = kwargs

        # response attributes
        self.api_response = response
        self.success = response['success']

        self.items = None
        self.num_items = None
        self.edm_items = None
        self.totalResults = None

        if self.success:
            self.items = response['items']
            self.num_items = len(self.items)
            self.edm_items = [EDM(item) for item in self.items]
            self.totalResults = response['totalResults']


        
            


        
        






        