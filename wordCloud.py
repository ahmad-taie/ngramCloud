import sys
from wordcloud import WordCloud
import wordcloud
from PIL import ImageColor
import colorsys


def get_color(amount):
    assert 0 <= red_to_green <= 1
    # in HSV, red is 0 deg and green is 120 deg (out of 360);
    # divide red_to_green with 3 to map [0, 1] to [0, 1./3.]
    hue = red_to_green / 3.0
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    return map(lambda x: int(255 * x), (r, g, b))


def get_bicolor_func(color, wordsurp):#color1, color2, wordSurpList):
    """Create a color function which returns a single hue and saturation with.
    different values (HSV). Accepted values are color strings as usable by
    PIL/Pillow.
    #>>> color_func1 = get_single_color_func('deepskyblue')
    #>>> color_func2 = get_single_color_func('#00b4d2')
    """

    # First get the range of surprisal values to normalize it
    maxSurp = wordsurp[max(wordSurpList, key=wordSurpList.get)]
    #print(maxSurp)

    old_r, old_g, old_b = ImageColor.getrgb(color)
    rgb_max = 255.
    h, s, v = colorsys.rgb_to_hsv(old_r / rgb_max, old_g / rgb_max,
                                  old_b / rgb_max)

    def single_color_func(word=None, font_size=None, position=None,
                          orientation=None, font_path=None, random_state=None):
        """Random color generation.
        Additional coloring method. It picks a random value with hue and
        saturation based on the color given to the generating function.
        Parameters
        ----------
        word, font_size, position, orientation  : ignored.
        random_state : random.Random object or None, (default=None)
          If a random object is given, this is used for generating random
          numbers.
        """
        valueSurpColor = wordsurp[word]/maxSurp
        r, g, b = colorsys.hsv_to_rgb(h, s, valueSurpColor)
        return 'rgb({:.0f}, {:.0f}, {:.0f})'.format(r * rgb_max, g * rgb_max,
                                                    b * rgb_max)
    return single_color_func

if len(sys.argv) > 1:
    gramsFile = sys.argv[1]
else:
    gramsFile = "testgrams.txt"

ngramFreqList = {}
wordSurpList = {}

with open(gramsFile) as attributes:
    # Parse the  file
    for line in attributes:
        line = line.split()
        word = " ".join(line[:-2])
        wordSurpList[word] = (float(line[-1]))
        ngramFreqList[word] = int(line[-2])

print(ngramFreqList)
print(wordSurpList)

amanshofkda = get_bicolor_func('deepskyblue',wordSurpList)

funColor = wordcloud.get_single_color_func('deepskyblue')

# Generate a word cloud image
wordcloud = WordCloud(background_color="white", color_func=funColor)
wordcloud.generate_from_frequencies(ngramFreqList)


#fit_words
# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# lower max_font_size
# wordcloud = wordcloud.generate_from_frequencies(ngramFreqList, 40)
# plt.figure()
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()