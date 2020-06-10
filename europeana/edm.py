class EDM:
  def __init__(self,edm_object):
    

    # edm attributes
    self.completeness = None
    self.country = None
    self.dataProvider = None
    self.dcDescriptionLangAware = None
    self.dcLanguage = None
    self.dcTitleLangAware = None
    self.edmDatasetName = None
    self.edmIsShownBy = None
    self.edmIsShownAt = None
    self.edmPreview = None
    self.type = None
    self.id = None
    self.edmPlaceLabelLangAware = None
    self.year = None

    # own attributes
    self.media_url = None
    self.provider_url = None
    self.thumbnail_url = None
    self.rights_url = None


    if 'completeness' in edm_object:
      self.completeness = edm_object['completeness']

    if 'country' in edm_object:
      self.country = edm_object['country'][0]
    
    if 'dataProvider' in edm_object:
      self.dataProvider = edm_object['dataProvider'][0]
    
    if 'dcDescriptionLangAware' in edm_object:
      self.dcDescriptionLangAware = edm_object['dcDescriptionLangAware']
    
    if 'dcLanguage' in edm_object:
      self.dcLanguage = edm_object['dcLanguage']
    
    if 'dcTitleLangAware' in edm_object:
      self.dcTitleLangAware = edm_object['dcTitleLangAware']
    
    if 'edmDatasetName' in edm_object:
      self.edmDatasetName = edm_object['edmDatasetName']

    if 'edmIsShownBy' in edm_object:
      self.edmIsShownBy = edm_object['edmIsShownBy']
      self.media_url = self.edmIsShownBy[0]
    
    if 'edmIsShownAt' in edm_object:
      self.edmIsShownAt = edm_object['edmIsShownAt']
      self.provider_url = self.edmIsShownAt[0]

    if 'edmPreview' in edm_object:
      self.edmPreview = edm_object['edmPreview']
      self.thumbnail_url = self.edmPreview[0]

    if 'edmPlaceLabelLangAware' in edm_object:
      self.edmPlaceLabelLangAware = edm_object['edmPlaceLabelLangAware']

    if 'year' in edm_object:
      self.year = edm_object['year'][0]

    if 'rights' in edm_object:
      self.rights_url = edm_object['rights'][0]

    if 'id' in edm_object:
      self.id = edm_object['id']

    if 'type' in edm_object:
      self.type = edm_object['type']
