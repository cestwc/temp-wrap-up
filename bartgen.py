import torch
import torch.nn as nn
from transformers import BartTokenizer, BartForConditionalGeneration

def loadmodel(modelDir, device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')):
	tokenizer = BartTokenizer.from_pretrained('facebook/bart-base')
	model = BartForConditionalGeneration.from_pretrained('facebook/bart-base')
	model.load_state_dict(torch.load(modelDir, map_location=device))
	model.to(device)
	return model

def bartGenerate(sentence, model, device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')):    
	inputs = tokenizer([sentence], max_length=1024, return_tensors='pt').to(device)

	# Generate Summary
	summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=1024, early_stopping=True)
	return [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in summary_ids][0], inputs['input_ids'].shape[1], summary_ids.shape[1]
