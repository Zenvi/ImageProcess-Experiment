import cv2
import os

png_path = './png_files/1/'
all_files = os.listdir(png_path)
cv2.namedWindow("PNG Pictures", 0)

index = 0
break_signal = 0
while True:

    if index < 0:
        index = index % (-len(all_files))
    else:
        index = index % len(all_files)

    png_file = all_files[index]


    if not png_file.endswith('.png'):
        continue

    png_image = cv2.imread(os.path.join(png_path, png_file), 0)
    cv2.imshow('PNG Pictures', png_image)
    print('On file: {}, shape: {}'.format(png_file, png_image.shape))

    while True:
        button_pressed = cv2.waitKey(0)
        if button_pressed & 0xFF == ord('d'):
            index += 1
            break
        elif button_pressed & 0xFF == ord('a'):
            index -= 1
            break
        elif button_pressed & 0xFF == ord('q'):
            break_signal = 1
            break
        else:
            print('Wrong move, please try again')

    if break_signal:
        break

    cv2.destroyAllWindows()
