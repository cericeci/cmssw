#ifndef DataFormats_PortableVertex_interface_TestHostCollection_h
#define DataFormats_PortableVertex_interface_TestHostCollection_h

#include "DataFormats/Portable/interface/PortableHostCollection.h"
#include "DataFormats/PortableVertex/interface/VertexSoA.h"

namespace portablevertex {

  // SoA with x, y, z, id fields in host memory
  using VertexHostCollection = PortableHostCollection<VertexSoA>;
  using TrackHostCollection  = PortableHostCollection<TrackSoA>;

}  // namespace portabletest

#endif  // DataFormats_PortableVertex_interface_TestHostCollection_h
