


import cv2
import threading
import time



class GrayScaleThread(threading.Thread):
    def _init_(self,lock,semaphore1, semaphore2, semaphore3 ,semaphore4 , q1=[],q2=[]):
        threading.Thread._init_(self)
        self.lock = lock
        self.semaphore1 = semaphore1
        self.semaphore2 = semaphore2
        self.semaphore3 = semaphore3
        self.semaphore4 = semaphore4
        self.q1 = q1
        self.q2 = q2
    def run(self):

        outputDir = 'frames'



        count = 0
        inputFrame = ""

        while inputFrame is not None:
            self.semaphore1.acquire()
            self.lock.acquire()
            count = self.q1.pop(0)
            self.lock.release()
            self.semaphore2.release()

            if count == -1:
                self.q2.append(-1)
                self.semaphore3.release()
                break

            inFileName = "{}/frame_{:04d}.jpg".format(outputDir,count)

            inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)


            print("Converting frame {}".format(count))

            grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)

            outFileName = "{}/grayscale_{:04d}.jpg".format(outputDir, count)

            cv2.imwrite(outFileName, grayscaleFrame)
            self.semaphore4.acquire()
            self.lock.acquire()
            self.q2.append(count)
            self.lock.release()
            self.semaphore3.release()

            #pass
