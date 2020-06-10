from .edm import EDM



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


        
            


        
        






        