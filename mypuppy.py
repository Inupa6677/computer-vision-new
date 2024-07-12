import cv2

img = cv2.imread('Computer-Vision-with-Python/DATA/00-puppy.jpg')

while True:
    
    cv2.imshow('puppy', img)
    
    # If we waited at least 1 millisecond and wepressed the esc 
    if cv2.waitKey(1) & 0xff == 27:
        break
        
cv2.destroyAllWindows()
