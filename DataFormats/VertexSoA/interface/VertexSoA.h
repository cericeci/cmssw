#ifndef DataFormats_VertexSoA_interface_VertexSoA_h
#define DataFormats_VertexSoA_interface_VertexSoA_h

#include <Eigen/Core>
#include <Eigen/Dense>

#include "DataFormats/SoATemplate/interface/SoACommon.h"
#include "DataFormats/SoATemplate/interface/SoALayout.h"
#include "DataFormats/SoATemplate/interface/SoAView.h"

unsigned int const nTracksPerVertex = 1024;  // Maximum number of tracks associated to a final vertex, i.e. after fitting it

using VertexToTrack = Eigen::Vector<float, nTracksPerVertex>;
using VertexToTrackInt = Eigen::Vector<int, nTracksPerVertex>;

// SoA layout with x, y, z, id fields
GENERATE_SOA_LAYOUT(VertexSoALayout,
                      // columns: one value per element
                      SOA_COLUMN(float, x),
                      SOA_COLUMN(float, y),
                      SOA_COLUMN(float, z),
                      SOA_COLUMN(float, t),

                      SOA_COLUMN(float, errx),
                      SOA_COLUMN(float, erry),
                      SOA_COLUMN(float, errz),
                      SOA_COLUMN(float, errt),

                      SOA_COLUMN(float, chi2),
                      SOA_COLUMN(float, ndof),
                      SOA_COLUMN(int, ntracks),
                      SOA_COLUMN(float, rho),

                      SOA_COLUMN(float, aux1),
                      SOA_COLUMN(float, aux2),

                      SOA_EIGEN_COLUMN(VertexToTrackInt, track_id),
                      SOA_EIGEN_COLUMN(VertexToTrack, track_weight),

                      SOA_COLUMN(bool, isGood),
                      SOA_COLUMN(int, order),

                      SOA_COLUMN(float, sw),
                      SOA_COLUMN(float, se),
                      SOA_COLUMN(float, swz),
                      SOA_COLUMN(float, swE),
                      SOA_COLUMN(float, exp),
                      SOA_COLUMN(float, exparg),

                      // Use entries for blocks
                      SOA_COLUMN(int32_t, nV))

using VertexSoA = VertexSoALayout<>;

#endif  // DataFormats_VertexSoA_interface_VertexSoA_h
