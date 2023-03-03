#ifndef DataFormats_PortableVertex_interface_alpaka_VertexDeviceCollection_h
#define DataFormats_PortableVertex_interface_alpaka_VertexDeviceCollection_h

#include "DataFormats/Portable/interface/alpaka/PortableCollection.h"
#include "DataFormats/PortableVertex/interface/VertexSoA.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"

namespace ALPAKA_ACCELERATOR_NAMESPACE {

  namespace portablevertex {

    // make the names from the top-level portabletest namespace visible for unqualified lookup
    // inside the ALPAKA_ACCELERATOR_NAMESPACE::portabletest namespace
    using namespace ::portablevertex;

    // SoA with x, y, z, id fields in device global memory
    using VertexDeviceCollection = PortableCollection<VertexSoA>;
    using TrackDeviceCollection = PortableCollection<TrackSoA>;
  }  // namespace portabletest

}  // namespace ALPAKA_ACCELERATOR_NAMESPACE

#endif  // DataFormats_PortableVertex_interface_alpaka_VertexDeviceCollection_h
