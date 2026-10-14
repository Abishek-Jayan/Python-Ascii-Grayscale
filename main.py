def main():
    '''
    Goal: Take a picture as input, display it using ascii art
    Constraints: No libraries, pure logic

    
    Steps:-
    1. Download a BMP file, display it in the terminal
    1. For each pixel in the image, print #
    2. If current pixel is black, skip. This represents space
    3.

    What questions I do need to solve to make my vision a reality?
    1. How to convert the image into grayscale without any library?
    a. What kind of file format will I start off with? BMP
    b. go over every pixel of the image and extract its alpha value. then set that as its rgb
        how to go over every pixel? i need to convert the data into a ___format
        how to extract alpha value?
    2. How to read the pixels of the image into Python 2D matrix of value range 0-1?
    3. How to map each value to a particular ascii character?
    4. How to 
    
. For File Parsing & Reading PixelsUncompressed Image Formats: Look into the file structure of PPM (Netpbm) or BMP. These formats store raw pixel data without complex compression algorithms, meaning you can read them with raw bytes.Python Binary I/O: Look up how Python handles binary files (open(..., 'rb')) and how to read specific byte sizes using built-in tools like the struct module.2. For Grayscale ConversionLuminance and Color Perception: Research how digital color channels (Red, Green, Blue) map to perceived brightness. Look up relative luminance and standard television/video color conversion weights (specifically how the human eye responds to different wavelengths of light).3. For Mapping Values to ASCIINormalization and Quantization: Look into how continuous numerical ranges (like floats from $0$ to $1$) get mapped or binned into discrete steps (like character indices in a fixed-size string).4. For Terminal Display & LayoutAspect Ratio Correction: Research why terminal grid cells are taller than they are wide, and look up basic image downsampling or nearest-neighbor grid sampling strategies to keep your art from looking stretched out.

    
    '''
    with open(blackbuck.bmp, mode='rb')as file:
        fileContent = file.read()

if __name__ == "__main__":
    main()
