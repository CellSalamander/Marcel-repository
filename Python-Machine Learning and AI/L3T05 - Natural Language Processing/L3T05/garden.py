import spacy
from spacy import displacy

gardenpathsentences = ["The old man the boat","The horse raced past the barn fell","Mary gave the child a band-aid","That Jill is never here hurts","The cotton clothing is made of grows in missisippi"]

nlp = spacy.load("en_core_web_sm")

for sentence in gardenpathsentences:
    
    doc = nlp(sentence)
    print([(w.text,w.pos_) for w in doc])


print(spacy.explain("DET"))
print(spacy.explain("ADP"))

# Entity: "The" is DET
# Explenation : determiner
# Yes , because the word "The" is a determiner , in the sentence "The old man the boat" , the first "The" makes sense , because we are specifying which old man but the second "the" doesn't make sense in the sentence.

# Entity: "of" is ADP
# Explenation : adposition
# Yes , because the word "of" is an adposition , in the sentence "The cotton clothing is made of grows in missisippi" the "of" makes sense , because it expresses a relationship to the cotten clothing.
        
        