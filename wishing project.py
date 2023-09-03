import time
time= time.strftime('%H:%M:%S')
print(time)
hour = time.strftime('%H')
print(hour)
minute = time.strftime('%M')
print(minute)
second = time.strftime('%S')
print(second)
   
 
if time>("00:00:00") and time< ("11:59:59"):
    print("good mrng sir !!")

elif time> ("12:00:00" ) and time< ("15:59:59"):
    print("good afternoon sir !!")

elif time> ("16:00:00 ") and time< ("18:59:59"):
    print ("good evening sir !!")

elif time> ("19:00:00") and time< ("23:59:59") :
    print("good nyt sir !!")


else:
    print("input error pls check it again !!")         
 


