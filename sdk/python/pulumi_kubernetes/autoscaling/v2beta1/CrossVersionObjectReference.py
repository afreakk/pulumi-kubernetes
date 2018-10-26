import pulumi
import pulumi.runtime

class CrossVersionObjectReference(pulumi.CustomResource):
    """
    CrossVersionObjectReference contains enough information to let you identify the referred
    resource.
    """
    def __init__(self, __name__, __opts__=None, name=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'autoscaling/v2beta1'
        self.apiVersion = 'autoscaling/v2beta1'

        __props__['kind'] = 'CrossVersionObjectReference'
        self.kind = 'CrossVersionObjectReference'

        if not name:
            raise TypeError('Missing required property name')
        elif not isinstance(name, str):
            raise TypeError('Expected property aliases to be a str')
        self.name = name
        """
        Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names
        """
        __props__['name'] = name

        super(CrossVersionObjectReference, self).__init__(
            "kubernetes:autoscaling/v2beta1:CrossVersionObjectReference",
            __name__,
            __props__,
            __opts__)
