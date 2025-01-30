#ifndef RecoVertex_PortablePrimaryVertexProducer_interface_alpaka_ClusterParamsDeviceCollection_h
#define RecoVertex_PortablePrimaryVertexProducer_interface_alpaka_ClusterParamsDeviceCollection_h

#include "RecoVertex/PortablePrimaryVertexProducer/interface/ClusterParamsHostCollection.h"
#include "DataFormats/Portable/interface/alpaka/PortableCollection.h"
#include "RecoVertex/PortablePrimaryVertexProducer/interface/ClusterParamsSoA.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"

namespace ALPAKA_ACCELERATOR_NAMESPACE {
  using ::ClusterParamsHostCollection;
  using ClusterParamsDeviceCollection = PortableCollection<ClusterParamsSoA>;
}
#endif  // 
