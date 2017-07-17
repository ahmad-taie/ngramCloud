import sys
from wordcloud import WordCloud

if len(sys.argv) > 1:
    gramsFile = sys.argv[1]
else:
    gramsFile = "testgrams.txt"


ngramsList = []
freqList = []
surpList = []

with open(gramsFile) as attributes:
    # Parse the  file
    for line in attributes:
        line = line.split()
        surpList.append(float(line[-1]))
        freqList.append(int(line[-2]))
        ngramsList.append(" ".join(line[:-2]))

print(ngramsList)
print(freqList)
print(surpList)


# Generate a word cloud image
wordcloud = WordCloud().generate(" ".join(ngramsList))

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(" ".join(ngramsList))
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()