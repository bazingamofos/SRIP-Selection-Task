#!/usr/bin/env python
# coding: utf-8

# In[13]:


get_ipython().system('pip install opencv-contrib-python --user')


# In[24]:


import cv2
import numpy as np

# Read the video
video_path = '1705951007967.mp4'
cap = cv2.VideoCapture(video_path)

# Background subtraction method (e.g., MOG2)
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply background subtraction
    fg_mask = bg_subtractor.apply(gray)

    # Find connected components
    _, labels, stats, _ = cv2.connectedComponentsWithStats(fg_mask)

    # Iterate through each connected component
    for i in range(1, stats.shape[0]):
        x, y, w, h, area = stats[i]

        # Calculate frequency (assuming 30 frames per second)
        frequency = area / (w * h * 30)

        # Filter components with frequency in the 0-1 Hz range
        if frequency >= 0 and frequency <= 1:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Components with 0-1 Hz frequency', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




