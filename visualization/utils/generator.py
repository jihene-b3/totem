import imageio
from os import listdir, makedirs, getcwd
from os.path import isfile, join, split, isdir
from selenium import webdriver
from time import sleep


def generate_pngs_from_htmls(source, destination, delay):
    htmls = []
    for file in listdir(source):
        splited_file = file.split(".")
        if splited_file[len(splited_file)-1] == "html":
            htmls.append(
                ('file://{path}/{mapfile}'.format(path=getcwd() + '/' + source, mapfile=file),
                    splited_file[0]
                 )
            )

    if not isdir(destination):
        makedirs(destination)

    for html in htmls:
        browser = webdriver.Firefox()
        browser.get(html[0])
        sleep(delay)
        browser.save_screenshot(destination+"/"+html[1]+".png")
        browser.quit()


def generate_gif_from_pngs(source, destination, speed):
    pngs = []
    d_folder, d_file = split(destination)
    for file in listdir(source):
        splited_file = file.split(".")
        if splited_file[len(splited_file)-1] == "png":
            pngs.append(imageio.imread(source + "/" + file))

    if not isdir(d_folder):
        makedirs(d_folder)

    imageio.mimwrite(destination, pngs, fps=speed)
