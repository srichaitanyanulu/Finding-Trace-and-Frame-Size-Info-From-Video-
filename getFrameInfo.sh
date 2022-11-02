#!/bin/bash

#notify
echo "Running the bash script. Please wait..."

#Write the video's trace to "output/trace.csv"
ffprobe -i $1 -v error -select_streams V:0 -show_entries "frame=pict_type,pkt_size" -of csv=p=0 > "output/trace.csv"

#notify
echo "Trace written to 'output/trace.csv'"

echo "Running the python script now..."

#Run the python code to print and write Frame Information to "output/frameInfo.txt"
python3 "src/main.py" > "output/frameInfo.txt"

echo "Frame Information written to 'output/frameInfo.txt'"

#END