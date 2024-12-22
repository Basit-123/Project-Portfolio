from PIL import Image, ImageFilter

def display_menu():
    print("\n--- PyPhotoshop ---")
    print("1. Open Image")
    print("2. Save Image")
    print("3. Resize Image")
    print("4. Rotate Image")
    print("5. Apply Blur")
    print("6. Apply Sharpen")
    print("7. Convert to Grayscale")
    print("8. Exit")

def open_image():
    path = input("Enter the path to the image: ")
    try:
        img = Image.open(path)
        print(f"Image {path} opened successfully!")
        return img
    except FileNotFoundError:
        print("Image not found. Please try again.")
        return None

def save_image(img):
    path = input("Enter the path to save the image (e.g., edited_image.jpg): ")
    try:
        img.save(path)
        print(f"Image saved as {path}.")
    except Exception as e:
        print(f"Failed to save image: {e}")

def resize_image(img):
    try:
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))
        resized = img.resize((width, height))
        print("Image resized successfully!")
        return resized
    except ValueError:
        print("Invalid dimensions. Please try again.")
        return img

def rotate_image(img):
    try:
        angle = int(input("Enter rotation angle (degrees): "))
        rotated = img.rotate(angle)
        print("Image rotated successfully!")
        return rotated
    except ValueError:
        print("Invalid angle. Please try again.")
        return img

def apply_blur(img):
    blurred = img.filter(ImageFilter.BLUR)
    print("Blur applied successfully!")
    return blurred

def apply_sharpen(img):
    sharpened = img.filter(ImageFilter.SHARPEN)
    print("Sharpen applied successfully!")
    return sharpened

def convert_grayscale(img):
    grayscale = img.convert("L")
    print("Image converted to grayscale successfully!")
    return grayscale

def main():
    img = None
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            img = open_image()
        elif choice == "2":
            if img:
                save_image(img)
            else:
                print("No image loaded. Please open an image first.")
        elif choice == "3":
            if img:
                img = resize_image(img)
            else:
                print("No image loaded. Please open an image first.")
        elif choice == "4":
            if img:
                img = rotate_image(img)
            else:
                print("No image loaded. Please open an image first.")
        elif choice == "5":
            if img:
                img = apply_blur(img)
            else:
                print("No image loaded. Please open an image first.")
        elif choice == "6":
            if img:
                img = apply_sharpen(img)
            else:
                print("No image loaded. Please open an image first.")
        elif choice == "7":
            if img:
                img = convert_grayscale(img)
            else:
                print("No image loaded. Please open an image first.")
        elif choice == "8":
            print("Exiting PyPhotoshop. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
