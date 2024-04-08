def numberplate_to_text():
    from PIL import Image 
    from pytesseract import pytesseract     #pip install pytesseract  
    #pip install pytesseract 

    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    image_path = r"Numberplate.jpg"

# Opening the image & storing it in an image object 
    img = Image.open(image_path) 

# Providing the tesseract 
# executable location to pytesseract library 
    pytesseract.tesseract_cmd = path_to_tesseract 

# Passing the image object to 
# image_to_string() function 
# This function will 
# extract the text from the image 
    text = pytesseract.image_to_string(img) 

# Displaying the extracted text 
#print(text[:-1])
    return (text)

def cropped_numberplate(image_name):
    # import required libraries
    import cv2  # pip install opencv-python 
    import numpy as np
    # Read input image
    img = cv2.imread(image_name)

    # convert input image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cascade = cv2.CascadeClassifier('haarcascades\haarcascade_russian_plate_number.xml')

    # Detect license number plates
    plates = cascade.detectMultiScale(gray, 1.2, 5)
    print('Number of detected license plates:', len(plates))

    # loop over all plates
    for (x,y,w,h) in plates:
   
    # draw green bounding rectangle around the license number plate
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        gray_plates = gray[y:y+h, x:x+w]
        color_plates = img[y:y+h, x:x+w]
   
   # save number plate detected
        cv2.imwrite('Numberplate.jpg', gray_plates)
  
   #To show image - highlighted car number plate with green border
       # cv2.imshow('Number Plate Image', img)
    #To show image - cropped number plate
    #cv2.imshow('Number Plate', gray_plates)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
 
def clean_number(data):
#Note: Length or new indian cars number is 10 and first two Alphabets shows state code 
    data=data.replace(" ","")
    for i in range(0,len(data)):
        if data[i].isalpha() and data[i+1].isalpha():
            number= data[i:i+10]
            break   
    return number
