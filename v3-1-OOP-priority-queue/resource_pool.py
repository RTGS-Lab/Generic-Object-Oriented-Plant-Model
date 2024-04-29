'''
resource_pool.py is a base class for any resource pool in a plant.
This can be as general as a phytomer or as specific as a fine root.
Some examples of resource pools are: leaf, canopy, roots, stem, seed,
ear, cob, silk, tassel, fruit, branch, spines, tubers, flowers, stolon,
'reserve', tiller, sub-tending leaves, panicle, fine roots, coarse roots, nodule,
top leaves, bottom leaves, flag leaves, etc.

As a base class or interface class, this is intended to be subclassed
into a specific, identifiable resource pool for a plant scientists research area
and coupled with a specific species specific allocation routine held in the plant.py
class. See more details on allocation routines in plant.py.

Authors: Bryan C. Runck, Diane Wang, Sajad Jamshidi (co-coded live)
'''

class resource_pool(object):

    def __init__(self):
        
        #### PRIMARY BASE RESOURCES IN PLANT PARTS ####
        '''
        We selected carbon and nitrogen as the most important elements making up a plant.
        Carbon is a major part of cell walls and structural biomass, and nitrogen 
        makes up rubisco, the most abundant protein on the planet. Carbon and nitrogen
        need to be tightly coordinated for central metabolism driving plant growth and development.

        It's easy to add other elements in sub-classing for specific studies.
        '''
        self.carbon = None # grams / m^2; carbon is the same as assimilate for our purposes
        self.nitrogen = None # grams / m^2; the same caveates exist here as described for carbon

        '''
        Carbon unit mass per ground area -- this is a difficult variable from a units perspective
        because the base physiological models used in the plant class are on a per unit area basis
        e.g. g/m^2, but when we think about a resource pool in a plant, like a stem, it makes
        more sense to talk about grams of carbon or carbon concentration in the biomass. For simplicity
        and parsimony with current physiological models, we chose to retain the mass/ground area, but
        recognize this as an area for potential improvements in the future to increase the fidelity of
        the representation between the model and actual measures in field and greenhouse.

        The simple work around to get to a per unit plant is to assume an area for a plant and
        then calculate the per unit plant based on this assumption. In other words, plant density per hectare
        becomes hectares per plant.
        '''


        #### TIME REPRESENTATION ####
        ''' Time is kept track of both at the plant-level as well as the specific organ-level.'''
        self.plant_age = 0 #centralized time for the plant object; biological time, most often in thermal units
        self.resource_pool_age = None # localized time for the resource_pool; biological time based on age of resource pool
        self.resource_pool_age_history = None # instrumentation variable to ensure sensible progression

        #### PULL STRENGTH FROM CENTRAL PLANT RESOURCES ####
        self.sink_strength = None # set based on set_sink_strength method




    def set_sink_strength(self):
        '''
        User will specify method for setting the sink strength determining
        the proportion of central plant carbon and nitrogen flowing to the resource pool.
        '''
        pass

    def step(self, plant_age):
        ''' Advances time, however defined by user. '''
        self.plant_age = plant_age # pass in from plant
        self.resource_pool_age_step()


    def resource_pool_age_step(self):
        ''' insert code here for updating pool age '''
        self.resource_pool_age = None
        self.resource_pool_age_history.append(self.resource_pool_age)
        pass


