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
        self.config=config
        self.tokenizer=tokenizer
        self.args=args
    
        
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

        prob=torch.sigmoid(logits)
        text_prob=torch.sigmoid(text_outputs)
        left_prob=torch.sigmoid(left_outputs)
        if labels is not None:
            labels=labels.float()
            loss=torch.log(prob[:,0]+1e-10)*labels+torch.log((1-prob)[:,0]+1e-10)*(1-labels)
            text_loss=torch.log(text_prob[:,0]+1e-10)*labels+torch.log((1-text_prob)[:,0]+1e-10)*(1-labels)
            left_loss=torch.log(left_prob[:,0]+1e-10)*labels+torch.log((1-left_prob)[:,0]+1e-10)*(1-labels)
            loss=-loss.mean()
            text_loss=-text_loss.mean()
            left_loss=-left_loss.mean()
            return loss+text_loss+left_loss,prob
        else:
            return prob
      
        
 
