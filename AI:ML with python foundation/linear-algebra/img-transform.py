import numpy as np
import matplotlib.pyplot as plt

heart_img = np.array([
    [255, 0, 0, 255, 0, 0, 255],
    [0, 255/2, 255/2, 0, 255/2, 255/2, 0],
    [0, 255/2, 255/2, 255/2, 255/2, 255/2, 0],
    [0, 255/2, 255/2, 255/2, 255/2, 255/2, 0],
    [255, 0, 255/2, 255/2, 255/2, 0, 255],
    [255, 255, 0, 255/2, 0, 255, 255],
    [255, 255, 255, 0, 255, 255, 255]
])

def save_image(image, name_identifier):
    plt.imshow(image, cmap="gray")
    plt.title(name_identifier)
    plt.axis('off')
    plt.savefig(f'{name_identifier}.png')
    plt.close()

# Save heart image
save_image(heart_img, "Heart")

# Invert color
inverted_heart_img = 255 - heart_img
save_image(inverted_heart_img, "Inverted_Heart")

# Rotate heart
rotated_heart_img = heart_img.T
save_image(rotated_heart_img, "Rotated_Heart")

# Random Image
random_img = np.random.randint(0, 255, (7, 7))
save_image(random_img, "Random_Image")

# Solve for heart image
x = np.linalg.solve(random_img, heart_img)
solved_heart_img = np.matmul(random_img, x)
save_image(x, "x")
save_image(solved_heart_img, "Solved_Heart_Image")
