try:
    from .camera import Camera
except ImportError:
    from camera import Camera    


#from camera import Camera # For running main

#from pi_camera import Camera # For Raspberry Pi
import numpy as np
import cv2

class OpenCVController(object):

    def __init__(self):
        print('OpenCV controller initiated')
        self.current_color = [False,False,False]
        self.camera = Camera()

    def process_frame(self):
        frame = self.camera.get_frame()
        jpg_as_np = np.fromstring(frame, np.uint8)
        img = cv2.imdecode(jpg_as_np, cv2.COLOR_RGB2BGR)
        
        # self.colour_detection(imageFrame)
        self.test(img)
        img = cv2.imencode('.jpg', img)[1].tobytes()

        return img


    def test(self, img):
        # img = np.frombuffer(frame, np.uint8)
        # img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)

        
        #conversion of RBG to HSV
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        #Masking for red color
        redlower1 = np.array([0, 87, 111], np.uint8)
        redupper1 = np.array([20, 255, 255], np.uint8)
        redmask1 = cv2.inRange(hsv, redlower1, redupper1)
        #res_R = cv2.bitwise_and(img, img, mask = redmask) 
        redlower2 = np.array([170, 120, 70], np.uint8)
        redupper2 = np.array([179, 255, 255], np.uint8)
        redmask2 = cv2.inRange(hsv, redlower2, redupper2)

        redmask = redmask1 + redmask2

        #Masking for Green 
        greenlower = np.array([25, 40, 100], np.uint8)
        greenupper = np.array([70, 255, 255], np.uint8)
        greenmask = cv2.inRange(hsv, greenlower, greenupper)
        #res_G = cv2.bitwise_and(img, img, mask = greenmask)
        

        #Masking for Yellow
        yellowlower = np.array([22, 130, 105], np.uint8)
        yellowupper = np.array([48,255,200], np.uint8)
        yellowmask = cv2.inRange(hsv, yellowlower, yellowupper)
        #res_Y=cv2.bitwise_and(img, img, mask = yellowmask)

        #Masking for purple
        purplelower = np.array([135,20,50], np.uint8)
        purpleupper = np.array([170,120,200], np.uint8)
        purplemask = cv2.inRange(hsv, purplelower, purpleupper)
        #res_P =cv2.bitwise_and(img, img, mask = purplemask)

        #kernal

        kernal = np.ones((5, 5), "uint8")
        #sred Color
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
            
            if(area > 5000):
                
                rx, ry, rw, rh = cv2.boundingRect(contour)
                img = cv2.rectangle(img,(rx,ry),(rx + rw, ry + rh),(0, 0, 255), 2)
                cv2.putText(img, "Red Color",(rx, ry), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,0,255))
        
        
        #GREEN COLOR
        contours, hierarchy = cv2.findContours(greenmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic,contour in enumerate(contours):
            area=cv2.contourArea(contour)
            if(area > 25000):
                gx, gy, gw, gh = cv2.boundingRect(contour)
                cv2.rectangle(img,(gx,gy),(gx + gw, gy + gh),(0, 255, 0), 2)
                cv2.putText(img, "Green Color",(gx, gy), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0,255,0))
         

        #yellow color
        contours, hierarchy = cv2.findContours(yellowmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic,contour in enumerate(contours):
            area=cv2.contourArea(contour)
            if(area > 25000):
                yx, yy, yw, yh = cv2.boundingRect(contour)
                img = cv2.rectangle(img,(yx,yy),(yx + yw, yy + yh),(0, 255, 217), 2)
                cv2.putText(img, "Yellow Color",(yx, yy), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 217))
        
        #purple color
        contours, hierarchy = cv2.findContours(purplemask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic,contour in enumerate(contours):
            area=cv2.contourArea(contour)
            if(area > 5000):
                px, py, pw, ph = cv2.boundingRect(contour)
                img = cv2.rectangle(img,(px,py),(px + pw, py + ph),(128, 0, 128), 2)
                cv2.putText(img, "Purple Color",(px, py), cv2.FONT_HERSHEY_SIMPLEX,1.0, (128,0,128))
                

        if(rx>=gx-4) and (ry>gy) and ((rx +rw) <= (gx + gw) and (ry+rh) <= (gy+gh)):
            self.current_color= [True, False, False]
        elif(rx>=px) and (ry>py) and ((rx +rw) <= (px + pw) and (ry+rh) <= (py+ph)):
            self.current_color= [False, True, False]
        elif(rx>=yx) and (ry>yy) and ((rx +rw) <= (yx + yw) and (ry+rh) <= (yy+yh)):
            self.current_color= [False, False, True]
        elif(rx>px and (rx+rw)>yx):
            self.current_color= [False, True, True]
        elif(rx<(gx+gw) and (rx+rw)>px):
            self.current_color= [True, True, False]

        #print('Monitoring')
        #return img

    def get_current_color(self):
        return self.current_color
