#ifndef DataFormats_PortableVertex_interface_TestSoA_h
#define DataFormats_PortableVertex_interface_TestSoA_h

#include <Eigen/Core>
#include <Eigen/Dense>

#include "DataFormats/SoATemplate/interface/SoACommon.h"
#include "DataFormats/SoATemplate/interface/SoALayout.h"
#include "DataFormats/SoATemplate/interface/SoAView.h"

namespace portablevertex {

  using vertToTrack = Eigen::Matrix<double, 512, 1>;
  GENERATE_SOA_LAYOUT(TrackSoALayout,
                      // Inputs for the clusterizer
                      SOA_COLUMN(double, significance),
                      SOA_COLUMN(double, dz2),
                      SOA_COLUMN(double, z),
                      SOA_COLUMN(double, weight),
		      SOA_COLUMN(double, sum_Z),
		      SOA_COLUMN(unsigned int, kmin),
		      SOA_COLUMN(unsigned int, kmax),
		      SOA_COLUMN(bool, isGood),
		      SOA_COLUMN(int, order), 
		      SOA_COLUMN(unsigned int, tt_index),
                      // General properties
                      SOA_SCALAR(double, min_z),
		      SOA_SCALAR(double, max_z),
		      SOA_SCALAR(unsigned int, nTrueTracks),
		      // Inputs for the fitter
		      SOA_COLUMN(double, dx),
		      SOA_COLUMN(double, dy),
		      SOA_COLUMN(double, dz),
		      SOA_COLUMN(double, px),
		      SOA_COLUMN(double, py),
		      SOA_COLUMN(double, pz),
		      SOA_COLUMN(double, dxError),
		      SOA_COLUMN(double, dyError),
		      SOA_COLUMN(double, dzError),
		      // Auxiliars
		      SOA_COLUMN(double, aux1),
		      SOA_COLUMN(double, aux2),
                      // Eigen columns, internal common vertex-track association matrices
                      SOA_EIGEN_COLUMN(vertToTrack, vert_sw),
		      SOA_EIGEN_COLUMN(vertToTrack, vert_se),
		      SOA_EIGEN_COLUMN(vertToTrack, vert_swz),
		      SOA_EIGEN_COLUMN(vertToTrack, vert_swE),
		      SOA_EIGEN_COLUMN(vertToTrack, vert_exp),
		      SOA_EIGEN_COLUMN(vertToTrack, vert_exparg))
			     
  using TrackSoA = TrackSoALayout<>;
  using trackToVertInt    = Eigen::Matrix<unsigned int, 512, 1>;
  using trackToVertDouble = Eigen::Matrix<double, 512, 1>;

  GENERATE_SOA_LAYOUT(VertexSoALayout,
		      SOA_SCALAR(unsigned int, nTrueVertex),
		      SOA_COLUMN(bool, isGood),
		      // Clusterizer properties
		      SOA_COLUMN(double, sw),
		      SOA_COLUMN(double, se),
		      SOA_COLUMN(double, swz),
		      SOA_COLUMN(double, swE),
		      SOA_COLUMN(double, exp),
		      SOA_COLUMN(double, exparg),
		      SOA_COLUMN(double, rho),
		      SOA_COLUMN(double, aux1),
		      SOA_COLUMN(double, aux2),
		      SOA_COLUMN(int, order),
		      // Fitter properties
		      SOA_COLUMN(double, z),
		      SOA_COLUMN(double, y),
		      SOA_COLUMN(double, x),
		      SOA_COLUMN(double, t),
		      SOA_COLUMN(double, chi2),
		      SOA_COLUMN(unsigned int, ndof),
		      SOA_COLUMN(double, errx),
		      SOA_COLUMN(double, erry),
		      SOA_COLUMN(double, errz),
		      SOA_COLUMN(double, errt),
		      SOA_COLUMN(unsigned int, ntracks),
		      SOA_EIGEN_COLUMN(trackToVertInt, trackid),
		      SOA_EIGEN_COLUMN(trackToVertDouble, trackweight))
  using VertexSoA = VertexSoALayout<>;

}  // namespace portablevertex

#endif  // DataFormats_PortableVertex_interface_TestSoA_h
