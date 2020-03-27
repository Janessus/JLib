import os
import sys
import time
import math
import random



BOLD = '\033[1m'

RED='\033[31m'
GREEN='\033[32m'
YELLOW='\033[33m'
BLUE='\033[34m'

NC='\033[0m'  # No Color

UP='\033[1A'
DOWN='\033[1B'
LINESTART='\033[1000D'

OPENER='\033[43;0m' + RED
BARCOLOR='\033[48;5;234m' + GREEN
BG = '\033[48;5;234m'


# prints the the given text with a idle indicator
# prints: opening [progrator default="."] * (increasing)count [closing]
# adds a progrator every $delay seconds
def printWaiting(opening: str, progrator='.', count=4, delay=1, closing=""):
    print(" " * os.get_terminal_size()[0] + "\r", end="")
    for i in range(count):
        print(opening + progrator * i + closing + "\r", end="")
        time.sleep(delay)





class JProgressBar:
    def __init__(self, opening: str, progress=0.0, barOpener="|", progrator="|", antiProgrator="|", barCloser="|",
                 closing="", barWidth=100, showPercentage=True, matchTerminalSize=True, colorize=True):
        self.opening = opening
        self.progress = progress
        self.barOpener = barOpener
        self.progrator = progrator
        self.antiProgrator = antiProgrator
        self.barCloser = barCloser
        self.closing = closing
        self.barWidth = barWidth
        self.showPercentage = showPercentage
        self.matchTerminalSize = matchTerminalSize
        self.colorize = colorize
        self.ending = ""
        self.__update()


    def setProgress(self, progress):
        self.progress = progress
        self.__update()


    def __update(self):
        if self.matchTerminalSize:
            if self.progress > 100:
                self.progress = 100
            elif self.progress < 0:
                self.progress = 0
            size = os.get_terminal_size()[0]
            self.barWidth = size - len(self.opening + self.barOpener + self.barCloser + self.closing + " ")
            percentage = self.progress
            if self.showPercentage:
                self.barWidth -= len(" " + str(format(percentage, ".2f")) + "%")
            self.progress = percentage / 100 * self.barWidth
        else:
            if self.progress > self.barWidth:
                self.progress = self.barWidth
            elif self.progress < 0:
                self.progress = 0
            percentage = self.progress / self.barWidth * 100
        if self.showPercentage:
            self.ending = self.closing + " " + str(format(percentage, ".2f")) + "%"
        if self.colorize:
            self.shownText = BG + self.opening + " " + OPENER + BOLD + self.barOpener + NC + BOLD
            for i in range(int(self.progress)):
                if i >= .8 * self.barWidth:
                    self.shownText += RED
                elif i >= .5 * self.barWidth:
                    self.shownText += YELLOW
                else:
                    self.shownText += BARCOLOR
                if i % len(self.progrator) == 0:
                    self.shownText += self.progrator
            self.shownText += BLUE + self.antiProgrator * int(
                self.barWidth - len(self.progrator) * int(math.ceil(self.progress/len(self.progrator)))) + OPENER + BOLD + self.barCloser + NC + BG + GREEN + self.ending + NC
        else:
            self.shownText = self.opening + " " + self.barOpener + self.progrator * int(self.progress) + self.antiProgrator * int(
                self.barWidth - self.progress) +  self.barCloser + self.ending


    def printBar(self, opening="JProgressBar", progress=.0):
        self.progress = progress
        if opening != "JProgressBar":
            self.opening = opening
        self.__update()
        print(" " * os.get_terminal_size()[0] + "\r", end="")
        print(self.shownText + "\r", end="")


class JBarPrinter:
    def __init__(self):
        self.bars = list()

    def addBar(self, bar: JProgressBar):
        self.bars.append(bar)

    def updateBar(self, n, progress):
        if n < len(self.bars):
            self.bars[n].setProgress(progress)

    def refresh(self):
        for bar in self.bars:
            bar.printBar()
            print(DOWN, end="")





















def progressBar(opening: str, progress=0.0, barOpener="[", progrator="|", antiProgrator=" ", barCloser="]", closing="", barWidth=100, showPercentage=True, matchTerminalSize=True, colorize=True):
    if matchTerminalSize:
        if progress > 100:
            progress = 100
        elif progress < 0:
            progress = 0
        size = os.get_terminal_size()[0]
        barWidth = size - len(opening + barOpener + barCloser + closing)
        percentage = progress
        if showPercentage:
            barWidth -= len(" " + str(format(percentage, ".2f")) + " %")
        progress = percentage/100 * barWidth
    else:
        if progress > barWidth:
            progress = barWidth
        elif progress < 0:
            progress = 0
        percentage = progress/barWidth*100
    if showPercentage:
        closing = closing + " " + str(format(percentage, ".2f")) + "%"

    print(" " * os.get_terminal_size()[0] + "\r", end="")

    if colorize:
        shownText = BG + opening + " " + OPENER + barOpener + NC + BOLD
        for i in range(int(progress)):
            if i >= .8 * barWidth:
                shownText += RED
            elif i >= .65 * barWidth:
                shownText += YELLOW
            else:
                shownText += BARCOLOR
            shownText += progrator
        shownText += BLUE + antiProgrator * int(barWidth - progress) + OPENER + barCloser + NC + BG + GREEN + closing + NC
    else:
        shownText = opening + " " + barOpener + progrator * int(progress) + antiProgrator * int(barWidth - progress) + barCloser + closing
    print(shownText + "\r", end="")


def printColors():
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print(u"\u001b[0m")

    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
        print(u"\u001b[0m")


#printColors()
print("\n\n")
try:
    p = JProgressBar("Bar1")
    bp = JBarPrinter()
    bp.addBar(p)
    bp.addBar(p)
    bp.addBar(JProgressBar("Bar2"))

    while True:
        for i in range(0, 10_001, 10):
            bp.refresh()
            bp.updateBar(0, random.random() * 100.0)
            bp.updateBar(1, random.random() * 100.0)
            #p.printBar(progress=(i/100))
            time.sleep(.1)
        time.sleep(1)
except KeyboardInterrupt:
    pass
print("\n\n")