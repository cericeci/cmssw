#!/usr/bin/env python
import os, re
import math, time
import sys

print("") 
print('START')
print("")
########   YOU ONLY NEED TO FILL THE AREA BELOW   #########
########   customization  area #########
queue           = "workday" # Queues: https://twiki.cern.ch/twiki/bin/view/ABPComputing/LxbatchHTCondor 
tag             = "test"    # To identify the set of jobs
NumberOfJobs    = -1        # How many to run
interval        = 1         # number files to be processed in a single job, take care to split your file so that you run on all files. The last job might be with smaller number of files (the ones that remain)
doSubmit = False             # Activate job submission (deactivate if you just want to test) 
cmsswPath = "/nfshome0/cericeci/PV_Alpaka/CMSSW_14_0_0/src/" # Path to your cms-sw installation
afsHome = "/afs/cern.ch/user/c/cericeci/private/" # Afs path where you want to store your valid proxy
fileList = open(sys.argv[1],'r') # Some txt, one line per file
output   = sys.argv[2] # Where do we put the output (full path)
files = []

for line in fileList.readlines():
  if "root" in line:
    files.append(line)

########   customization end   #########
tag = tag
path = os.getcwd()
print("")
print('Do not worry about folder creation:')
os.system("rm -rf tmp%s"%tag)
os.system("rm -rf exec%s"%tag)
os.system("rm -rf batchlogs%s"%tag)
os.system("mkdir tmp%s"%tag)
os.system("mkdir exec%s"%tag)
print("")

if NumberOfJobs == -1: 
  NumberOfJobs = (len(files)+ interval)/interval
##### loop for creating and sending jobs #####
for x in range(1, int(NumberOfJobs)+1):
    ##### creates directory and file list for job #######
    jobFiles = files[max(0,(x-1)*interval):min(x*interval, len(files))]
    with open('exec%s/job_'%tag+str(x)+'.sh', 'w') as fout:
        fout.write("#!/bin/sh\n")
        fout.write("echo\n")
        fout.write("echo\n")
        fout.write("echo 'START---------------'\n")
        fout.write("echo 'WORKDIR ' ${PWD}\n")
        fout.write("export HOME=$PWD\n")
        fout.write("export X509_USER_PROXY=$1\n")
        fout.write("source /afs/cern.ch/cms/cmsset_default.sh\n")
        fout.write("cd %s \n"%cmsswPath)
        fout.write("cmsenv\n")
        fout.write("cd -\n")
        fout.write("cmsRucmsRun %s/testVertexing.py -d -a old -o old_%s -i '%s'\n"%(os.getcwd(), output + "/output_%i.root"%(x), ",".join(jobFiles)))
        fout.write("cmsRucmsRun %s/testVertexing.py -d -a new -o new_%s -i '%s'\n"%(os.getcwd(), output + "/output_%i.root"%(x), ",".join(jobFiles)))        
        fout.write("echo 'STOP---------------'\n")
        fout.write("echo\n")
        fout.write("echo\n")
    os.system("chmod 755 exec%s/job_"%tag+str(x)+".sh")
    
###### create submit.sub file ####
   
print("Will now set up your proxy for remote running")
os.system("voms-proxy-init -voms cms --out %s/x509up"%afsHome)


os.mkdir("batchlogs%s"%tag)
with open('submit.sub', 'w') as fout:
    fout.write("executable              = $(filename)\n")
    fout.write("Proxy_path              = %s/x509up\n"%afsHome)
    fout.write("arguments               = $(Proxy_path) $(ClusterId)$(ProcId)\n")
    fout.write("output                  = batchlogs%s/$(ClusterId).$(ProcId).out\n"%tag)
    fout.write("error                   = batchlogs%s/$(ClusterId).$(ProcId).err\n"%tag)
    fout.write("log                     = batchlogs%s/$(ClusterId).log\n"%tag)
    fout.write('+JobFlavour = "%s"\n' %(queue))
    fout.write("\n")
    fout.write("queue filename matching (exec%s/job_*sh)\n"%tag)
    
###### sends bjobs ######
os.system("echo submit.sub")
if doSubmit: os.system("condor_submit -spool submit.sub")
  
print()
print("your jobs:")
os.system("condor_q")
print()
print('END')
print()
