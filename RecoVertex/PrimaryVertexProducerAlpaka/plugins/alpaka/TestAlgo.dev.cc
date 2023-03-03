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
                                  int32_t trackssize,
                                  portablevertex::VertexDeviceCollection::View vertexview) const {
      // global index of the thread within the grid
      const int32_t thread = alpaka::getIdx<alpaka::Grid, alpaka::Threads>(acc)[0u];
      // make a strided loop over the kernel grid, covering up to "size" elements
      for (int32_t i : elements_with_stride(acc, trackssize)) {
        trackview[i].z() = 0.;
      }
    }
  };

  void TestAlgo::fill(Queue& queue, portablevertex::VertexDeviceCollection& vertices, portablevertex::TrackDeviceCollection& tracks) const {
    // use 512 items per group (this value is arbitrary, but it's a reasonable starting point)
    uint32_t items = 512;

    // use as many groups as needed to cover the whole problem
    uint32_t trackgroups = divide_up_by(tracks->metadata().size(), items);

    // map items to
    //   - threads with a single element per thread on a GPU backend
    //   - elements within a single thread on a CPU backend
    auto workDiv = make_workdiv<Acc1D>(trackgroups, items);

    alpaka::exec<Acc1D>(queue, workDiv, TestAlgoKernel{}, tracks.view(), tracks->metadata().size(), vertices);
  }

}  // namespace ALPAKA_ACCELERATOR_NAMESPACE
