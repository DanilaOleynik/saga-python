
import saga.attributes
import saga.exceptions as se
import constants       as const

#-------------------------------------------------------------------------------
#
class Description (saga.attributes.Attributes) :
    """ 
    The resource description class. 

    Resource descriptions are used for two purposes:

      * an application can pass :class:`saga.resource.Description` instances to
        a :class:`saga.resource.Manager` instance, to request control over the
        resource slice described in the description; 

      * an application requests a resource's description for inspection of
      * resource properties.

    
    """

    # --------------------------------------------------------------------------
    #
    def __init__(self, d=None):

        # set attribute interface properties

        import saga.attributes as sa

        self._attributes_extensible  (False)
        self._attributes_camelcasing (True)

        # register properties with the attribute interface

        self._attributes_register  (const.RTYPE       , None , sa.ENUM  , sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.TEMPLATE    , None , sa.STRING, sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.IMAGE       , None , sa.STRING, sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.DYNAMIC     , False, sa.BOOL  , sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.START       , None , sa.TIME  , sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.END         , None , sa.TIME  , sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.DURATION    , None , sa.TIME  , sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.MACHINE_OS  , None , sa.STRING, sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.MACHINE_ARCH, None , sa.STRING, sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.SIZE        , 1    , sa.INT   , sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.MEMORY      , None , sa.STRING, sa.SCALAR, sa.WRITEABLE) 
        self._attributes_register  (const.ACCESS      , None , sa.STRING, sa.SCALAR, sa.WRITEABLE) 

        self._attributes_set_enums (const.RTYPE, [const.COMPUTE ,
                                                  const.STORAGE ,
                                                  const.NETWORK ])

        # FIXME: initialization should be done in Attributes: initialization
        # from dict or from other attributable
        #
        if  d :
            for key in d.list_attributes () :
                self.set_attribute (key, d.get_attribute (key)) 


    # --------------------------------------------------------------------------
    #
    def __deepcopy__ (self, other) :
        return self.clone (other)

    # --------------------------------------------------------------------------
    #
    def clone (self, other=None) :
        """ 
        deep copy: unlike the default python assignment (copy object reference),
        a deep copy will create a new object instance with the same state --
        after a deep copy, a change on one instance will not affect the other.
        """

        # a job description only has attributes - so create a new instance,
        # clone the attribs, and done.
        if not other :
            other = saga.job.Description ()

        return self._attributes_deep_copy (other)


# ------------------------------------------------------------------------------
#
class ComputeDescription (Description) : 

    def __init__ (self, d=None) :
        
        if  d :
            if  const.RTYPE in d and d[const.RTYPE] != const.COMPUTE :
                raise se.BadParameter ("Cannot create ComputeResource with type '%s'" \
                                    % d[const.RTYPE])

        self._descr = super  (ComputeDescription, self)
        self._descr.__init__ (d)

        self.rtype = const.COMPUTE
        self.set_attribute (const.RTYPE, const.COMPUTE)

        self._attributes_dump ()


# ------------------------------------------------------------------------------
#
class StorageDescription (Description) :

    def __init__ (self, d=None) :
        
        if  d :
            if  const.RTYPE in d and d[const.RTYPE] != const.STORAGE :
                raise se.BadParameter ("Cannot create StorageResource with type '%s'" \
                                    % d[const.RTYPE])

        self._descr = super  (StorageDescription, self)
        self._descr.__init__ (d)

        self.rtype = const.STORAGE


# ------------------------------------------------------------------------------
#
class NetworkDescription (Description) :

    def __init__ (self, d=None) :
        
        if  d :
            if  const.RTYPE in d and d[const.RTYPE] != const.NETWORK :
                raise se.BadParameter ("Cannot create NetworkResource with type '%s'" \
                                    % d[const.RTYPE])

        self._descr = super  (NetworkDescription, self)
        self._descr.__init__ ()

        self.rtype = const.NETWORK



# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
