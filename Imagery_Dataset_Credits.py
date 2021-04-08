#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Simple imagery object
class produit_imagerie(object):
    def __init__(self, platform = None, level = None, source = None, processing = None):
        self.platform   = platform
        self.level      = level
        self.source     = source
        self.processing = processing


# In[11]:


# List of recognized cases
list_of_allowed_cases = []
list_of_allowed_cases.append(produit_imagerie('Pleiades', 'Image', 'Dinamis', [None]))
list_of_allowed_cases.append(produit_imagerie('Pleiades', 'Image', 'Dinamis', ['Home']))
list_of_allowed_cases.append(produit_imagerie('Pleiades', 'Image', 'CIEST2', ['Home']))
list_of_allowed_cases.append(produit_imagerie('Pleiades', 'Pleiades_DEM', 'Dinamis', ['MicMac']))
list_of_allowed_cases.append(produit_imagerie('Pleiades', 'Pleiades_DEM', 'Dinamis', ['S-CAPAD']))
list_of_allowed_cases.append(produit_imagerie('Pleiades', 'Pleiades_DEM', 'Dinamis', ['S-CAPAD','MicMac']))
list_of_allowed_cases.append(produit_imagerie('Pleiades', 'Pleiades_DEM', 'Dinamis', ['GDM-Opt']))
list_of_allowed_cases.append(produit_imagerie('Sentinel-1', 'SLC', 'PEPS', [None]))
list_of_allowed_cases.append(produit_imagerie('Sentinel-1', 'SLC', 'PEPS', ['Home']))
list_of_allowed_cases.append(produit_imagerie('Sentinel-1', 'SLC', 'Flatsim', [None]))
    
# List of allowed platforms
list_of_allowed_platforms = set()
print("List of recognized cases : ")
for mycase in list_of_allowed_cases:
    print(" ",mycase.platform, mycase.level, mycase.source, mycase.processing)
    list_of_allowed_platforms.add(mycase.platform)
    
print('List of plaforms : ', list_of_allowed_platforms)


# In[3]:


# List of acknowledgements
dict_acknow = dict()
dict_acknow['Dinamis'] = 'Access to Pleiades data was granted through the DINAMIS program (https://dinamis.teledetection.fr/) via project ID 20XX-XX-XX (PI: YYYY, YYYY@myemail.fr).'
dict_acknow['Dinamis'] = 'Access to Pleiades data was granted through the CIEST2 program (https://www.poleterresolide.fr/ciest-2-nouvelle-generation-2/).'
dict_acknow['S-CAPAD'] = 'Calculation of the Pleiades DSM used the S-CAPAD cluster of IPGP.'
dict_acknow['Pleiades'] = 'The underlying dataset from which this work has been derived includes Pleiades material ©CNES (Year of image acquisition), distributed by AIRBUS DS.'
dict_acknow['Sentinel-1'] = 'The underlying dataset from which this work has been derived includes EO material ©CCME (Year of image acquisition), provided under COPERNICUS by the European Union and ESA.'


# In[14]:


# List of licences
dict_licenc = dict()
dict_licenc['Dinamis'] = 2
dict_licenc['Pleiades_DEM'] = 3
dict_licenc['Flatsim'] = 3
dict_licenc['GDMSAR'] = 2

# Meaning of the licence codes
codes_licenc = dict()
codes_licenc[0] = 'This dataset is licenced under a Creative Commons Zero (Public Domain).'
codes_licenc[1] = 'This dataset is licensed under a Creative Commons CC BY 4.0 International License (Attribution).'
codes_licenc[2] = 'This dataset is licensed under a Creative Commons CC BY-SA 4.0 International License (Attribution-ShareAlike).'
codes_licenc[3] = 'This dataset is licensed under a Creative Commons CC BY-NC 4.0 International License (Attribution-NonCommercial).'
codes_licenc[4] = 'This dataset is licensed under a Creative Commons CC BY-NC-SA 4.0 International License (Attribution-NonCommercial-ShareAlike).'
codes_licenc[5] = 'This dataset is licensed under a Creative Commons CC BY-ND 4.0 International License (Attribution-NoDerivatives).'
codes_licenc[6] = 'This dataset is licensed under a Creative Commons CC BY-NC-ND 4.0 International License (Attribution-NonCommercial-NoDerivatives).'


# In[5]:


# List of citations
dict_citation = dict()
dict_citation['Flatsim'] = 'Thollard et al. (2021).'
dict_citation['MicMac'] = 'Rupnik et al. (2017).'


# In[6]:


