import spacy
from spacy.lang.ar import Arabic


nlp = Arabic()


text = u'ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و المقادير الهندسية و غيرها، أن تتعامل على أنها أجسام جبرية، و أعطت الرياضيات ككل مسارا جديدا للتطور بمفهوم أوسع بكثير من الذي كان موجودا من قبل، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل'



doc = nlp(text)

token_list = []
for w in doc:
           token_list.append(w.text)
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
