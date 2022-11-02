import csv

#Read the Trace File
Filename = "output/trace.csv"

#Create ditionaries to store Frame Info along with Min, Max, Avg Frame Sizes
Frames, Min, Max, Avg = dict(), dict(), dict(), dict()

with open(Filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        #Check if we have data in the row
        if(len(row) > 0):
            size, frameType = row[0], row[1]
            if frameType in Frames.keys():
                #Update Min
                if Min[frameType] > int(size): Min[frameType] = int(size)
                #Update Max
                if Max[frameType] < int(size): Max[frameType] = int(size)
                #Update number of frames and frame size for a given frametype
                Frames[frameType] = [Frames[frameType][0] + 1, Frames[frameType][1] + int(size)]
            else:
                #Initialize Min and Max
                Min[frameType] = Max[frameType] = int(size)
                #Initalize Frames
                Frames[frameType] = [1, int(size)]

    #Find Avg Frame Size for each Frametype
    for key in Frames.keys():
        Avg[key] = round(Frames[key][1]/Frames[key][0], 2)

#Print all Information About Each FrameType
for key in Frames.keys():
    print(key+"-frames:")
    print("Total Size:", Frames[key][1], "bytes")
    print("Count:", Frames[key][0], "frames")
    print("Minimum "+key+"-frame Size:", Min[key], "bytes")
    print("Maximum "+key+"-frame Size:", Max[key], "bytes")
    print("Average "+key+"-frame Size:", Avg[key], "bytes\n")



