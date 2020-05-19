import tkinter as t
import PIL
import cv2
from PIL import ImageOps, Image, ImageTk, ImageEnhance

# window setup
width = 20
window = t.Tk()
window.geometry('400x1000')
# sets window icon to a pic of parchment
window.iconbitmap("cover.ico")
# sets window title
window.title("Image Manipulation")
# label to tell user to enter file in entry box below
t.Label(window, text="Enter file name:", width=width).grid(column=0, row=0)
imageName = t.Entry(window, width=width)
imageName.grid(column=0, row=1)
# label letting user know the box below contains the name of the last image saved
lastImage = t.Label(window, text="The last image saved:", width=width)
lastImage.grid(column=1, row=0)
last = t.Label(window, text="NONE", width=width, border=5, relief="solid", bg="white", font=("Helvetica", 8))
last.grid(column=1, row=1)


def crop(image1, factor):
    """
    Crops a given image
    :param image1: String-file name of image to be cropped
    :param factor: String- factor of crop, image will have size/factor
    pixels removed on each side
    :return: String-the file location of the newly created cropped image
    """
    name = image1
    image1 = Image.open(image1)
    image2 = ImageOps.crop(image1, image1.size[1] // int(factor))  # dividing height of image by 4
    image2.save(r"C:\Users\zobok\compScience\EFIP\GUILearning\cropped" + factor + "-" + name)
    return "cropped" + factor + "-" + name


def colorize(image1, c1, c2):
    """
    Colorizes a given image with given set of two colors
    color order will change result
    :param image1: String- file name of image
    :param c1: String- first color
    :param c2: String-Second color
    :return: String-the file location of the newly created colorized image
    """
    name = image1
    image1 = Image.open(image1)
    image2 = ImageOps.colorize(image1, c1, c2)
    image2.save(r"C:\Users\zobok\compScience\EFIP\GUILearning\colorized-" + c1 + "-" + c2 + "-" + name)
    return "colorized-" + c1 + "-" + c2 + "-" + name


def autoContrast(image1, percentage):
    """
    Increases contrast of a given image
    This function calculates a histogram of the input image,
    removes cutoff percent of the lightest and darkest pixels
    from the histogram, and remaps the image so that the darkest pixel
    becomes black (0), and the lightest becomes white (255).
    :param image1: String-file location of image
    :param percentage: String-percentage of input range being cut off
    :return: String-the file location of the newly created auto contrasted image
    """
    name = image1
    image1 = Image.open(image1)
    image2 = ImageOps.autocontrast(image1, int(percentage), 0)
    image2.save(r"C:\Users\zobok\compScience\EFIP\GUILearning\autoContrast" + percentage + "-" + name)
    return "autoContrast" + percentage + "-" + name


def enhancingBrightness(image1, factor):
    """
    Enhances the brightness of an image
    :param image1:String- file location
    :param factor: String- enchantment factor
    " An enhancement factor of 0.0 gives a black image.
    A factor of 1.0 gives the original image.”
    :return: String-the file location of the newly created brighter image
    """
    name = image1
    image1 = Image.open(image1)
    temp = ImageEnhance.Brightness(image1)  # temp is a var we can perform a brightness enhancement on
    image2 = temp.enhance(float(factor))  # Preform enhancement with a factor of 1.6 and set that new enhance image
    image2.save(r"C:\Users\zobok\compScience\EFIP\GUILearning\brightness" + factor + "-" + name)
    return "brightness" + factor + "-" + name


def enhancingSharpness(image1, factor):
    """
    Enhaces the shapness of an image by a given factor
    :param factor: String_ factor to adjust shaprness by
    "a factor of 1.0 gives the original image,
    and a factor of 2.0 gives a sharpened image.”
    :param image1:String- file name of image
    :return:String-the file location of the newly created sharper image
    """
    name = image1
    image1 = Image.open(image1)
    temp = PIL.ImageEnhance.Sharpness(image1)
    image2 = temp.enhance(float(factor))
    image2.save(r"C:\Users\zobok\compScience\EFIP\GUILearning\sharpened" + factor + "-" + name)
    return "sharpened" + factor + "-" + name


def getSize(image1):
    """
    gets the image size of a given image
    :param image1: string-file name of image
    :return: String- the image size
    """
    img = Image.open(image1)
    size = img.size
    return str(size)


def getType(image1):
    """
    gets type of image given and returns it as a string
    :param image1: String- file location of image
    :return: String-format of given image
    """
    img = Image.open(image1)
    formatType = str(img.format)
    return formatType


def captureFromCam():
    vid = cv2.VideoCapture(0)
    img_counter = 0;
    while (True):
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        if not ret:
            print("failed to grab frame")
            break
        frame = cv2.flip(frame, 1)
        # Display the resulting frame
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            # SPACE pressed
            # string of name we will give image
            img_name = "opencv_frame_{}.png".format(img_counter)
            # save image frame as img_name
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    vid.release()
    cv2.destroyAllWindows()


def makeCroppedButton(row):
    """
    Makes the cropped button and its event function, cropPushed, it also makes a label to tell the user what to put into
    and entry box it creates for the crop factor.
    There is another label above the entry box that provides the restrictions on the possible inputs in to the box.
    When the cropped button is pressed the original image in the imageName box is shown, then that image is cropped
    according to the scale factor in the factor entry and the new image is displayed
    :return: Int: how many rows down the making of this button, labels and entry caused
    """
    enterFactorLabel = t.Label(window, text="Enter scale factor: ", bg="purple", fg="white", width=width, borderwidth=5,
                               relief="ridge")
    enterFactorLabel.grid(column=0, row=row + 1)
    restrictionLabel = t.Label(window, text="int x, removed=size/x", bg="purple", fg="white", width=width,
                               borderwidth=5,
                               relief="ridge")
    restrictionLabel.grid(column=1, row=row)

    factor = t.Entry(window, width=width)
    factor.grid(column=1, row=row + 1)

    def cropPushed():
        """
        This is the event that occurs when the cropped button is pressed
        It calls crop which crops the image according to a scale value
        It opens both the original and new images
        It also changes the value of the last saved image according
        :return: NONE
        """
        # checks to make sure there is an image and a factor
        if len(imageName.get()) != 0 and len(factor.get()) != 0:
            image1 = Image.open(imageName.get())
            image1.show()
            # calling crop which will return the file location of the new image
            image = crop(imageName.get(), factor.get())
            image2 = Image.open(image)
            image2.show()
            last.configure(text=image)

    cropButton = t.Button(window, text="Crop", bg="purple", fg="white", width=width, command=cropPushed)
    cropButton.grid(column=0, row=row)
    return row + 2


def makeAutoContrastButton(row):
    """
    Makes the auto contrast button and its event function, autoContrastPushed, it also makes a label to tell the user
    what to put into the entry box it creates for the cut off percentage.
    There is another label above the entry box that provides the restrictions on the possible inputs in to the box.
    When the autoContrast button is pressed the original image in the imageName box is shown, then that image is
    contrasted according to the cutoff percentage in the percentage entry and the new image is displayed
    :param row: int- the row we start placing at
    :return: Int: how many rows down the making of this button, labels and entry caused
    """

    enterPercentageLabel = t.Label(window, text="Enter cut off percentage: ", bg="blue", fg="white", width=width,
                                   borderwidth=5,
                                   relief="ridge")
    enterPercentageLabel.grid(column=0, row=row + 1)
    guideLabel = t.Label(window, text="Int w/in 0-100", bg="blue", fg="white", width=width, borderwidth=5,
                         relief="ridge")
    guideLabel.grid(column=1, row=row)

    percentage = t.Entry(window, width=width)
    percentage.grid(column=1, row=row + 1)

    def autoContrastPushed():
        """
        This is the event that occurs when the auto contrast button is pressed
        It calls autoContrast which changes the contrast of the image according to a cut off percentage
        It opens both the original and new images
        It also changes the value of the last saved image according
        :return: NONE
        """
        print(len(imageName.get()))
        if len(imageName.get()) != 0 and len(percentage.get()) != 0:
            image1 = Image.open(imageName.get())
            image1.show()
            image = autoContrast(imageName.get(), percentage.get())
            image2 = Image.open(image)
            image2.show()
            last.configure(text=image)

    contrastButton = t.Button(window, text="Auto Contrast", bg="blue", fg="white", width=width,
                              command=autoContrastPushed)
    contrastButton.grid(column=0, row=row)
    return row + 2


def makeColorButton(row):
    """
    Makes the colorize button and its event function, colorPushed, it also makes a label to tell the user
    what to put into the entry box it creates for the cut off percentage.
    When the colorize button is pressed the original image in the imageName box is shown, then that image is
    colorized according to colors, c1 & c2 in their corresponding entry boxes and the new image is displayed
    :param row: int- the row we start placing at
    :return: Int: how many rows down the making of this button, labels and entry caused
    """
    enterColorsLabel = t.Label(window, text="Enter 2 colors: ", bg="orangeRed3", fg="white", width=width, borderwidth=5,
                               relief="ridge")
    enterColorsLabel.grid(column=1, row=row)
    # c1 and c2 correspond to the color entries
    c2 = t.Entry(window, width=width)
    c2.grid(column=1, row=row + 1)
    c1 = t.Entry(window, width=width)
    c1.grid(column=0, row=row + 1)

    def colorPushed():
        """
        This is the event that occurs when the colorize button is pressed
        It calls colorize which changes the colors of the image according to 2 given colors
        It opens both the original and new images
        It also changes the value of the last saved image according
        :return: NONE
        """
        print(len(imageName.get()))
        if len(imageName.get()) != 0 and len(c1.get()) != 0 and len(c2.get()) != 0:
            image1 = Image.open(imageName.get())
            image1.show()
            image = colorize(imageName.get(), c1.get(), c2.get())
            image2 = Image.open(image)
            image2.show()
            last.configure(text=image)

    colorizeButton = t.Button(window, text="Colorize", bg="orangeRed3", fg="white", width=width, borderwidth=2,
                              command=colorPushed)
    colorizeButton.grid(column=0, row=row)
    return row + 2


def makeBrightnessButton(row):
    """
    Makes the brightness button and its event function, brightPushed, it also makes a label to tell the user
    what to put into the entry box it creates for the brightness factor
    There is another label above the entry box that provides the restrictions on the possible inputs in to the box.
    When the brightness button is pressed the original image in the imageName box is shown, then that image is
    made brighter according to factor and shown
    :param row: int- the row we start placing at
    :return: Int: how many rows down the making of this button, labels and entry caused
    """
    do = t.Label(window, text="Enter brightness factor:", bg="violetRed3", fg="white", width=width, borderwidth=5,
                 relief="ridge")
    do.grid(column=0, row=row + 1)

    l1 = t.Label(window, text="Num w/in 1-2", bg="violetRed3", fg="white", width=width, borderwidth=5,
                 relief="ridge")
    l1.grid(column=1, row=row)
    factor = t.Entry(window, width=width)
    factor.grid(column=1, row=row + 1)

    def brightPushed():
        """
        This is the event that occurs when the brightness button is pressed
        It calls enhancingBrightness which changes the brightness of the image according to a factor
        It opens both the original and new images
        It also changes the value of the last saved image according
        :return: NONE
        """
        if len(imageName.get()) != 0 and len(factor.get()) != 0:
            image1 = Image.open(imageName.get())
            image1.show()
            image = enhancingBrightness(imageName.get(), factor.get())
            image2 = Image.open(image)
            image2.show()
            last.configure(text=image)

    brightButton = t.Button(window, text="Brightness", bg="violetRed3", fg="white", width=width, borderwidth=2,
                            command=brightPushed)
    brightButton.grid(column=0, row=row)
    return row + 2


def makeSharpButton(row):
    """
    Makes the sharpness button and its event function, sharptPushed, it also makes a label to tell the user
    what to put into the entry box it creates for the sharpener factor.
    There is another label above the entry box that provides the restrictions on the possible inputs in to the box.
    When the sharpness button is pressed the original image in the imageName box is shown, then that image is
    sharpened according to the factor entry and the new image is displayed
    :param row: int- the row we start placing at
    :return: Int: how many rows down the making of this button, labels and entry caused
    """
    sharpLabel = t.Label(window, text="Enter Sharpness factor:", bg="darkGreen", fg="white", width=width, borderwidth=5,
                         relief="ridge")
    sharpLabel.grid(column=0, row=row + 1)

    restrictionLabel = t.Label(window, text="Num w/in 1-2", bg="darkGreen", fg="white", width=width, borderwidth=5,
                               relief="ridge")
    restrictionLabel.grid(column=1, row=row)
    factor = t.Entry(window, width=width)
    factor.grid(column=1, row=row + 1)

    def sharpPushed():
        """
        This is the event that occurs when the sharpen button is pressed
        It calls enhancingSharpness which changes the sharpness of the image according to a factor
        It opens both the original and new images
        It also changes the value of the last saved image according
        :return: NONE
        """
        print(len(imageName.get()))
        if len(imageName.get()) != 0 and len(factor.get()) != 0:
            image1 = Image.open(imageName.get())
            image1.show()
            image = enhancingSharpness(imageName.get(), factor.get())
            image2 = Image.open(image)
            image2.show()
            last.configure(text=image)

    sharpButton = t.Button(window, text="Sharpness", bg="darkGreen", fg="white", width=width, borderwidth=2,
                           command=sharpPushed)
    sharpButton.grid(column=0, row=row)
    return row + 2


def getSizeButton(row):
    """
    Makes the size button and its event function, sizePushed
    when pushed the label sizeLabel changes to show the dimensions
    :param row: int- the row we start placing at
    :return: Int: how many rows down the making of this button, labels and entry caused
    """
    sizeLabel = t.Label(window, text="Size:", bg="deepPink4", fg="white", width=width, borderwidth=5,
                        relief="ridge")
    sizeLabel.grid(column=1, row=row)

    def sizePushed():
        """
         This is the event that occurs when the size button is pressed
         It calls getSize which gets the size of an image
         It changes sizeLabel to the returned size
         :return: NONE
         """
        print(len(imageName.get()))
        if len(imageName.get()) != 0:
            size = getSize(imageName.get())
            sizeLabel.configure(text="Size: " + size)

    sizeButton = t.Button(window, text="Size", bg="deepPink4", fg="white", width=width, borderwidth=2,
                          command=sizePushed)
    sizeButton.grid(column=0, row=row)
    return row + 1


def getFormatButton(row):
    """
    Makes the format button and its event function, formatPushed
    when pushed the label format Label changes to show the format of the image
    :param row: int- the row we start placing at
    :return: Int: how many rows down the making of this button, labels and entry caused
    """
    formatLabel = t.Label(window, text="Format:", bg="steelBlue", fg="white", width=width, borderwidth=5,
                          relief="ridge")
    formatLabel.grid(column=1, row=row)

    def formatPushed():
        """
         This is the event that occurs when the format button is pressed
         It calls getType which gets the format of an image
         It changes formatLabel to the returned format
         :return: NONE
         """
        print(len(imageName.get()))
        if len(imageName.get()) != 0:
            formatType = getType(imageName.get())
            formatLabel.configure(text="Format: " + formatType)

    formatButton = t.Button(window, text="Format", bg="steelBlue", fg="white", width=width, borderwidth=2,
                            command=formatPushed)
    formatButton.grid(column=0, row=row)
    return row + 1


def makeLiveViewButton(row):
    def openPressed():
        captureFromCam()

    openCamera = t.Button(text="Live Camera View", bg="fireBrick4", fg="white", width= width, command=openPressed)
    openCamera.grid(column=0, row=row)
    return row


def blankLine(row):
    """
    inserts a blank line/label in columns 0 and 1 at a given row
    :param row: int-row number
    :return: int- row number increased by 1
    """
    t.Label(window, text="", width=width).grid(column=0, row=row)
    t.Label(window, text="", width=width).grid(column=1, row=row)
    return row + 1


def makeButtons():
    """
    makes the button for the gui
    uses an int row to keep track of where to place widgets
    hopefully this wil make for easy modification/ rearranging
    :return: NONE
    """
    row = 2
    row = blankLine(row)
    row = makeCroppedButton(row)
    row = blankLine(row)
    row = makeAutoContrastButton(row)
    row = blankLine(row)
    row = makeColorButton(row)
    row = blankLine(row)
    row = makeBrightnessButton(row)
    row = blankLine(row)
    row = makeSharpButton(row)
    row = blankLine(row)
    row = getSizeButton(row)
    row = blankLine(row)
    row = getFormatButton(row)
    row = blankLine(row)
    row = makeLiveViewButton(row)


def runGui():
    """
    calls a function to make buttons and opens the window
    :return: NONE
    """
    makeButtons()
    window.mainloop()


def main():
    """
    main function
    :return: NONE
    """
    runGui()


if __name__ == '__main__':
    main()
