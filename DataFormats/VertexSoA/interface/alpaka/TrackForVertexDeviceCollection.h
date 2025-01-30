#ifndef DataFormats_VertexSoA_interface_alpaka_TrackForVertexDeviceCollection_h
#define DataFormats_VertexSoA_interface_alpaka_TrackForVertexDeviceCollection_h

#include "DataFormats/VertexSoA/interface/TrackForVertexHostCollection.h"
#include "DataFormats/Portable/interface/alpaka/PortableCollection.h"
#include "DataFormats/VertexSoA/interface/TrackForVertexSoA.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"

using ::TrackForVertexHostCollection;
using TrackDeviceCollection = PortableCollection<::TrackForVertexSoA>;

#endif  // DataFormats_VertexSoA_interface_alpaka_TrackForVertexDeviceCollection_h
