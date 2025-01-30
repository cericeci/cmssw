#ifndef RecoVertex_PortablePrimaryVertexProducer_interface_ClusterParamsHostCollection_h
#define RecoVertex_PortablePrimaryVertexProducer_interface_ClusterParamsHostCollection_h

#include "DataFormats/Portable/interface/PortableHostCollection.h"
#include "RecoVertex/PortablePrimaryVertexProducer/interface/ClusterParamsSoA.h"


// SoA with x, y, z, id fields in host memory
using ClusterParamsHostCollection = PortableHostCollection<ClusterParamsSoA>;

#endif 
