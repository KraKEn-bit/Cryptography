from PIL import Image
import numpy as np

# Load images (both should be same size)
img1 = Image.open("Charles_Babbage_Original.jpg").convert("RGB")
img2 = Image.open("Charles_Babbage_Original.jpg").convert("RGB")  # you can replace with another image

# Convert to NumPy arrays
arr1 = np.array(img1)
arr2 = np.array(img2)

# Apply bitwise operations
and_img = np.bitwise_and(arr1, arr2)
or_img  = np.bitwise_or(arr1, arr2)
xor_img = np.bitwise_xor(arr1, arr2)

# Convert back to images
and_result = Image.fromarray(and_img)
or_result  = Image.fromarray(or_img)
xor_result = Image.fromarray(xor_img)

# Save results
and_result.save("AND_result.jpg")
or_result.save("OR_result.jpg")
xor_result.save("XOR_result.jpg")

# Show results
and_result.show()
or_result.show()
xor_result.show()
