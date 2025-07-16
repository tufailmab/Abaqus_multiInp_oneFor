# Developer: Engr. Tufail Mabood
# WhatsApp: +923440907874
# Note: Incase if you are using this script and having problems, ask me on WhatsApp and i will guide youa accordingly.

import os
import re
from abaqus import *
from abaqusConstants import *

# Get current working directory
current_dir = os.getcwd()

# Find all .inp files
inp_files = sorted([f for f in os.listdir(current_dir) if f.endswith('.inp')])
for_files = sorted([f for f in os.listdir(current_dir) if f.endswith('.for')])

# Validation
if not inp_files:
    raise Exception("No .inp files found in current directory.")
if not for_files:
    raise Exception("No .for files found in current directory.")
if len(for_files) > 1:
    raise Exception("More than one .for file found. This script expects only ONE.")

# Use the single .for file
for_file = for_files[0]
for_path = os.path.join(current_dir, for_file)
base_for = os.path.splitext(for_file)[0]

# Loop through all .inp files
for inp_file in inp_files:
    inp_path = os.path.join(current_dir, inp_file)
    base_inp = os.path.splitext(inp_file)[0]

    # Make a valid job name
    job_name = base_inp + '_' + base_for
    safe_name = re.sub('[^A-Za-z0-9_]', '_', job_name)
    if not safe_name[0].isalpha():
        safe_name = 'job_' + safe_name

    print "Creating job:", safe_name

    # Create the job
    mdb.JobFromInputFile(name=safe_name,
        inputFileName=inp_path,
        type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None,
        memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE,
        userSubroutine=for_path,
        scratch='', resultsFormat=ODB,
        parallelizationMethodExplicit=DOMAIN, numDomains=1,
        activateLoadBalancing=False, multiprocessingMode=DEFAULT,
        numCpus=1)

    # Submit & wait
    print "Submitting job:", safe_name
    mdb.jobs[safe_name].submit(consistencyChecking=OFF)
    print "Waiting for job to finish:", safe_name
    mdb.jobs[safe_name].waitForCompletion()
    print "Finished job:", safe_name
