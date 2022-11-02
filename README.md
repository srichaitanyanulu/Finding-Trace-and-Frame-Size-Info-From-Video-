### **Description:**
This project allows you to write the trace of a video, and display the frame size information on I-, P-, and B-frames, along with the minimum, maximum, and average frame sizes in the trace.

### **Prerequisites:**
I executed my files on Linux, but you can test it on any operating system if you have **FFmpeg, Python3,** and a way to run **Bash scripts**.

### **Steps to run:**
* First, place your video file under the input folder and open a terminal.

* Next, give the execute permission to the “getFrameInfo.sh” bash script, by running the following command:
**chmod +x getFrameInfo.sh”**

* Now just run the following command:
**./getFrameInfo.sh <input/video_filename>**

* You would see some information getting displayed regarding the progress.

* After the trace and frame information is written to the output folder, just open them and check the information.

### **Video Used:**
* I downloaded the video at: ["https://archive.org/details/charlie_chaplin_film_fest"](https://archive.org/details/charlie_chaplin_film_fest) in **MPEG** format.
* The Output Trace file and File Information for this video can be found under the “output” folder with the names **“sample_trace.csv”** and **“sample_fileInfo.txt”** respectively.
