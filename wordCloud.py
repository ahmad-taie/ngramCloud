import sys
from wordcloud import WordCloud
from PIL import ImageColor


ngramFreqList = {}
wordSurpList = {}

def get_colorFunc(color1, color2):

    r1, g1, b1 = ImageColor.getrgb(color1)
    r2, g2, b2 = ImageColor.getrgb(color2)

    minR = min(r1,r2)
    minB = min(b1,b2)
    minG = min(g1,g2)

    rangeR = max(r1,r2) - minR
    rangeB = max(b1,b2) - minB
    rangeG = max(g1,g2) - minG

    def getRGB(fract):
        """
        returns color based on fraction starting from min and to max
        """
        R = minR + fract*rangeR
        G = minG + fract*rangeG
        B = minB + fract*rangeB
        return R, G, B

    return getRGB


def get_bicolor_func(color1, color2, wordsurp):
    #('deepskyblue') or ('#00b4d2')

    # First get the max of surpr. values to normalize with it
    maxSurp = wordsurp[max(wordSurpList, key=wordSurpList.get)]

    def colorByWordfunc(word=None, font_size=None, position=None,
                          orientation=None, font_path=None, random_state=None):

        valueSurpColor = 1 - (wordsurp[word]/maxSurp)
        rgbFunc = get_colorFunc(color1, color2)
        r, g, b = rgbFunc(valueSurpColor)
        return 'rgb({:.0f}, {:.0f}, {:.0f})'.format(r,g,b)

    return colorByWordfunc


def parseInput(args):

    # fileName, color1, color2

    gramsFile = "testgrams.txt"
    color1 = 'red'
    color2 = 'yellow'

    argCount =  len(args)
    if argCount > 1:
        gramsFile = args[1]
        if argCount > 2:
            color1 = args[2]
            if argCount > 3:
                color2 = args[3]

    return gramsFile, color1, color2


def mainCloud():

    gramsFile, color1, color2 = parseInput(sys.argv)

    with open(gramsFile) as attributes:
        # Parse the  file
        for line in attributes:
            line = line.split()
            word = " ".join(line[:-2])
            wordSurpList[word] = (float(line[-1]))
            ngramFreqList[word] = int(line[-2])

    funColor = get_bicolor_func(color1, color2, wordSurpList)

    # Generate a word cloud image
    wordcloud = WordCloud(background_color="white", color_func=funColor)
    wordcloud.generate_from_frequencies(ngramFreqList)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()



mainCloud()