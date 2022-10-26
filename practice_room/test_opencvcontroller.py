try:
    from .camera import Camera # For running app
except ImportError:
    
    from camera import Camera # For local test
# from pi_camera import Camera # For Raspberry Pi
    import numpy as np
    import cv2

class OpenCVController(object):

    def __init__(self):
        print('OpenCV controller initiated')
        self.current_color = [False,False,False]
        self.camera = Camera()

    def process_frame(self):
        frame = self.camera.get_frame()
        jpg_as_np = np.frombuffer(frame, np.uint8)
        img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)

        
        #conversion of RBG to HSV
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        #Masking for red color
        redlower = np.array([136, 87, 111], np.uint8)
        redupper = np.array([180, 255, 255], np.uint8)
        redmask = cv2.inRange(hsv, redlower, redupper)
        # res_R = cv2.bitwise_and(img, img, mask = redmask) 
        

        #Masking for Green 
        greenlower=np.array([25, 52, 72], np.uint8)
        greenupper=np.array([102,255,255], np.uint8)
        greenmask=cv2.inRange(hsv, greenlower, greenupper)
        #res_G = cv2.bitwise_and(img, img, mask = greenmask)
        

        #Masking for Yellow
        yellowlower=np.array([2,2,2], np.uint8)
        yellowupper=np.array([2,2,2], np.uint8)
        yellowmask=cv2.inRange(hsv, yellowlower, yellowupper)
        #res_Y=cv2.bitwise_and(img, img, mask = yellowmask)

        #Masking for purple
        purplelower=np.array([2,2,2], np.uint8)
        purpleupper=np.array([2,2,2], np.uint8)
        purplemask =cv2.inRange(hsv, purplelower, purpleupper)
        #res_P =cv2.bitwise_and(img, img, mask = purplemask)

        #kernal

        kernal = np.ones((5, 5), "uint8")
        #red Color
        redmask = cv2.dilate(redmask, kernal) 
        res_R = cv2.bitwise_and(img, img, mask = redmask)

        #Green Color
        greenmask = cv2.dilate(greenmask, kernal) 
        res_G = cv2.bitwise_and(img, img, mask = greenmask)
        
        #yellow color
        yellowmask = cv2.dilate(yellowmask, kernal) 
        res_Y = cv2.bitwise_and(img, img, mask = yellowmask)

        #purple color
        purplemask = cv2.dilate(purplemask, kernal) 
        res_P = cv2.bitwise_and(img, img, mask = purplemask)
	    

        #RED COLOR
        
        contours, hierarchy = cv2.findContours(redmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic,contour in enumerate(contours):
            area=cv2.contourArea(contour)
            if(area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img,(x,y),(x + w, y + h),(0, 0, 255), 2)
                cv2.putText(img, "Red Color",(x, y), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,0,255))
        
        #GREEN COLOR
        contours, hierarchy = cv2.findContours(greenmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic,contour in enumerate(contours):
            area=cv2.contourArea(contour)
            if(area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img,(x,y),(x + w, y + h),(0, 255, 0), 2)
                cv2.putText(img, "Red Color",(x, y), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,255,0))

        #yellow color
        contours, hierarchy = cv2.findContours(yellowmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic,contour in enumerate(contours):
            area=cv2.contourArea(contour)
            ###checking for the maximum area of the countour 
            area_max=np.max(area)
            if(area >= area_max):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img,(x,y),(x + w, y + h),(0, 0, 255), 2)
                cv2.putText(img, "Red Color",(x, y), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,0,255))
        
        #purple color
        contours, hierarchy = cv2.findContours(purplemask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic,contour in enumerate(contours):
            area=cv2.contourArea(contour)
            area_max_2=np.max(area)
            if(area >= area_max_2):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img,(x,y),(x + w, y + h),(0, 0, 255), 2)
                cv2.putText(img, "Red Color",(x, y), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,0,255))
        frame=buffer.tobytes()
        print('Monitoring')
        return frame

    def get_current_color(self):
        return self.current_color
