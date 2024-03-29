# -*- coding: utf-8 -*-
"""DataMining_Business-Understanding.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dwIX73g0JSgY8vkkFtefBNfYD7tGA4bw
"""



"""#Anime Ratings Analysis & Recommender System

##Tujuan Bisnis
Tujuan proyek ini adalah untuk menganalisis data rating anime dan mengembangkan sistem rekomendasi   untuk memberikan rekomendasi yang baik untuk  pengguna berdasarkan kesukaan mereka. Dengan demikian, diharapkan dapat meningkatkan pengalaman pengguna dalam menemukan anime yang sesuai dengan selera mereka.
##Assess Situation
Situasi bisnis yang mendasari proyek ini adalah:


1.   Kebutuhan akan sistem yang dapat membantu memberikan rekomendasi yang sesuai dengan selera mereka
2.   Meningkatkan interaksi pengguna dengan platform anime.
3. Kurangnya pemahaman selera unik setiap pengguna, maka terdapat keaadan yang dimana rekomendasinya kurang tepat


##Data Mining Goals
Tujuan dari analisis data pada dataset ini adalah :


1. Mengembangkan sistem rekomendasi yang dapat memberikan rekomendasi anime yang sesuai dengan selera pengguna.
2.   Memprediksi rating anime berdasarkan faktor-faktor tertentu
3. mengidentifikasi tren dan pola dalam data rating

##Projek Plan
Pertama-tama dimulai dengan pengumpulan data rating anime dari sumber yang tersedia. Selanjutnya, data akan dijelaskan karakteristiknya dan pola-pola yang menarik untuk di itentifikasi. kemudian mendeskripsikan data yang akan di identifikasi seperti contoh "ID anime, nama, genre, jenis, episode, rating", lalu menilai kualitas data dan masalah data yang akan diidentifikasi.
"""

import pandas as pd

df = pd.read_csv("anime.csv")

df.head()