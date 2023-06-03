# import os
#
# from gtts import gTTS
# from playsound import playsound
#
# gTTS('Hello Surndhar').save('surenshar.mp3')
# playsound('service/surenshar.mp3')
# os.remove('service/surenshar.mp3')

"""notification"""
# import time
# from plyer import notification
#
#
# def notify():
#     while True:
#         notification.notify(
#             title="ALERT!!!",
#             message="Take a break! It has been an hour!",
#             timeout=10
#         )
#         time.sleep(2)
# notify()

# from gingerit.gingerit import GingerIt
# text = input("Enter a sentence >>: ")
# corrected_text = GingerIt().parse(text)
# print(corrected_text)

# from sketchpy import library,canvas
# from sklearn.preprocessing import scale
# pen = canvas.sketch_from_image('D:\software\python-server\service\datas.jpg')
# pen.draw()
# obj = library.rdj()
# obj.pen.speed(2)
# obj.draw()

# pen = canvas.sketch_from_svg('./service/surendhar.svg')
# pen.draw()

import power
import psutil
p = power.PowerManagement().get_providing_power_source_type()
d = psutil.sensors_battery()
while True:
    print('pp')
    if d.percent == 20:
        print('in')
        d.power_plugged = True