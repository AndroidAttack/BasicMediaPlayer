# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os

# This wil be an Art Gallery from my AI Image creator from bing
# I hope you think it's FABULOUS! :P
# Python doesn't need commas!
# completion of file names for music sequence, music filename, and image
# volume increase and decrease with new code to switch in between songs next
import pygame
# Adding Audio to GUI
from pygame import mixer

# Create in action (instance) for pygame to start
pygame.init()
# pre-initialize pygame.mixer
pygame.mixer.pre_init(frequency=44100, size=-16, channels=1, buffer=2 ** 12)
# init() channels refers to mono vs stereo, not playback Channel object
# ___________________Adding music to the files____________________

# to play music file code template source: https://www.geeksforgeeks.org/python-playing-audio-file-in-pygame/
# create a path variable to get audio from file folder
Audio_Directory = "audiofiles"
# Make a list of all the files in the audio folder
# python uses brackets!
Audio_Filenames = [audiofilename for audiofilename in os.listdir(Audio_Directory) if
                   audiofilename.endswith(".mp3") or audiofilename.endswith(".wav")]

# __________________________________________________________________________


# assigning values to X and Y variable
# These will be the new variables for width and height
X = 1000
Y = 800

# Create variables for width and height of screen
Window_Width = X  # didn't want to change variables ro replaced 1000 with Y
Window_Height = Y  # replaced 825  with  Y
# Create the object (Window)
window = pygame.display.set_mode((Window_Width, Window_Height))
# make a title for the window
pygame.display.set_caption("The Sad Truths")

# create a path variable to get images from file folder
Image_Directory = "images"
# Make a list of all the files in the images' folder
# python uses brackets!
Image_Filenames = [filename for filename in os.listdir(Image_Directory) if
                   filename.endswith(".jpg") or filename.endswith(".gif")]

# ______________________Making a Text Box to display image name______________________________________
# updating and showing the name of each picture as it changes!
# great challenge! I had to figure out that I had to put this code under the Image_Path because
# it wasn't recognized as active. I moved this code and then Image_Path worked to display on window

# code that helped from source: https://www.geeksforgeeks.org/python-display-text-to-pygame-window/#
# code for learning were to put text: https://www.geeksforgeeks.org/pygame-working-with-text/?ref=lbp

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
# Create the object
display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.Font('freesansbold.ttf', 32)
# text = font.render(file, True, green, blue)
# textRect = text.get_rect()
# textRect.topleft = (20, 20)


# going to work on updating name of pictures! :D


# _____________________________Making a textbox for Audio filename and Audio Play__________________________________
# dictionary objects are not callable
# list indices must be integers or slices, not float
# tuples take floats
# possible to call floats by slicing
# slicing is like sorting
musicfiles = []
# play music
initial_volume = 0.5

def music_volume(audio_path):
    pygame.mixer.init()
    # load song
    mixer.music.load(audio_path)
    # Set the initial volume; it should be a value between 0.0 and 1.0
    pygame.mixer.music.set_volume(initial_volume)
    # play song in loop
    mixer.music.play(-1)
    musicfiles.append(audio_path)
# _________________________________________________________________________________________
# This is for getting audiofile names
# index for audio files
# Make a textbox to show song on GUi
textbox_surface = pygame.display.set_mode((X, Y))

audios = []

for audiofilename in Audio_Filenames:
    audio_path = os.path.join(Audio_Directory, audiofilename)
    #play music
    music_volume(audio_path)
    audiofile = font.render(audio_path, True, green, blue)
    text_rect_two = audiofile.get_rect()
    text_rect_two.midleft = (20, 80)
    audios.append(audiofile)


# __________________________________Creating a list for images and image filenames___________________
# load images to be viewed in a loop
# Create a list to do so
# Create an empty list for the images to have it's own "space"
images = []
# index for image name
files = []

