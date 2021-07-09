import nltk, string
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
​
text = """Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as "algebraic objects". It gave mathematics a whole new development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a way which had not happened before."""
text = text.lower()
text_p = "".join([char for char in text if char not in string.punctuation])
words = nltk.word_tokenize(text_p)
stop_words = stopwords.words('english')
filtered_words = [word for word in words if word not in stop_words]
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in filtered_words]
pos = pos_tag(filtered_words)

for tree in pos:
           print(tree)
