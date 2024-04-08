

import image_to_text #My own created module having function numberplate_to_text()


image_to_text.cropped_numberplate("2.jpeg")
number=image_to_text.numberplate_to_text()
print("From image car number",number)
print("Cleaned car number is ", image_to_text.clean_number(number))
