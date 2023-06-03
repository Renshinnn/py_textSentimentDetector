from textblob import TextBlob

teks = input("Masukkan teks: ")
sentimen = TextBlob(teks).sentiment.polarity

if sentimen > 0:
    print("Sentimen positif")
elif sentimen < 0:
    print("Sentimen negatif")
else:
    print("Sentimen netral")
