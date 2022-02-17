// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Kubernetes.Types.Outputs.Core.V1
{

    /// <summary>
    /// Represents a Glusterfs mount that lasts the lifetime of a pod. Glusterfs volumes do not support ownership management or SELinux relabeling.
    /// </summary>
    [OutputType]
    public sealed class GlusterfsPersistentVolumeSource
    {
        /// <summary>
        /// endpoints is the endpoint name that details Glusterfs topology. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
        /// </summary>
        public readonly string Endpoints;
        /// <summary>
        /// endpointsNamespace is the namespace that contains Glusterfs endpoint. If this field is empty, the EndpointNamespace defaults to the same namespace as the bound PVC. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
        /// </summary>
        public readonly string EndpointsNamespace;
        /// <summary>
        /// path is the Glusterfs volume path. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
        /// </summary>
        public readonly string Path;
        /// <summary>
        /// readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod
        /// </summary>
        public readonly bool ReadOnly;

        [OutputConstructor]
        private GlusterfsPersistentVolumeSource(
            string endpoints,

            string endpointsNamespace,

            string path,

            bool readOnly)
        {
            Endpoints = endpoints;
            EndpointsNamespace = endpointsNamespace;
            Path = path;
            ReadOnly = readOnly;
        }
    }
}
