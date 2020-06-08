from .edm import EDM

class SearchResponse:
    def __init__(self,response, query, **kwargs):

        self.api_response = response
        self.items = response['items']

        self.totalResults = response['totalResults']
        self.edm_items = [EDM(item) for item in self.items]
        self.num_items = len(self.edm_items)

        self.query = query
        self.params = kwargs
        self.params.update({'n':response['n']})
        self.params.update({'start':response['start']})


        
        






        