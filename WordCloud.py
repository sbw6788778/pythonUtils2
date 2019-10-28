from wordcloud import WordCloud
import matplotlib.pyplot as plt
f = open(u'test.txt','r').read()

wordcloud = WordCloud(font_path='C:/Windows/Fonts/MSYH.TTC',background_color="white",width=1000, height=860, margin=2).generate(f)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file('test.png')


