def word_count(text):
	string=text.split()
	return len(string)

def character_count(text):
	dict={}
	string=text
	for i in string:
		j=i.lower()
		if j in dict:
			dict[j]=dict[j]+1
		else:
			dict.update({j:1})
	return dict

def sort_on(items):
	return items["num"]

def dictionary_sort(dictionary):
	d=[]
	for i in dictionary:
		d.append({"char":i,"num":dictionary[i]})
	d.sort(reverse=True,key=sort_on)
	return d