# Check whether your imagery object belongs to the list of recognized cases
class check_imagerie(object):

    # First, check the platform
    def get_platform(self):
        return self.__platform
    def set_platform(self, value):
        if value in list_of_allowed_platforms:
            self.__platform = value
        else:
            raise TypeError("Platform name can be %s" % list_of_allowed_platforms)
    platform = property(get_platform, set_platform)

    # Next, define the level
    def get_level(self):
        return self.__level
    def set_level(self, value):
        try:
            self.platform
        except:
            print("Please define a platform")
        else:
            list_of_allowed_levels = set()
            for mycase in list_of_allowed_cases:
                if mycase.platform == self.platform:
                    list_of_allowed_levels.add(mycase.level)
            if value in list_of_allowed_levels:
                self.__level = value
            else:
                raise TypeError("Level can be %s" % list_of_allowed_levels)
    level = property(get_level, set_level)

    # Then, tell us from what source you got the data
    def get_source(self):
        return self.__source
    def set_source(self, value):
        try:
            self.level
        except:
            print("Please define a level")
        else:
            list_of_allowed_sources = set()
            for mycase in list_of_allowed_cases:
                if mycase.platform == self.platform and mycase.level == self.level:
                    list_of_allowed_sources.add(mycase.source)
            if value in list_of_allowed_sources:
                self.__source = value
            else:
                raise TypeError("Source can be %s" % list_of_allowed_sources)
    source = property(get_source, set_source)

    # Finally, mention if you applied some processing to the data
    def get_processing(self):
        return self.__processing
    def set_processing(self, value):
        try:
            self.source
        except:
            print("Please define a source")
        else:
            list_of_allowed_processings = set()
            for mycase in list_of_allowed_cases:
                if mycase.platform == self.platform and mycase.level == self.level and mycase.source == self.source:
                    for my_processing in mycase.processing:
                        list_of_allowed_processings.add(my_processing)
            if set(value).issubset(list_of_allowed_processings):
                self.__processing = value
            else:
                raise TypeError("Processing can be %s" % list_of_allowed_processings)
    processing = property(get_processing, set_processing)
    
    def get_acknowledgments_licence(self):
        try:
            self.source; self.processing;
        except:
            print("Not all attributes have been set...")
        else:
            licence = set(); ackowledgement = set(); citation = set();
            for mycase in list_of_allowed_cases:
                if mycase.platform == self.platform:
                    if self.platform in dict_acknow:
                        ackowledgement.add(dict_acknow[self.platform])
                    if self.platform in dict_licenc:
                        licence.add(dict_licenc[self.platform])
                    if self.platform in dict_citation:
                        citation.add(dict_citation[self.platform])
                if mycase.level == self.level:
                    if self.level in dict_acknow:
                        ackowledgement.add(dict_acknow[self.level])
                    if self.level in dict_licenc:
                        licence.add(dict_licenc[self.level])
                    if self.level in dict_citation:
                        citation.add(dict_citation[self.level])
                if mycase.source == self.source:
                    if self.source in dict_acknow:
                        ackowledgement.add(dict_acknow[self.source])
                    if self.source in dict_licenc:
                        licence.add(dict_licenc[self.source])
                    if self.source in dict_citation:
                        citation.add(dict_citation[self.source])
                if set(mycase.processing).issubset(set(self.processing)):
                    if set(mycase.processing).issubset(set(dict_acknow.keys())):
                        for myprocessing in mycase.processing:
                            ackowledgement.add(dict_acknow[myprocessing])
                    if set(mycase.processing).issubset(set(dict_licenc.keys())):
                        for myprocessing in mycase.processing:
                            licence.add(dict_licenc[myprocessing])
                    if set(mycase.processing).issubset(set(dict_citation.keys())):
                        for myprocessing in mycase.processing:
                            citation.add(dict_citation[myprocessing])
            if len(licence)>0: print('Licence : \n',codes_licenc[max(licence)]) # Take the most restrictive licence
            if len(ackowledgement)>0: print('Acknowledgement : \n'," ".join(ackowledgement))
            if len(citation)>0: print('Citation : \n'," ".join(citation))


# In[7]:


# What licence / acknowledgements do I need for my case?
x = check_imagerie();
x.platform = 'Pleiades'; x.level = 'Pleiades_DEM'; x.source = 'Dinamis'; x.processing = ['S-CAPAD']; #print(x.__dict__);
x.get_acknowledgments_licence()


# In[8]:


# What licence / acknowledgements do I need for my case?
x = check_imagerie();
x.platform = 'Pleiades'; x.level = 'Pleiades_DEM'; x.source = 'Dinamis'; x.processing = ['S-CAPAD','MicMac']; #print(x.__dict__);
x.get_acknowledgments_licence()


# In[15]:


# What licence / acknowledgements do I need for my case?
x = check_imagerie();
x.platform = 'Sentinel-1'; x.level = 'Pleiades_DEM'; x.source = 'Dinamis'; x.processing = ['S-CAPAD','MicMac']; #print(x.__dict__);
x.get_acknowledgments_licence()


# In[16]:


# What licence / acknowledgements do I need for my case?
x = check_imagerie();
x.platform = 'Sentinel-1'; x.level = 'SLC'; x.source = 'Flatsim'; x.processing = [None]; #print(x.__dict__);
x.get_acknowledgments_licence()


# In[ ]:




