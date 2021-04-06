#PyParagraph:
#Import a text file filled with a paragraph of your choosing.

#Assess the passage for each of the following:
	#Approximate word count
	#Approximate sentence count
	#Approximate letter count (per word)
	#Average sentence length (in words)


f = open("raw_data\paragraph_1.txt")
data = f.read()
print(f.read())

words=[]
#count of words
words=data.split()

word_count = len(data.split())

# count of characters
character_count = len(data)
#print(character_count)

special_character_count=data.count(" ")+data.count(".")\
+data.count(",")+data.count("(")+data.count(")")+data.count("-")
#print(special_character_count)

ave_word_length = round(((character_count-special_character_count)/word_count),1)
#print(ave_word_length)


#count of sentences
sentence_count=data.count('.')
ave_sentence_length = word_count/sentence_count
#print(ave_sentence_length)

#Terminal printout:
print("Paragraph Analysis")
print("-------------------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {ave_word_length}")
print(f"Average Sentence Length: {ave_sentence_length}")


