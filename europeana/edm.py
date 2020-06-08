class EDM:
  def __init__(self,edm_object):

    self.completeness = None
    if 'completeness' in edm_object:
      self.completeness = edm_object['completeness']

    self.country = None
    if 'country' in edm_object:
      self.country = edm_object['country'][0]

    self.dataProvider = None
    if 'dataProvider' in edm_object:
      self.dataProvider = edm_object['dataProvider'][0]

    self.dcDescriptionLangAware = None
    if 'dcDescriptionLangAware' in edm_object:
      self.dcDescriptionLangAware = edm_object['dcDescriptionLangAware']

    self.dcLanguage = None
    if 'dcLanguage' in edm_object:
      self.dcLanguage = edm_object['dcLanguage']

    self.dcTitleLangAware = None
    if 'dcTitleLangAware' in edm_object:
      self.dcTitleLangAware = edm_object['dcTitleLangAware']

    self.edmDatasetName = None
    if 'edmDatasetName' in edm_object:
      self.edmDatasetName = edm_object['edmDatasetName']


    self.edmIsShownBy = None
    self.media_url = None
    if 'edmIsShownBy' in edm_object:
      self.edmIsShownBy = edm_object['edmIsShownBy']
      self.media_url = self.edmIsShownBy[0]
    
    self.edmIsShownAt = None
    self.provider_url = None
    if 'edmIsShownAt' in edm_object:
      self.edmIsShownAt = edm_object['edmIsShownAt']
      self.provider_url = self.edmIsShownAt[0]

    self.edmPreview = None
    self.thumbnail_url = None
    if 'edmPreview' in edm_object:
      self.edmPreview = edm_object['edmPreview']
      self.thumbnail_url = self.edmPreview[0]

    self.edmPlaceLabelLangAware = None
    if 'edmPlaceLabelLangAware' in edm_object:
      self.edmPlaceLabelLangAware = edm_object['edmPlaceLabelLangAware']

    self.year = None
    if 'year' in edm_object:
      self.year = edm_object['year'][0]

    self.rights_url = None
    if 'rights' in edm_object:
      self.rights_url = edm_object['rights'][0]

    self.id = None
    if 'id' in edm_object:
      self.id = edm_object['id']

    self.type = None
    if 'type' in edm_object:
      self.type = edm_object['type']
