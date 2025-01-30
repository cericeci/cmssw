#ifndef RecoVertex_PortablePrimaryVertexProducer_interface_ClusterParamsSoA_h
#define RecoVertex_PortablePrimaryVertexProducer_interface_ClusterParamsSoA_h

#include <Eigen/Core>
#include <Eigen/Dense>

#include "DataFormats/SoATemplate/interface/SoACommon.h"
#include "DataFormats/SoATemplate/interface/SoALayout.h"
#include "DataFormats/SoATemplate/interface/SoAView.h"

#include <Eigen/Core>
#include <Eigen/Dense>

GENERATE_SOA_LAYOUT(ClusterParams,
                      SOA_SCALAR(float, d0CutOff),
                      SOA_SCALAR(float, TMin),
                      SOA_SCALAR(float, delta_lowT),
                      SOA_SCALAR(float, zmerge),
                      SOA_SCALAR(float, dzCutOff),
                      SOA_SCALAR(float, Tpurge),
                      SOA_SCALAR(int, convergence_mode),
                      SOA_SCALAR(float, delta_highT),
                      SOA_SCALAR(float, Tstop),
                      SOA_SCALAR(float, coolingFactor),
                      SOA_SCALAR(float, vertexSize),
                      SOA_SCALAR(float, uniquetrkweight),
                      SOA_SCALAR(float, uniquetrkminp),
                      SOA_SCALAR(float, zrange))

using ClusterParamsSoA = ClusterParams<>;

#endif
