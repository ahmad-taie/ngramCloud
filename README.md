# ngramCloud

This simple script extends word_cloud to provide 2 parameters for generating the word cloud: word size and  word color.ngram

# Input file format

The input file is a text file with one word for the word cloud per line.
An input line is in the format:  word(s) x y
Where the word(s) is the required characters for the word cloud, x is the color variation parameter, and y is the size parameter.

An example input file is provided.

# Running the script and params

To run the script, provide the parameters:

 fileName, color1, color
 
fileName is the text file containing the inputs to the word cloud.
color1 and color2 are the supported color names from The PIL ImageColor Module. (Optional, default: red , yellow)

# Notes

The original context was to have the variation of color based on word surpirsal, and the size based on frequency, hence the names in the code.

Feel free to experiment with get_colorFunc to modify how the colors vary with the values.
