import codecs

with codecs.open('pali_data.txt', 'r', encoding='utf8') as f:

	data = f.read().split()

	fifth = len(data)/5 + 1

	start = 0
	end = fifth

	for letter in 'abcde':


		with codecs.open(letter,'w',encoding='utf8') as part:
			part.write(' '.join(data[start:fifth]))

			print start
			print end

		start = end
		end = end + fifth
