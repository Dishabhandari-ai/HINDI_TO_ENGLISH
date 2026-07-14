import cv2
import os


def preprocess_image(input_path, output_path):

    image = cv2.imread(input_path)

    if image is None:
        raise FileNotFoundError(f"Image not found: {input_path}")

    height, width = image.shape[:2]

    max_size = 1000

    scale = min(max_size / width, max_size / height)

    new_width = int(width * scale)

    new_height = int(height * scale)

    resized = cv2.resize(
        image,
        (new_width, new_height),
        interpolation=cv2.INTER_AREA
    )

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    median = cv2.medianBlur(gray,3)

   

    binary = cv2.adaptiveThreshold(
        median,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (2, 2)
    )

    processed = cv2.morphologyEx(
        binary,
        cv2.MORPH_CLOSE,
        kernel
    )

    cv2.imwrite(output_path, processed)

    return output_path

if __name__ == "__main__":

    output2 = preprocess_image(
        "uploads/imgsample2.jpg",
        "outputs/processed_sample2.png"
    )

    print(output2)

    img = cv2.imread(output2)

    cv2.imshow("Processed", img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()    