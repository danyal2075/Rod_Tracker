import time
import io


class Camera(object):
    def __init__(self):
        #...
        print("Starting pi camera")
        
        
    def get_frame(self):
        my_stream = io.BytesIO()
        with pi_camera.Camera() as camera:
            camera.resolution = (640, 480)
            camera.start_preview()
            time.sleep(1)

            for _ in camera.capture_continuous(my_stream, 'jpeg',
                                               use_video_port=True):
                my_stream.seek(0)
                self.image = my_stream.read()
                my_stream.seek(0)
                my_stream.truncate()

                return self.image
        print("Capturing frame from pi camera")

