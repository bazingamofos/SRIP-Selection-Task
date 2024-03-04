# SRIP-Selection-Task (Project 2: Develop a respiration sensing system in SmartWatch)

**The task required to:**
* Use OpenCV with the the [thermal video](https://drive.google.com/file/d/1PWS2MoFphHwTwblN82QZZbYqEmycN0Jj/view) to find components that have a frequency of 0-1 Hz. 
* In the above question, components refer to the 4 or 8 connected components. 

**Code Explanation:**
> bg_subtractor = cv2.createBackgroundSubtractorMOG2()
* Background subtraction is a technique used to separate foreground objects (moving objects) from the background in a video sequence. MOG2 is a specific algorithm for background subtraction.

> while True:
> 
> &nbsp;&nbsp;&nbsp;&nbsp;ret, frame = cap.read()
> 
> &nbsp;&nbsp;&nbsp;&nbsp;if not ret:
> 
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break
* Within the loop, frames are read from the video file using the cap.read() function. The function returns two values: ret, which indicates whether a frame was successfully read, and frame, which contains the image data of the frame. 

> gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
* Each frame is converted to a grayscale. Grayscale images have only one channel, representing the intensity of light, which simplifies further processing.

> fg_mask = bg_subtractor.apply(gray)
* The background subtraction method (bg_subtractor) created earlier is applied to the grayscale frame (gray). This produces a binary mask (fg_mask) where foreground objects are highlighted against the background.

> _, labels, stats, _ = cv2.connectedComponentsWithStats(fg_mask)
* By default, the `cv2.connectedComponentsWithStats` function uses 8 connectivity to find connected components in the foreground mask generated by the background subtraction method. This function returns the number of connected components, the labeled mask, statistics about each component (such as its position and size), and an optional output mask.

> for i in range(1, stats.shape[0]):
* A loop is initiated to iterate through each connected component found in the previous step. The loop starts from index 1 because index 0 represents the background component.
python

> x, y, w, h, area = stats[i]
* For each connected component, its statistics (position, size, and area) are extracted from the stats array.

> frequency = area / (w * h * 24.61)
* The frequency of the connected component's appearance in the video is calculated. This is done by dividing the area of the component by the product of its width (w), height (h), and the frame rate.

> if frequency >= 0 and frequency <= 1:
> 
> &nbsp;&nbsp;&nbsp;&nbsp;cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
* For each connected component passing the frequency filter, a rectangle is drawn around it on the original color frame.
