from gensim.summarization import summarize
from gensim.summarization import keywords
import pandas as pd 


if __name__ == "__main__":
	df = pd.read_csv('newtestament.txt', delimiter="|", skiprows=0, names=['Book', 'Chapter', 'Verse', 'Original Text'])
	text = df[df['Book'] == 'Mat']['Original Text'].values

	alltext = ''
	for verse in text:
	    alltext += verse

	print summarize(alltext, ratio = 0.005)
	print keywords(text, ratio = 0.01)

