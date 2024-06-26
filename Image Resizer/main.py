import cv2

# Configurable Parameters
source = "hellocric.jpg"
destination = "newImage.jpg"
scale_present = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)

# percent by which the image is resized
scale_percent = 50

# calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (new_width, new_height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)
# cv2.waitKey(0)