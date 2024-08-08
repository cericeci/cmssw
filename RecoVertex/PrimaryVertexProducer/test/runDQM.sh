cmsenv
cmsRun testVertexing.py -a old -d -o old.root
cmsRun testVertexing.py -a new -d -o new.root

harvestTrackValidationPlots.py old_DQM.root -o cpu.root
harvestTrackValidationPlots.py new_DQM.root -o gpu.root

makeTrackValidationPlots.py gpu.root cpu.root --png --extended

