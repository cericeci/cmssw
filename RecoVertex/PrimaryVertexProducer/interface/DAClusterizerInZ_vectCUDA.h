#ifndef RecoVertex_PrimaryVertexProducer_DAClusterizerInZ_vectCUDA_h
#define RecoVertex_PrimaryVertexProducer_DAClusterizerInZ_vectCUDA_h

/**\class DAClusterizerInZ_vectCUDA

 Description: separates event tracks into clusters along the beam line

	Version which auto-vectorizes with gcc 4.6 or newer

 */

#include "RecoVertex/PrimaryVertexProducer/interface/TrackClusterizerInZ.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "FWCore/ParameterSet/interface/ConfigurationDescriptions.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include <vector>
#include "DataFormats/Math/interface/Error.h"
#include "RecoVertex/VertexTools/interface/VertexDistanceXY.h"
#include "RecoVertex/VertexPrimitives/interface/TransientVertex.h"
#include "RecoVertex/PrimaryVertexProducer/interface/clusterizerCUDA.h"
#include "HeterogeneousCore/CUDAUtilities/interface/device_unique_ptr.h"
#include "HeterogeneousCore/CUDAUtilities/interface/host_noncached_unique_ptr.h"



class DAClusterizerInZ_vectCUDA final : public TrackClusterizerInZ {
public:
  static void fillPSetDescription(edm::ParameterSetDescription &desc);

  DAClusterizerInZ_vectCUDA(const edm::ParameterSet &conf);

  std::vector<std::vector<reco::TransientTrack> > clusterize(
      const std::vector<reco::TransientTrack> &tracks) const override;

  std::vector<TransientVertex> vertices(const std::vector<reco::TransientTrack> &tracks) const;

  track_t fill(const std::vector<reco::TransientTrack> &tracks) const;

  void set_vtx_range(double beta, track_t &gtracks, vertex_t &gvertices) const;

  void clear_vtx_range(track_t &gtracks, vertex_t &gvertices) const;

  unsigned int thermalize(
      double beta, track_t &gtracks, vertex_t &gvertices, const double delta_max, const double rho0 = 0.) const;

  double update(
      double beta, track_t &gtracks, vertex_t &gvertices, const double rho0 = 0, const bool updateTc = false) const;

  void dump(
      const double beta, const vertex_t &y, const track_t &tks, const int verbosity = 0, const double rho0 = 0.) const;
  bool merge(vertex_t &y, track_t &tks, double &beta) const;
  bool purge(vertex_t &, track_t &, double &, const double) const;
  bool split(const double beta, track_t &t, vertex_t &y, double threshold = 1.) const;

  double beta0(const double betamax, track_t const &tks, vertex_t const &y) const;
  void verify(const vertex_t &v, const track_t &tks, unsigned int nv = 999999, unsigned int nt = 999999) const;

private:
  double zdumpcenter_;
  double zdumpwidth_;

  double vertexSize_;
  unsigned int maxIterations_;
  double coolingFactor_;
  double betamax_;
  double betastop_;
  double dzCutOff_;
  double d0CutOff_;

  double mintrkweight_;
  double uniquetrkweight_;
  double uniquetrkminp_;
  double zmerge_;
  double betapurge_;

  unsigned int convergence_mode_;
  double delta_highT_;
  double delta_lowT_;

  double sel_zrange_;
  const double zrange_min_ = 0.1;  // smallest z-range to be included in a tracks cluster list
};

//#ifndef DAClusterizerInZ_vectCUDA_h
#endif
