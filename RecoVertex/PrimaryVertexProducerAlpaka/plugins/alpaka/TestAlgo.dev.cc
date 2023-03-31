// Check that ALPAKA_HOST_ONLY is not defined during device compilation:
#ifdef ALPAKA_HOST_ONLY
#error ALPAKA_HOST_ONLY defined in device compilation
#endif

#include <alpaka/alpaka.hpp>

#include "DataFormats/PortableVertex/interface/alpaka/VertexDeviceCollection.h"
#include "HeterogeneousCore/AlpakaInterface/interface/config.h"
#include "HeterogeneousCore/AlpakaInterface/interface/traits.h"
#include "HeterogeneousCore/AlpakaInterface/interface/workdivision.h"

#include "TestAlgo.h"

namespace ALPAKA_ACCELERATOR_NAMESPACE {

  using namespace cms::alpakatools;

  class TestAlgoKernel {
  public:
    template <typename TAcc, typename = std::enable_if_t<alpaka::isAccelerator<TAcc>>>
    ALPAKA_FN_ACC void operator()(TAcc const& acc,
                                  portablevertex::TrackDeviceCollection::View trackview,
                                  int32_t trackviewsize,
                                  portablevertex::VertexDeviceCollection::View vertexview) const {
      // Globals, they need to be provided as inputs later
      double rho0 = 0.0;
      double beta = 1./3.;  // 1/T
      cParams = {
        .Tmin   = 2.0, 
        .Tpurge = 2.0, 
        .Tstop  = 0.5,
        .vertexSize = 0.006,
        .coolingFactor = 0.6,
        .d0CutOff = 3.,
        .dzCutOff = 3.,
        .uniquetrkweight = 0.8,
        .uniquetrkminp = 0.0,
        .zmerge = 1e-2,
        .sel_zrange = 4.,
        .convergence_mode = 0,
        .delta_lowT = 1e-3,
        .delta_highT = 1e-2,
      };
      bool updateTc = true;
      int DEBUGLEVEL = -5;
      // global index of the thread within the grid
      const int32_t thread = alpaka::getIdx<alpaka::Grid, alpaka::Threads>(acc)[0u];
      double Z_init = rho0 * exp(-(*beta) * cparams.dzCutOff * cparams.dzCutOff); // 99% of the time rho0 is going to be 0, so maybe an if here can save some time. Exponentials are not cheap
      // Initiliaze stuff to 0
      for (int32_t itrackO : elements_with_stride(acc, trackviewsize)){
        unsigned int itrack = trackview[itrackO].order();
        for (unsigned int ivertexO = trackview[itrack].kmin() ; ivertexO < trackview[itrack].kmax() ; ++ivertexO){ // ivertexO loops over ordered vertex
          unsigned int ivertex = vertexview[ivertexO].order(); // ivertex translates from ordered vertex to real vertex positions
          trackview[itrack][ivertex].vert_sw() = 0.;
          trackview[itrack][ivertex].vert_se() = 0.;
          trackview[itrack][ivertex].vert_swz() = 0.;
          if (updateTc) trackview[itrack][ivertex].vert_swE() = 0.;
          trackview[itrack][ivertex].vert_exp() = 0.;
          trackview[itrack][ivertex].vert_exparg() = 0.;
        }
      }
      alpaka::syncBlockThreads(acc);
      for (int32_t itrackO : elements_with_stride(acc, trackviewsize)){
        unsigned int itrack = trackview[itrackO].order();
        double botrack_dz2 = -(beta) * trackview[itrack].dz2();
        trackview[itrack].sum_Z() = Z_init;
        for (unsigned int ivertexO = trackview[track].kmin() ; ivertexO < trackview[itrack].kmax() ; ++ivertexO){ // ivertexO loops over ordered vertex
          unsigned int ivertex = vertexview[ivertexO].order(); // ivertex translates from ordered vertex to real vertex positions
          double mult_res = trackview[itrack].z() - vertexview[ivertex].z();
          trackview[itrack][ivertex].vert_exparg() = botrack_dz2* (mult_res * mult_res);
          trackview[itrack][ivertex].vert_exp()    = alpaka::math::exp(trackview[itrack][ivertex].vert_exparg()); // exp is defined as basic alpaka::math
          trackview[itrack][ivertex].sum_Z()      += vertexview[ivertex].rho()*trackview[itrack][ivertex].vert_exp()();
        }
        if(not(std::isfinite(trackview[itrack].sum_Z()))) trackview[itrack].sum_Z() = 0; // Just in case something diverges
        if(trackview[itrack].sum_Z() > 1e-100){ // If partition > 0, then it is non-trivially assigned to a vertex and we need to compute stuff
          double sumw = trackview[itrack].weight()/trackview[itrack].sum_Z();
          for (unsigned int ivertexO = trackview[itrack].kmin() ; ivertexO < trackview[itrack].kmax() ; ++ivertexO){
            unsigned int ivertex = vertexview[ivertexO].order();
            trackview[itrack][ivertex].vert_se() = trackview[itrack][ivertex].vert_exp()* sumw;
            double w                   = vertexview[ivertex].rho() * trackview[itrack][ivertex].vert_exp() * sumw * trackview[itrack].dz2();
            trackview[itrack][ivertex].vert_sw()  = w;
            trackview[itrack][ivertex].vert_swz() = w * trackview[itrack].z();
            if (updateTc) trackview[itrack][ivertex].vert_swE() = -w * trackview[itrack][ivertex].vert_exparg()/(beta); // Only need it when changing the Tc         
          }
        }
      }
      alpaka::syncBlockThreads(acc); // Need to synchronize, as now we have to add across vertexes
      // first set to zero the data members of vertexview that will store the sum
      for (int32_t ivertexO : elements_with_stride(acc, vertexviewsize)){
        unsigned int ivertex    = vertexview[ivertexO].order(); // ivertex translates from ordered vertex to real vertex positions
        vertexview[ivertex].se()   = 0.;
        vertexview[ivertex].sw()   = 0.;
        vertexview[ivertex].swz()  = 0.;
        vertexview[ivertex].aux1() = 0.; // Aux here is delta, the position variation in this update loop
        if (updateTc) vertexview[ivertex].swE() = 0.;
      }

      alpaka::syncBlockThreads(acc); //Just to be extremely careful

      // secondly sum across columns the matrices and store results    
      for (unsigned int itrackO = firstElement; itrackO < trackview[itrack].nTrueTracks ; itrackO += gridSize){
        unsigned int itrack = trackview[itrackO].order();
        for (unsigned int ivertexO = trackview[itrack].kmin(); ivertexO < trackview[itrack].kmax(); ivertexO++){
          unsigned int ivertex    = vertexview[ivertex].order(ivertexO); // ivertex translates from ordered vertex to real vertex positions
          alpaka::atomicAdd(acc,&vertexview[ivertex].se(), trackview[itrack][ivertex].vert_se());
          alpaka::atomicAdd(acc,&vertexview[ivertex].sw(), trackview[itrack][ivertex].vert_sw());
          alpaka::atomicAdd(acc,&vertexview[ivertex].swz(), trackview[itrack][ivertex].vert_swz());
          alpaka::atomicAdd(acc,&vertexview[ivertex].swE(), trackview[itrack][ivertex].vert_swE());
          if (updateTc)           alpaka::atomicAdd(acc,&vertexview[ivertex].swE(), trackview[itrack][ivertex].vert_swE());
        }
      }
      alpaka::syncBlockThreads(acc);
    
      // finally evaluate the new position for each vertex
      for (int32_t ivertexO : elements_with_stride(acc, vertexviewsize)){
        unsigned int ivertexO    = vertexview[ivertexO].order(); // ivertex translates from ordered vertex to real vertex positions
        if (vertexview[ivertex].sw() > 0){ //The vertex position is updated
          double znew    = vertexview[ivertex].swz()/vertexview[ivertex].sw();
          vertexview[ivertex].aux1() = abs(znew-vertexview[ivertex].z());
          vertexview[ivertex].z()    = znew; 
        }
        vertexview[ivertex].rho()    = vertexview[ivertex].rho() * vertexview[ivertex].se() * (*osumtkwt);  // The relative vertex weight is updated
        if (DEBUGLEVEL == -5 && thread == 0){
        printf("UPDATE: Params for vertex %i, after update, se=%1.10f, sw=%1.10f, swz=%1.10f, swE=%1.10f, z=%1.10f, rho=%1.10f\n", ivertex, vertexview[ivertex].se(), vertexview[ivertex].sw(), vertexview[ivertex].swz(), vertexview[ivertex].swE(), vertexview[ivertex].z(), vertexview[ivertex].rho());
        }
      }
    // Some safety printing
    if (thread == 0 && DEBUGLEVEL == -5){
      printf("UPDATE: Vertex ordering: \n");
      for (unsigned int ivertex = 0; ivertex < 512; ivertex ++){
        printf("%i, ", vertexview[ivertex].order());
      }
      printf("\n");
    }
    
    alpaka::syncBlockThreads(acc); //Just to be extremely careful
  };



  void TestAlgo::fill(Queue& queue, portablevertex::VertexDeviceCollection& vertexview, portablevertex::TrackDeviceCollection& trackview) const {
    // use 512 items per group (this value is arbitrary, but it's a reasonable starting point)
    uint32_t items = 512;

    // use as many groups as needed to cover the whole problem
    uint32_t trackgroups = divide_up_by(trackview[itrack].metadata().size(), items);

    // map items to
    //   - threads with a single element per thread on a GPU backend
    //   - elements within a single thread on a CPU backend
    auto workDiv = make_workdiv<Acc1D>(trackgroups, items);

    alpaka::exec<Acc1D>(queue, workDiv, TestAlgoKernel{}, trackview.view(), trackview[itrack].metadata().size(), vertexview);
  }

}  // namespace ALPAKA_ACCELERATOR_NAMESPACE
