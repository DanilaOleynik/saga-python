
import saga.cpi.base
import saga.cpi.context

SYNC  = saga.cpi.base.sync
ASYNC = saga.cpi.base.async

######################################################################
#
# adaptor meta data
#
_adaptor_name     =    'saga.adaptor.saga_adaptor_context_myproxy'
_adaptor_registry = [{ 'name'    : _adaptor_name,
                       'type'    : 'saga.Context',
                       'class'   : 'ContextMyProxy',
                       'schemas' : ['MyProxy']
                     }]


######################################################################
#
# adaptor registration
#
def register () :

    # perform some sanity checks, like check if dependencies are met
    return _adaptor_registry


######################################################################
#
# job adaptor class
#
class ContextMyProxy (saga.cpi.Context) :

    def __init__ (self, api) :
        saga.cpi.Base.__init__ (self, api, _adaptor_name)
        # print "myproxy context adaptor init"


    @SYNC
    def init_instance (self, type) :
        # print "myproxy context adaptor instance init sync %s" % id
        self._api.type = type


    @SYNC
    def set_defaults (self) :

        # make sure we have server, username, password
        api = self._get_api ()

        print "type:   %s"  %  api.type
        print "user:   %s"  %  api.user_id
        print "pass:   %s"  %  api.user_pass
        print "server: %s"  %  api.server
        print "ttl:    %s"  %  api.life_time
        pass



# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

