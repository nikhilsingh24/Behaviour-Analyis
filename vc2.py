import cv2
 
def save_webcam(outPath,fps,mirror=False):
    cap = cv2.VideoCapture(0)
    currentFrame = 1
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(outPath, fourcc, fps, (int(width), int(height)))
 
    while (cap.isOpened()):

        ret, frame = cap.read()
 
        if ret == True:
            if mirror == True:
                frame = cv2.flip(frame, 1)
            out.write(frame)
            cv2.imshow('frame', frame)
        else:
            break
 
        if cv2.waitKey(1) & 0xFF == ord('q'):  # if 'q' is pressed then quit
            break
	print("if q is pressed then quit")

        currentFrame += 1
    cap.release()
    out.release()
   
 
def main():
    save_webcam('output.avi', 30.0,mirror=True)
def FrameCapture(path):   
   	 vidObj = cv2.VideoCapture(path) 
    	 count = 0
         success = 1
  
    	 while success: 
        	success, image = vidObj.read() 
        	cv2.imwrite("frame%d.jpg" % count, image) 
        	count += 1
 
#if __name__ == '__main__': 
  
    	#FrameCapture("/home/nikhil/Desktop/output.avi") 

 
if __name__ == '__main__':
	main()
	FrameCapture("/home/nikhil/Desktop/output.avi")	
	cv2.destroyAllWindows()

	
