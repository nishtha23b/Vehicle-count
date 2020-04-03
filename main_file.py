import cv2,time
car_cascade = cv2.CascadeClassifier("toy_car_cascade.txt")
bike_cascade = cv2.CascadeClassifier("toy_bike_cascade.txt")
truck_cascade = cv2.CascadeClassifier("toy_truck_cascade.txt")
carCount = 0
bikeCount = 0
truckCount = 0
video = cv2.VideoCapture(0)
while True:
    check,frame = video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
    bikes = bike_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
    trucks = truck_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
    
    for x, y, w, h in cars:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 3)
    for x, y, w, h in bikes:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 3)
    for x, y, w, h in trucks:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 225, 0), 3)
    
    cv2.rectangle(frame, ((0,frame.shape[0] -25)),(270, frame.shape[0]), (255,255,255), -1)
    cv2.imshow("Capturing Video" , frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
try:
    cv2.putText(frame, "Number of Cars detected: " + str(cars.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
    #print("Number of cars = " , str(cars.shape[0]))
    carCount = int(str(cars.shape[0]))
except:
    carCount = 0

try:
    cv2.putText(frame, "Number of Bike detected: " + str(bikes.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
    #print("Number of bikes = " , str(bikes.shape[0]))
    bikeCount = int(str(bikes.shape[0])) 
except:
    bikeCount = 0


try:
    cv2.putText(frame, "Number of cars detected: " + str(trucks.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)
    #print("Number of Trucks = " , str(trucks.shape[0]))
    truckCount = int(str(trucks.shape[0]))
except:
    truckCount = 0
    
print('Cars:- ' , carCount)
print('Bikes:- ' , bikeCount)
print('Trucks:- ' , truckCount)
def carTime(carNumber):
    if(carNumber == 0):
        return 0
    elif(carNumber >0 and carNumber <= 5):
        return 15
    elif(carNumber >5 and carNumber <=10 ):
        return 25
    else:
        return 45
    
def truckTime(truckNumber):
    if(truckNumber == 0):
        return 0
    elif(truckNumber >0 and truckNumber <=3):
        return 20
    else:
        return 40
def bikeTime(bikeNumber):
    if(bikeNumber == 0):
        return 0
    elif(bikeNumber > 0 and bikeNumber <= 10):
        return 20
    elif(bikeNumber > 10 and bikeNumber <= 20):
        return 40
    else:
        return 60 
timing = 5 + carTime(carCount) + truckTime(truckCount) + bikeTime(bikeCount)
timing = timing % 120
print("Signal Timing:- " , timing)
video.release()
cv2.destroyAllWindows()
