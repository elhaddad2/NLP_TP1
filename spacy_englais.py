import spacy
from spacy.lang.en import English


nlp = spacy.load('en_core_web_sm')


text = """Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as "algebraic objects". It gave mathematics a whole new development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a way which had not happened before."""



doc = nlp(text)

token_list = []
for token in doc:
           token_list.append(token.text)
print (token_list)

lemmas = [[token.text,token.lemma_] for token in doc]
print(lemmas)

spacy_stopwords = STOP_WORDS
print(spacy_stopwords)

filtered_sent=[]

for word in doc:
           if word.is_stop==False and word.text.isalpha()==True:
                      filtered_sent.append(word)
print(filtered_sent)

post_tag=[]

for post in doc:
           post_tag.append([post.text,post.pos_])
print (post_tag)
