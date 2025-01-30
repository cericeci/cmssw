#ifndef DataFormats_PortableVertex_interface_alpaka_TrackForVertexDeviceCollection_h
#define DataFormats_PortableVertex_interface_alpaka_TrackForVertexDeviceCollection_h

#include "DataFormats/PortableVertex/interface/TrackForVertexHostCollection.h"
#include "DataFormats/Portable/interface/alpaka/PortableCollection.h"
#include "DataFormats/PortableVertex/interface/TrackForVertexSoA.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"

namespace ALPAKA_ACCELERATOR_NAMESPACE::portablevertex {

  // make the names from the top-level portablevertex namespace visible for unqualified lookup
  // inside the ALPAKA_ACCELERATOR_NAMESPACE::portablevertex namespace
  using ::portablevertex::TrackForVertexHostCollection;

  using TrackDeviceCollection = PortableCollection<::portablevertex::TrackForVertexSoA>;

}  // namespace ALPAKA_ACCELERATOR_NAMESPACE::portablevertex

#endif  // DataFormats_PortableVertex_interface_alpaka_TrackForVertexDeviceCollection_h
