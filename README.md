# Self Driving Car
- At firt Create a png file where there a Stright Line Road. Background is Black and Road Color is White. (road/road1.png)
- instal pygame
```
pip install pygame
```
## Step 1> Load Picture or Track
- import pygame
```
import pygame
```
- initialize the pygame
```
pygame.init
```
- load the picture (road/road.png)

- now we should set the window size. অর্থাৎ আমাদের window এঁর সাইজ কত হবে সেটা define করা। 
```
window= pygame.display.set_mode((1900,900))
```
এখানে set_mode এঁর ভ্যালু হবে পিকচারের সাইজ অনুযায়ী। তা না হলে সম্পুর্ণ পিকচার দেখা যাবে না। 
- একন আমরা চাচ্ছি ওই window তে আমাদের পিকচার টা দেখাক এবং সেটা দেখাতেই থাকবে মানে while loop যতক্ষণ না আমরা কেটে দিচ্ছি। 
```
while True: 
```
- এখন পিকচার দেখানোর জন্য window এঁর function হলো blit যার পুরো meaning Bl= Block I= Image T= Transform
```
window.blit(track,(0,0))
```
এখানে আমরা কোন পিকচার কে Transform করতে চাচ্ছি? track পিকচার কে তাই প্রথম parameter হলো যেই পিকচারকে Transform করতে চাচ্ছি সেটার নাম  
দ্বিতীয় প্যারামেটার হলো window এঁর কোন position এ আমরা চাচ্ছি সেই position। (0,0) মানে হলো window এঁর এক্কেবারে upper left corner. 

- এখন আমাদের pygame এঁর display তে তও আমরা অনেক changes করেছি। সেটাকে update করা লাগবে। 
```
pygame.display.update()
```
** Entire Source code 
```
import pygame
pygame.init()
track=pygame.image.load('road/road1.png')
window= pygame.display.set_mode((1600,900))

while True:
    window.blit(track,(0,0))
    pygame.display.update()
```
> এই টুকতে তেমন কিছুই হচ্ছে না। শুধু মাত্র আমাদের পিকচার টা load হয়ে সেটা show করতেছে। 

- এখানে একটা বিপত্তি আসল। window টা ক্লোজ করা যাচ্ছে না। আমাদের terminal kill করা লাগতেছে। So lets fixed it. 
- প্রথমেই আমরা দেখে নেই যে window তে কি কি events হচ্ছে। 
```
while True:
    for events in pygame.event.get():
        print(events)
```
এতে করে কিছুই হবে না শুধু window তে যেই যেই event হচ্ছে সেগুলো type wise print করবে। যদি আমরা close button এ ক্লিক করই তাহলে দেখব যে events type= quite এরকম কিছু আসতেছে। তার মানে events এঁর type যদি pygame.quite হয় তাহলেই আমাদের ব্রেক করবে। কিন্তু সমস্যা হলো break শুধু inner for loop এ কাজ করবে। outer while loop এ কাজ করবে না। এইজন্য আলাদা একটা variable নিতে হবে। আমরা নিলাম visibility= True হিসেবে আর while loop টা চলবে visibility অনুযায়ী। 
```
visibility=True
while visibility:
    for events in pygame.event.get():
```
- এখন যদি if events.type == pygame.QUIT: এটা True হয় তাহলে আমাদের visibility False হয়ে যাবে। 
```
visibility=True
while visibility:
    for events in pygame.event.get():
        # print(events)
        if events.type == pygame.QUIT:
            visibility=False
    window.blit(track,(0,0))
    pygame.display.update()
```

## Step 2> Load The Car ans resize and set the position
- আগের মত আমরা একটা Car এঁর পিকচার load করি। 
- এখন দেখা গেল যে আমাদের road এঁর তুলনায় গাড়ি অনেক বড়। তাহলে আমাদের এখন গাড়ির সাইজ ছোট করতে হবে। 
- এই যে গাড়ির সাইজ ছট করা সেটা হলো scale করা। pygame এঁর transform class এঁর মধ্যে একটা function ই আছে transform করা। 

```
car_scal=pygame.transform.scale(car,(200,150))
```
এই scale function এঁর দুইটা parameter. প্রথম parameter এ বলে দিতে হয় যে কোন পিকচার টা ট্রান্সফর্ম করা লাগবে বা স্কেইল করা লাগবে। পরের parameter এ সাইজ বলে দিতে হয় যে কত width, heigth এঁর হবে। (weidth, heigth) এই দুইটা মিলে একটা parameter। আমি আমার মতো করে যেভাবে সুন্দর হয় সেই weidth, heigth বসালাম। 

- এখন কাজ হলো car টাকে proper জায়গায় বা আমাদের road/ lan/ track এ বসানো। এটার জন্য     window.blit(car_scal,(10,270)) এই blit এঁর position arguments গুলো পরিবর্তন করতে হবে। আমি আমার সুন্দর মতো tune করে সবালাম। যদি ডান দিকে আসতে হয় তাহলে first argument (10) টাকে বারাতে হবে অথবা বাম দিকে নিতে চাইলে কমাতে হবে। যদি নিচের দিকে আনতে হয় তাহলে second argument (270) কে বারাতে হবে। আর উপরে নিতে হলে কমাতে হবে। 


