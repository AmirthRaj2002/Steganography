# IMPLEMENTATION AND ANALYSIS OF HYBRID DCT-DWT DIGITAL WATERMARKING

# Hybrid Watermarking System

## Project Introduction
In today's digital age, protecting multimedia content from unauthorized access is crucial. This project presents a **hybrid watermarking system** that combines **Discrete Wavelet Transform (DWT)**, **Discrete Cosine Transform (DCT)**, and **Singular Value Decomposition (SVD)** to secure digital assets.

### Key Components
1. **Watermark Selection**: Users can choose a watermark based on their data type and visibility preferences.
2. **DWT Embedding**: The host image is decomposed into four sub-bands. A chosen sub-band is divided into 4x4 blocks, where the watermark is embedded into the DCT coefficients using pseudorandom sequences.
3. **SVD Integration**: SVD is used to enhance robustness by embedding the watermark in the singular values of the transformed image, making it less susceptible to attacks and distortions.
4. **DWT Extraction**: The watermarked image is analyzed to retrieve the embedded watermark.
5. **DCT Modules**: Optional modules enhance data authentication and detect any modifications in the image.

This approach allows for **blind watermarking**, meaning the original image is not needed for watermark extraction, making it practical for real-world applications.

## Algorithm Steps for water.py
The algorithm for the hybrid watermarking system integrates DWT, DCT, and SVD. Below are the steps implemented in the code:

1. **Resize Images**: The cover image is resized to \(512 \times 512\) pixels, and the watermark image is resized to \(256 \times 256\) pixels.

2. **Preprocessing**:
   - Convert the cover image to a float32 format and normalize it to the range [0, 1].
   - Perform a 2D DWT on the cover image using the Haar wavelet, resulting in approximation (\(cA\)) and detail coefficients (\(cH, cV, cD\)).

3. **Watermark Transformation**:
   - Convert the watermark image to float32 and apply DCT to obtain the frequency components.

4. **SVD Decomposition**:
   - Perform SVD on the DCT-transformed approximation \(cA_dct\) and the watermark image, obtaining the matrices \(u, s, v\) for both.

5. **Embedding**:
   - Create a new singular value matrix by adding the scaled singular values of the watermark to the singular values of the DCT-transformed approximation:
     - Set an embedding factor \(\alpha\) (e.g., \(\alpha = 10\)).
     - Embed the watermark's singular values into the cover's singular values.

6. **SVD Reconstruction**:
   - Perform SVD on the modified singular value matrix to reconstruct the watermarked approximation.
   - Use the reconstructed singular values to form the new matrix for \(W_{modi}\).

7. **Inverse Transformations**:
   - Apply inverse DCT to the modified approximation.
   - Finally, apply inverse DWT to combine the modified approximation with the original detail coefficients to generate the watermarked image.

8. **Display the Watermarked Image**: Show the resulting watermarked image.

This algorithm leverages the strengths of DWT, DCT, and SVD to create a robust watermarking system that is imperceptible under specific conditions.


# PSNR Value Calculation Algorithm for psnr.py

This algorithm calculates the Peak Signal-to-Noise Ratio (PSNR) between two images. It is commonly used in image processing to evaluate the quality of an image compared to a reference image.

## Algorithm Steps:
1. **Load Images**: Load the original and contrast images using OpenCV's `cv2.imread` method.
2. **Resize Image**: Resize the original image to a specific size, if needed.
3. **Mean Squared Error (MSE)**: 
   - Compute the pixel-by-pixel difference between the two images.
   - Square the difference and calculate the mean.
   - If MSE is 0, return a PSNR of 100 (indicating identical images).
4. **PSNR Calculation**:
   - Use the formula: 
     \[
     PSNR = 20 \cdot \log_{10}\left(\frac{{\text{{PIXEL\_MAX}}}}{{\sqrt{{MSE}}}}\right)
     \]
   - `PIXEL_MAX` is the maximum possible pixel value (typically 255 for 8-bit images).
5. **Return PSNR**: The result is printed as the PSNR value.



