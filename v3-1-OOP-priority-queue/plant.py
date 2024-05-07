'''
plant.py is the interface class that needs to be sub-classed for
specific species/cultivars to hold plant-level pools that
are allocated into (or taken from) for the resource pools at
each time step. In this version, the plant object is a priority
queue of resource_pools. In other words, the plant is composed
of resource pools of specific types.

To use this class, you first need to specify your growth and development
for your specific species or cultivar. You do this by sub-classing resource_pool.py.

Then, you create a priority queue in the plant by defining a dictionary that
defines what order each resource pool can access the plant's central resources
at each time step.

Authors: Bryan C. Runck, Diane Wang, Sajad Jamshidi
'''

class plant(object):

    def __init__(self):
        self.resource_pools = [] # list of resource pools in priority order; 
                                 # constructed in method construct_resource_pools()
        
        self.plant_age = 0 # most often defined by thermal time; passed into resource units
        
        #### CENTRAL POOL OF RESOURCES AVAILABLE TO RESOURCE POOLS ####
        ''' 
        Major physiological process are represented at the plant or canopy level.
        For this reason, we store centralized pools that resource units use to
        progress through growth and development.
        '''
        self.carbon = 0 # central carbon available at time step t; # grams / m^2; 
                        # grams / m^2; carbon is the same as assimilate for our purposes
        self.carbon_history = [] # plant-level history of carbon available at eaach time step
        self.nitrogen = 0 # central nitrogen available at time step t; # grams / m^2; 
        self.nitrogen_history = [] # plant-level history of nitrogen available at each time step; 
                                   # grams / m^2
	


        '''Water status? Or water? Operates differently from C/N. Water is a flux.'''
        self.water = 1 # scalar for other processes in this version ranges from 0-1; often calculated proportional to need
        self.water_history = [] # history of water scalar

	'''Water? Turgor-driven(sp?) growth; expansive growth; water entrance into plant at time step t
           Water used in modeling typically as a trigger for "stress" which is a limit on photosysnthesis
           and transpiration, which ultimately limits stored carbon. Can track stem or leaf water potential.
           Follow flow of water based on resistances.

           Scalar used for water. This gets updated at each time step and affects uptake.
        '''

        #### ENVIRONMENT-DERIVED INPUTS ####
        ''' '''
        self.absorbed_PAR = 0 # W/m^2 ground area/hour
        self.absorbed_PAR_history = [] # history of PAR readings
        self.temperature = 0 # degrees C; leaf or plant temperature
        self.temperature_history = [] # history of leaf or plant temperatures


        def construct_resource_pools(self, pools):
            pass


        def step(self):
            self.photosynthesize()
            self.transpire()


        def calculate_assimilates(self):
        ''' To be defined for specific case; could be photosynthesis or radiation use efficiency'''
            pass


        def calculate_water_flux(self):
        ''' To be defined for specific case'''
            pass
