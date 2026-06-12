Based on CMSSW\_16\_1\_0\_pre4

## Installation (only need to run once)

cmsrel CMSSW_16_1_0_pre4
cd CMSSW_16_1_0_pre4/src/
git cms-init
git cms-merge-topic cericeci:17_X_fromPR_plusTests
scram b -j 8

## Running the vertexing 

cmsRun testVertexing.py -m Old -i Zmumu_16X.txt -o Zmumu_RelCal_16X_New.root -d

cmsRun testVertexing.py -m InBlocks -i Zmumu_16X.txt -o Zmumu_RelCal_16X_New.root -d

## Harvesting DQM plots:

### First create file list from previous output
echo file:$PWD/Zmumu_RelCal_16X_Old_DQM.root >> Old_DQM.txt

### Then harvest and rename output
cmsRun harvester.py inputFileList=Old_DQM.txt
mv DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root Old.root

### Same for new algo
echo file:$PWD/Zmumu_RelCal_16X_New_DQM.root >> New_DQM.txt
cmsRun harvester.py inputFileList=New_DQM.txt
mv DQM_V0001_R000000001__Global__CMSSW_X_Y_Z__RECO.root New.root

## Making DQM plots from harvested files:
makeTrackValidationPlots.py --extended Old.root New.root
