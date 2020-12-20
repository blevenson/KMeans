# Python script to run K-means on image
# @author Brett Levenson

import sys
import KMeans
import image

def main():
    print("Running K-means")
    
    if len(sys.argv) != 4:
        print("Usage: python3 main.py [K value] [input_image] [output_image]")
        exit(1)
    
    K_val = int(sys.argv[1])
    input_image = sys.argv[2]
    output_image = sys.argv[3]

    '''
    # Sample code to use k-means
    k_means = KMeans.KMeans(K=2)
    k_means.fit([[-20], [-10], [-40], [40], [-30], [30]])

    print(k_means.predict([-100]))
    print(k_means.predict([100]))
    '''

    img = image.Image(input_image)

    k_means_img = KMeans.KMeans(K=K_val, iters=10)
    img_bytes = img.get_byte_array()
    k_means_img.fit(img_bytes)

    for i in range(len(img_bytes)):
        img_bytes[i] = k_means_img.predict(img_bytes[i])

    img.save_image(img_bytes, output_image)
    
if __name__ == "__main__":
    main()
