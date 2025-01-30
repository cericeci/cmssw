#ifndef DataFormats_PortableVertex_interface_TrackForVertexHostCollection_h
#define DataFormats_PortableVertex_interface_TrackForVertexHostCollection_h

#include "DataFormats/Portable/interface/PortableHostCollection.h"
#include "DataFormats/PortableVertex/interface/TrackForVertexSoA.h"

namespace portablevertex {

  // SoA with x, y, z, id fields in host memory
  using TrackForVertexHostCollection = PortableHostCollection<TrackForVertexSoA>;
}  // namespace portablevertex

#endif  // DataFormats_PortableVertex_interface_TrackForVertexVertexHostCollection_h
