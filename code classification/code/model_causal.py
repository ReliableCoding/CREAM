# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
import torch
import torch.nn as nn
import torch
from torch.autograd import Variable
import copy
from torch.nn import CrossEntropyLoss, MSELoss

    
    
class Model(nn.Module):   
    def __init__(self, encoder,text_encoder,left_encoder,config,tokenizer,args):
        super(Model, self).__init__()
        self.encoder = encoder
        self.text_encoder = text_encoder
        self.left_encoder = left_encoder
        self.config=config
        self.tokenizer=tokenizer
        self.args=args
        self.num_labels = 104
        self.loss_fct = CrossEntropyLoss()
    
        
    def forward(self, input_ids=None,labels=None,text_inputs=None,left_inputs=None,current_epoch=None): 
        outputs=self.encoder(input_ids,attention_mask=input_ids.ne(1))[0]
        text_outputs=self.encoder(text_inputs,attention_mask=text_inputs.ne(1))[0]
        left_outputs=self.encoder(left_inputs,attention_mask=left_inputs.ne(1))[0]
        if current_epoch is not None:
            if current_epoch == -1:
                logits = outputs+1*text_outputs+1*left_outputs- self.args.alpha*text_outputs
            elif current_epoch>=0 and current_epoch<=int(self.args.epoch*self.args.fusion):
                logits = outputs
            else:
                logits = (outputs+1*text_outputs+1*left_outputs)/3
        else:
            logits = outputs

        if labels is not None:
            loss = self.loss_fct(logits.view(-1, self.num_labels), labels.view(-1))
            text_loss = self.loss_fct(text_outputs.view(-1, self.num_labels), labels.view(-1))
            left_loss = self.loss_fct(left_outputs.view(-1, self.num_labels), labels.view(-1))
            return loss+text_loss+left_loss,logits
        else:
            return logits
      
        
 
