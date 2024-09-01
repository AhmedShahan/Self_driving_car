# Self Driving Car
- At firt Create a png file where there a Stright Line Road. Background is Black and Road Color is White. (road/road1.png)
- instal pygame
```
pip install pygame
```
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
window= pygame.display.set_mode(1200,720)
```
- একন আমরা চাচ্ছি ওই window তে আমাদের পিকচার টা দেখাক এবং সেটা দেখাতেই থাকবে মানে while loop যতক্ষণ না আমরা কেটে দিচ্ছি। 
```
while True: 
```
- এখন পিকচার দেখানোর জন্য window এঁর function হলো blit যার পুরো meaning Bl= Block I= Image T= Transform
