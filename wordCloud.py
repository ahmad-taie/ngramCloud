import sys
from wordcloud import WordCloud
import wordcloud

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

# lower max_font_size
wordcloud = wordcloud.generate_from_frequencies(ngramFreqList, 40)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()