for filename in Image_Filenames:
    # get path to image and compare image to file allowed type
    Image_Path = os.path.join(Image_Directory, filename)
    # label variable image as loading action for image from image path
    image = pygame.image.load(Image_Path)
    # added a label variable for filename retrieving
    file = font.render(Image_Path, True, green, blue)
    # setup textbox
    text_rect = file.get_rect()
    text_rect.topleft = (20, 20)
    # add images to list from images
    images.append(image)
    # added this to show image name
    files.append(file)

# __________________________________________________________________________________

# ______________________ Main Program Loop - Display Images _______________________


# initial start for filename index
current_filename_index = 0
current_file = files[current_filename_index]
# initial start for image index
current_image_index = 0
current_image = images[current_image_index]
# initial start for audio index
current_audio_index = 0
current_audio = audios[current_audio_index]
# initial start for musicfile index
current_musicfiles_index = 0
current_musicfiles = musicfiles[current_musicfiles_index]

# Create a clock object to control the frame rate
clock = pygame.time.Clock()
# Create and start our main program loop
# Create a variable that it's running
# its best practice to put "is" before for recognition
is_running = True
# loop until running is set to false
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Color in window background
    window.fill((255, 255, 255))
    # Display current event on window
    # learn how to change picture size for window room
    window.blit(current_image, (0, 0))
    # display textbox and current filename
    display_surface.blit(current_file, text_rect)

    # DISPLAY TEXTBOX FOR audio file
    textbox_surface.blit(current_audio, text_rect_two)

    # Update the display
    pygame.display.flip()
    # __________Handle events in program________
    # Handle any events (When users press keys, button commands, or use timers)
    # nest "if" statements to do this
    for event in pygame.event.get():
        # if player  presses X on window
        if event.type == pygame.QUIT:
            # close program
            is_running = False
            # adding another key
            # find keys in pygame library on internet
        elif event.type == pygame.KEYDOWN:
            # now we can put different keys
            if event.key == pygame.K_RIGHT:
                # plus 1 means go right
                # len()
                # % means ????
                # changes images
                current_image_index = (current_image_index + 1) % len(images)
                # changes name to right
                current_filename_index = (current_filename_index + 1) % len(files)
                # change audio
                current_audio_index = (current_audio_index + 1) % len(audios)
                # change music file
                current_musicfiles_index = (current_musicfiles_index + 1) % len(musicfiles)
                # get the current image from the list using the current_image_index
                current_image = images[current_image_index]
                # the current file is the current index file
                current_file = files[current_filename_index]
                # the current file of audio
                current_audio = audios[current_audio_index]
                # the current file for music
                current_musicfiles = musicfiles[current_musicfiles_index]
                mixer.music.load(current_musicfiles)
                mixer.music.play(-1)
            elif event.key == pygame.K_LEFT:
                # change image to left
                current_image_index = (current_image_index - 1) % len(images)
                # changes name to Left
                current_filename_index = (current_filename_index - 1) % len(files)
                # change audio
                current_audio_index = (current_audio_index - 1) % len(audios)
                # change music file
                current_musicfiles_index = (current_musicfiles_index - 1) % len(musicfiles)
                # the current file of Image
                current_image = images[current_image_index]
                # the current file of Image filename
                current_file = files[current_filename_index]
                # the current file of audio
                current_audio = audios[current_audio_index]
                # the current file of music
                current_musicfiles = musicfiles[current_musicfiles_index]
                mixer.music.load(current_musicfiles)
                mixer.music.play(-1)
            elif event.key == pygame.K_UP:
                initial_volume += 0.1  # Increase volume
                if initial_volume > 1.0:
                    initial_volume = 1.0  # Cap at 1.0
                pygame.mixer.music.set_volume(initial_volume)
            elif event.key == pygame.K_DOWN:
                initial_volume -= 0.1  # Decrease volume
                if initial_volume < 0.0:
                    initial_volume = 0.0  # Floor at 0.0
                pygame.mixer.music.set_volume(initial_volume)

# _____________________________________________________________________________________________
# Set the frame rate to 30 frames per second
clock.tick(30)
# __________ END PROGRAMS_____________
# Stop the mixer
pygame.mixer.music.stop()
# Stop Pygame
pygame.quit()
