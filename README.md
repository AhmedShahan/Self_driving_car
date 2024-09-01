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