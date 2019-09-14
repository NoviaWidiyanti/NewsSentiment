import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from Skripsi_Test import konten

import matplotlib.pyplot as plt

def vis_wordcloud(kalimat):

    comment_words = ' '
    stopwords = set(STOPWORDS) 

    # iterate through the csv file 
    for val in kata.itertuples(index = False): 
        variabel1 = val[0]
        variabel2 = val[1]
        # variabel1 = variabel1.to_string()
        # variabel2 = variabel2.to_string()

        kalimat = variabel1 + variabel2
        print(kalimat)
          
        # typecaste each val to string 
        val = str(kalimat) 
      
        # split the value 
        tokens = val.split() 
          
        # Converts each token into lowercase 
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower() 
              
        for words in tokens: 
            comment_words = comment_words + words + ' '
      
      
            wordcloud = WordCloud(width = 800, height = 800, 
                            background_color ='white', 
                            stopwords = stopwords, 
                            min_font_size = 10).generate(comment_words) 
              
            # plot the WordCloud image                        
            plt.figure(figsize = (8, 8), facecolor = None) 
            plt.imshow(wordcloud) 
            plt.axis("off") 
            plt.tight_layout(pad = 0) 
              
            

    return (plt.show()) 