## Step 3> Move the car
- আমরা পুর্বের স্টেপ এ দেখলাম যে আমরা যদি প্রথম argument (10) change করি তাহলে গাড়ি বাম থেকে ডান দিকে যাবে। যেহেতু আমাদের ট্র্যাক হলও বাম থেকে ডানে তাহলে এই ভ্যালু টাই বার বার চেঞ্জ হতে হবে। 

- তাহলে এখন car এঁর position টা আলাদা একটা ভ্যারিয়েবল দিয়ে লিখে নেই। 
```
car_x=10
car_y=270
while visibility:
    for events in pygame.event.get():
        # print(events)
        if events.type == pygame.QUIT:
            visibility=False
    window.blit(track,(0,0))
    window.blit(car_scal,(car_x,car_y))
    pygame.display.update()
```
এখন আউটপুট দিলে কিছুই আসবে না আগের মতো। এবার আমরা  car_x এঁর ভ্যালু বারাতে থাকি। 

```
car_x=10
car_y=270
while visibility:
    for events in pygame.event.get():
        # print(events)
        if events.type == pygame.QUIT:
            visibility=False
    window.blit(track,(0,0))
    window.blit(car_scal,(car_x,car_y))
    car_x=car_x+2
    pygame.display.update()
```
এখান আমাদের car সুন্দর করেই move করতেছে। কিন্তু এখানে একটা সমস্যা হল। বাম দিক থেকে গিয়ে ডান দিকে ট্র্যাক থেকে বের হয়ে যাচ্ছে। আমরা চাচ্ছি ট্র্যাক বের বাইরে জেন না জায়। 

## Step 4> Stop the Car before Track end
- আমাদের এখন উচিত ট্র্যাক শেষ হইয়ার আগেই গাড়িটা যেন আর সামনে না আগায়। অর্থাৎ car_x এঁর ভ্যালু যেন আর না বারে সেটা করা। 

- এটার জন্য আমরা একটা sensor এঁর মতো সাহায্য নিব। কিরকম সেন্সর। আসলে এটা কোনো সেন্সর না কিন্তু আমাদের সেন্সরের মতোই কাজ দিবে। সেটা কিরকম। ধরা জাঁক আমাদের সেন্সর টা থাকবে গাড়ির ঠিক মধ্যখানে। সেখান থেকে একটা জায়গা সামনে পর্যন্ত সেটার boundary থাকে অর্থাৎ এক কথায় দেখবে। দেখবে বলতে সেটা চেক করবে যে সাদা লাইন আছে নাকি কালো লাইন। এটাই হবে আমাদের সেন্সরের কাজ। 

- প্রথমেই সেই সেন্সরের অবস্থান কথায় হবে সেটা বলে দেই। গাড়ির ঠিক মাঝে অর্থাৎ অর্থমানে গাড়ির position যেখানে সেটা + গাড়ির অর্ধেক। অর্থাৎ গাড়ির position x + width/2.....গাড়ির position y + height/2.           এখানে width/ heigth এঁর কিছু উলট পালট হবে পারে। তাই যদি সঠিক না হয় তাহলে change করে দেখতে হবে। 
```
sensor_x=car_x + (220/2)
sensor_y= car_y + (170/2)
while visibility:
```

- এবার এক কাজ করা যাক এই sensor এঁর position এ একটা বিন্দু আকা যাক। 
```
    pygame.draw.circle(window,(0,255,0),(sensor_x,sensor_y),5,5)
    pygame.display.update()
```
এখনে কী হল? আমরা একটা circle draw করতে চাই। সেটা কোথায় হবে আমাদের window তে। আচ্ছা কী কালারের হবে? আমরা (0,255,0) mean (R,G,B) অর্থাৎ সবুজ কালারের দিলাম। পরের parameter হলও বিন্দিটার কেন্দ্র কোথায় হবে। আমরা তও বলেই দিয়েছি sensor_x, sensor_y তে। এঁর পরে হলো বিন্দুর radius কত হবে? আমি দিলাম ৫। এঁর পরে হলও thickness কত হবে আমি দিলাম ৫। 

- এখন যদি রান করি তাহলে দেখা যাবে বিন্দু আসছে কিন্তু সেটা একই জায়গায় স্থির হয়ে আছে। গাড়ির সাথে আগাচ্ছে না। এঁর কারণ গাড়ি x axis বরাবর তো move করতেছে, কিন্তু বিন্দু move তও করার কথা না। তাহলে আমরা এক কাজ করি সেন্সরের পজিশন এঁর ভ্যারিয়েবল গুলো আমারা while loop এঁর মধ্যে নইয়ে আসি। তাহলে car_x change হলেই আমাদের sensor_x change হয়ে যাবে। 

```
while visibility:
    sensor_x=car_x + (220/2)
    sensor_y= car_y + (170/2)
    for events in pygame.event.get():
        # print(events)
        if events.type == pygame.QUIT:
            visibility=False
    window.blit(track,(0,0))
    window.blit(car_scal,(car_x,car_y))
    car_x=car_x+2
    pygame.draw.circle(window,(0,255,0),(sensor_x,sensor_y),5,5)
    pygame.display.update()
```
