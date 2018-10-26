import pulumi
import pulumi.runtime

class PriorityClassList(pulumi.CustomResource):
    """
    PriorityClassList is a collection of priority classes.
    """
    def __init__(self, __name__, __opts__=None, items=None, metadata=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'scheduling.k8s.io/v1alpha1'
        self.apiVersion = 'scheduling.k8s.io/v1alpha1'

        __props__['kind'] = 'PriorityClassList'
        self.kind = 'PriorityClassList'

        if not items:
            raise TypeError('Missing required property items')
        elif not isinstance(items, list):
            raise TypeError('Expected property aliases to be a list')
        self.items = items
        """
        items is the list of PriorityClasses
        """
        __props__['items'] = items

        if metadata and not isinstance(metadata, dict):
            raise TypeError('Expected property aliases to be a dict')
        self.metadata = metadata
        """
        Standard list metadata More info:
        http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#metadata
        """
        __props__['metadata'] = metadata

        super(PriorityClassList, self).__init__(
            "kubernetes:scheduling.k8s.io/v1alpha1:PriorityClassList",
            __name__,
            __props__,
            __opts__)
