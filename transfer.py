import json

def fromSentenceCompression(directory, destiny = 'transfer.json'):
	with open(directory, 'r') as f:
		compData = json.loads('[' + f.read().replace('}\n\n{', '},\n{') + ']')

	pairs = [{'long':compData[i]['graph']['sentence'], 'short':compData[i]['compression']['text']} for i in range(len(compData))]
	data = [json.dumps(x) + '\n' for x in pairs]
	with open(destiny, 'w') as f:
		f.writelines(data)
	return destiny
