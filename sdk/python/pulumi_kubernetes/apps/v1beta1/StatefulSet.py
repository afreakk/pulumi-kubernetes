import pulumi
import pulumi.runtime

from ... import tables

class StatefulSet(pulumi.CustomResource):
    """
    DEPRECATED - This group version of StatefulSet is deprecated by apps/v1beta2/StatefulSet. See
    the release notes for more information. StatefulSet represents a set of pods with consistent
    identities. Identities are defined as:
     - Network: A single stable DNS and hostname.
     - Storage: As many VolumeClaims as requested.
    The StatefulSet guarantees that a given network identity will always map to the same storage
    identity.
    """
    def __init__(self, __name__, __opts__=None, metadata=None, spec=None, status=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'apps/v1beta1'
        __props__['kind'] = 'StatefulSet'
        __props__['metadata'] = metadata
        __props__['spec'] = spec
        __props__['status'] = status

        super(StatefulSet, self).__init__(
            "kubernetes:apps/v1beta1:StatefulSet",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
