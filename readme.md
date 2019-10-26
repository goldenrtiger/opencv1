# https://docs.opencv.org/3.4.3/
#examples:
* LKtest.py 稀疏光
* Lktest1.py 稠密光
* Shi-TomasiTest.py
* FASTTest.py
* GussianTest.py 运动模糊
* GussianTest1.py 图像与二维高斯分布的概率密度函数做卷积，模糊图像细节
* SIFT1Test.py BFmatcher 
> cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,flags=2) cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
* SIFT2Test.py FlannBasedMatcher
> cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,flags=2) cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
> 修改if m.distance < 0.7*n.distance:为 if m.distance < 1*n.distance