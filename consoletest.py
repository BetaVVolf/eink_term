#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)


from waveshare_epd import epd2in13_V3
from PIL import Image, ImageDraw, ImageFont
import time

# Function to simulate capturing tty1 content (reads from a text file for demonstration)
def capture_tty1_simulated():
    typeout = input()
    return typeout

# Initialize the e-ink display
def init_display():
    epd = epd2in13_V3.EPD()
    epd.init()
    return epd

# Create an image from the captured text
def create_text_image(epd, text):
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)

    # Define the font and size
    # Adjust the font path or size as needed. Using a smaller font size can display more text.
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)

    # Split the text into lines so it fits on the screen
    lines = []
    words = text.split()
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 36:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
            if len(current_line) > 36:
                lines.append(current_line[:36])
                current_line = current_line[36:]
    if current_line:
        lines.append(current_line.strip())

    for i, line in enumerate(lines):
        draw.text((0, i * 15), line, font=font, fill=0)

    return image

    return image

# Display the image on the e-ink display
def display_image(epd, image):
    epd.display(epd.getbuffer(image))
    time.sleep(2)  # Display the image for 2 seconds

# Main function to run the program
def main():
    epd = init_display()
    tty1_content = capture_tty1_simulated()  # In a real scenario, replace this with actual tty1 content capture
    text_image = create_text_image(epd, tty1_content)
    display_image(epd, text_image)
    epd.sleep()  # Put the display to sleep to prevent burn-in

if __name__ == '__main__':
    main()
