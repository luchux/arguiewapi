def pos_tag(text_list):
	return [(word,word) for word in text_list]

def word_tokenize(text):
	return text.split()

#TODO: from nltk import pos_tag, word_tokenize
#TOD: add our classifier for sentiment, words, etc. this is so naive.
standard_features = {'clean':'clean',
					'dirty':'clean',
					 'comfort':'comfort',
					 'location':'location',
					 'connection':'location',
					 'metro':'location',
					 'bus':'location',
					 'transport':'location',
					 'metro':'location',
					 'services':'services',
					 'service':'services',
					 'internet':'services',
					 'facilities':'services',
					 'facility':'services',
					 'minibar':'services', 
					 'breakfast':'services',
					 'wifi':'services',
					 'wi-fi':'services',
					 'breakfast':'services',
					 'staff':'staff',
					 'employess':'staff',
					 'price':'price',
					 'prices':'price',
					 'cost':'cost',
					 'see':'view',
					 'view':'view', 
					 'sight':'view',
					 'look':'view',
					 'barman':'staff',
					 'lady':'staff',
					 'furniture':'ambience',
					 'ambience':'ambience',
					 'room':'comfort',
					 'rooms':'comfort',
					 'bed':'comfort',
					 'noisy':'comfort',
					 'silent':'comfort',
					 'check':'staff'
					}

def filter_tags(lista,tags):
	return [(word,tag) for word,tag in lista if tag in tags]

def extract_features(lista):
	features =  [(standard_features[word.lower()],tag) for word,tag in lista if word.lower() in standard_features]
	feats_words = [word for word,tag in features]
	return list(set(feats_words))
	
def analize_text(text):
	postag = pos_tag(word_tokenize(text))
	feats = extract_features(postag)
	return feats