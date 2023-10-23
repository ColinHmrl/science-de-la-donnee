# Training n°2023_10_05_08_22_07
    number of classes: 2
    model: resnet50
    model type: binary
    image size: 150x150
    batch size: 128
    ----------------------------
    ## Compile config
    {'optimizer': 'adam', 'loss': {'module': 'keras.losses', 'class_name': 'BinaryCrossentropy', 'config': {'reduction': 'auto', 'name': 'binary_crossentropy', 'from_logits': False, 'label_smoothing': 0.0, 'axis': -1, 'fn': 'binary_crossentropy'}, 'registered_name': None}, 'metrics': ['accuracy'], 'loss_weights': None, 'weighted_metrics': None, 'run_eagerly': None, 'steps_per_execution': None, 'jit_compile': None}
    ----------------------------
    ## Summary
    Model: "model"
__________________________________________________________________________________________________
 Layer (type)                Output Shape                 Param #   Connected to                  
==================================================================================================
 input_1 (InputLayer)        [(None, 150, 150, 3)]        0         []                            
                                                                                                  
 conv1_pad (ZeroPadding2D)   (None, 156, 156, 3)          0         ['input_1[0][0]']             
                                                                                                  
 conv1_conv (Conv2D)         (None, 75, 75, 64)           9472      ['conv1_pad[0][0]']           
                                                                                                  
 conv1_bn (BatchNormalizati  (None, 75, 75, 64)           256       ['conv1_conv[0][0]']          
 on)                                                                                              
                                                                                                  
 conv1_relu (Activation)     (None, 75, 75, 64)           0         ['conv1_bn[0][0]']            
                                                                                                  
 pool1_pad (ZeroPadding2D)   (None, 77, 77, 64)           0         ['conv1_relu[0][0]']          
                                                                                                  
 pool1_pool (MaxPooling2D)   (None, 38, 38, 64)           0         ['pool1_pad[0][0]']           
                                                                                                  
 conv2_block1_1_conv (Conv2  (None, 38, 38, 64)           4160      ['pool1_pool[0][0]']          
 D)                                                                                               
                                                                                                  
 conv2_block1_1_bn (BatchNo  (None, 38, 38, 64)           256       ['conv2_block1_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block1_1_relu (Activ  (None, 38, 38, 64)           0         ['conv2_block1_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv2_block1_2_conv (Conv2  (None, 38, 38, 64)           36928     ['conv2_block1_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv2_block1_2_bn (BatchNo  (None, 38, 38, 64)           256       ['conv2_block1_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block1_2_relu (Activ  (None, 38, 38, 64)           0         ['conv2_block1_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv2_block1_0_conv (Conv2  (None, 38, 38, 256)          16640     ['pool1_pool[0][0]']          
 D)                                                                                               
                                                                                                  
 conv2_block1_3_conv (Conv2  (None, 38, 38, 256)          16640     ['conv2_block1_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv2_block1_0_bn (BatchNo  (None, 38, 38, 256)          1024      ['conv2_block1_0_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block1_3_bn (BatchNo  (None, 38, 38, 256)          1024      ['conv2_block1_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block1_add (Add)      (None, 38, 38, 256)          0         ['conv2_block1_0_bn[0][0]',   
                                                                     'conv2_block1_3_bn[0][0]']   
                                                                                                  
 conv2_block1_out (Activati  (None, 38, 38, 256)          0         ['conv2_block1_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv2_block2_1_conv (Conv2  (None, 38, 38, 64)           16448     ['conv2_block1_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv2_block2_1_bn (BatchNo  (None, 38, 38, 64)           256       ['conv2_block2_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block2_1_relu (Activ  (None, 38, 38, 64)           0         ['conv2_block2_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv2_block2_2_conv (Conv2  (None, 38, 38, 64)           36928     ['conv2_block2_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv2_block2_2_bn (BatchNo  (None, 38, 38, 64)           256       ['conv2_block2_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block2_2_relu (Activ  (None, 38, 38, 64)           0         ['conv2_block2_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv2_block2_3_conv (Conv2  (None, 38, 38, 256)          16640     ['conv2_block2_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv2_block2_3_bn (BatchNo  (None, 38, 38, 256)          1024      ['conv2_block2_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block2_add (Add)      (None, 38, 38, 256)          0         ['conv2_block1_out[0][0]',    
                                                                     'conv2_block2_3_bn[0][0]']   
                                                                                                  
 conv2_block2_out (Activati  (None, 38, 38, 256)          0         ['conv2_block2_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv2_block3_1_conv (Conv2  (None, 38, 38, 64)           16448     ['conv2_block2_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv2_block3_1_bn (BatchNo  (None, 38, 38, 64)           256       ['conv2_block3_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block3_1_relu (Activ  (None, 38, 38, 64)           0         ['conv2_block3_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv2_block3_2_conv (Conv2  (None, 38, 38, 64)           36928     ['conv2_block3_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv2_block3_2_bn (BatchNo  (None, 38, 38, 64)           256       ['conv2_block3_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block3_2_relu (Activ  (None, 38, 38, 64)           0         ['conv2_block3_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv2_block3_3_conv (Conv2  (None, 38, 38, 256)          16640     ['conv2_block3_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv2_block3_3_bn (BatchNo  (None, 38, 38, 256)          1024      ['conv2_block3_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv2_block3_add (Add)      (None, 38, 38, 256)          0         ['conv2_block2_out[0][0]',    
                                                                     'conv2_block3_3_bn[0][0]']   
                                                                                                  
 conv2_block3_out (Activati  (None, 38, 38, 256)          0         ['conv2_block3_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv3_block1_1_conv (Conv2  (None, 19, 19, 128)          32896     ['conv2_block3_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv3_block1_1_bn (BatchNo  (None, 19, 19, 128)          512       ['conv3_block1_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block1_1_relu (Activ  (None, 19, 19, 128)          0         ['conv3_block1_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv3_block1_2_conv (Conv2  (None, 19, 19, 128)          147584    ['conv3_block1_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv3_block1_2_bn (BatchNo  (None, 19, 19, 128)          512       ['conv3_block1_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block1_2_relu (Activ  (None, 19, 19, 128)          0         ['conv3_block1_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv3_block1_0_conv (Conv2  (None, 19, 19, 512)          131584    ['conv2_block3_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv3_block1_3_conv (Conv2  (None, 19, 19, 512)          66048     ['conv3_block1_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv3_block1_0_bn (BatchNo  (None, 19, 19, 512)          2048      ['conv3_block1_0_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block1_3_bn (BatchNo  (None, 19, 19, 512)          2048      ['conv3_block1_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block1_add (Add)      (None, 19, 19, 512)          0         ['conv3_block1_0_bn[0][0]',   
                                                                     'conv3_block1_3_bn[0][0]']   
                                                                                                  
 conv3_block1_out (Activati  (None, 19, 19, 512)          0         ['conv3_block1_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv3_block2_1_conv (Conv2  (None, 19, 19, 128)          65664     ['conv3_block1_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv3_block2_1_bn (BatchNo  (None, 19, 19, 128)          512       ['conv3_block2_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block2_1_relu (Activ  (None, 19, 19, 128)          0         ['conv3_block2_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv3_block2_2_conv (Conv2  (None, 19, 19, 128)          147584    ['conv3_block2_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv3_block2_2_bn (BatchNo  (None, 19, 19, 128)          512       ['conv3_block2_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block2_2_relu (Activ  (None, 19, 19, 128)          0         ['conv3_block2_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv3_block2_3_conv (Conv2  (None, 19, 19, 512)          66048     ['conv3_block2_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv3_block2_3_bn (BatchNo  (None, 19, 19, 512)          2048      ['conv3_block2_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block2_add (Add)      (None, 19, 19, 512)          0         ['conv3_block1_out[0][0]',    
                                                                     'conv3_block2_3_bn[0][0]']   
                                                                                                  
 conv3_block2_out (Activati  (None, 19, 19, 512)          0         ['conv3_block2_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv3_block3_1_conv (Conv2  (None, 19, 19, 128)          65664     ['conv3_block2_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv3_block3_1_bn (BatchNo  (None, 19, 19, 128)          512       ['conv3_block3_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block3_1_relu (Activ  (None, 19, 19, 128)          0         ['conv3_block3_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv3_block3_2_conv (Conv2  (None, 19, 19, 128)          147584    ['conv3_block3_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv3_block3_2_bn (BatchNo  (None, 19, 19, 128)          512       ['conv3_block3_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block3_2_relu (Activ  (None, 19, 19, 128)          0         ['conv3_block3_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv3_block3_3_conv (Conv2  (None, 19, 19, 512)          66048     ['conv3_block3_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv3_block3_3_bn (BatchNo  (None, 19, 19, 512)          2048      ['conv3_block3_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block3_add (Add)      (None, 19, 19, 512)          0         ['conv3_block2_out[0][0]',    
                                                                     'conv3_block3_3_bn[0][0]']   
                                                                                                  
 conv3_block3_out (Activati  (None, 19, 19, 512)          0         ['conv3_block3_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv3_block4_1_conv (Conv2  (None, 19, 19, 128)          65664     ['conv3_block3_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv3_block4_1_bn (BatchNo  (None, 19, 19, 128)          512       ['conv3_block4_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block4_1_relu (Activ  (None, 19, 19, 128)          0         ['conv3_block4_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv3_block4_2_conv (Conv2  (None, 19, 19, 128)          147584    ['conv3_block4_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv3_block4_2_bn (BatchNo  (None, 19, 19, 128)          512       ['conv3_block4_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block4_2_relu (Activ  (None, 19, 19, 128)          0         ['conv3_block4_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv3_block4_3_conv (Conv2  (None, 19, 19, 512)          66048     ['conv3_block4_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv3_block4_3_bn (BatchNo  (None, 19, 19, 512)          2048      ['conv3_block4_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv3_block4_add (Add)      (None, 19, 19, 512)          0         ['conv3_block3_out[0][0]',    
                                                                     'conv3_block4_3_bn[0][0]']   
                                                                                                  
 conv3_block4_out (Activati  (None, 19, 19, 512)          0         ['conv3_block4_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv4_block1_1_conv (Conv2  (None, 10, 10, 256)          131328    ['conv3_block4_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv4_block1_1_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block1_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block1_1_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block1_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block1_2_conv (Conv2  (None, 10, 10, 256)          590080    ['conv4_block1_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block1_2_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block1_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block1_2_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block1_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block1_0_conv (Conv2  (None, 10, 10, 1024)         525312    ['conv3_block4_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv4_block1_3_conv (Conv2  (None, 10, 10, 1024)         263168    ['conv4_block1_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block1_0_bn (BatchNo  (None, 10, 10, 1024)         4096      ['conv4_block1_0_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block1_3_bn (BatchNo  (None, 10, 10, 1024)         4096      ['conv4_block1_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block1_add (Add)      (None, 10, 10, 1024)         0         ['conv4_block1_0_bn[0][0]',   
                                                                     'conv4_block1_3_bn[0][0]']   
                                                                                                  
 conv4_block1_out (Activati  (None, 10, 10, 1024)         0         ['conv4_block1_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv4_block2_1_conv (Conv2  (None, 10, 10, 256)          262400    ['conv4_block1_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv4_block2_1_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block2_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block2_1_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block2_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block2_2_conv (Conv2  (None, 10, 10, 256)          590080    ['conv4_block2_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block2_2_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block2_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block2_2_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block2_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block2_3_conv (Conv2  (None, 10, 10, 1024)         263168    ['conv4_block2_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block2_3_bn (BatchNo  (None, 10, 10, 1024)         4096      ['conv4_block2_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block2_add (Add)      (None, 10, 10, 1024)         0         ['conv4_block1_out[0][0]',    
                                                                     'conv4_block2_3_bn[0][0]']   
                                                                                                  
 conv4_block2_out (Activati  (None, 10, 10, 1024)         0         ['conv4_block2_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv4_block3_1_conv (Conv2  (None, 10, 10, 256)          262400    ['conv4_block2_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv4_block3_1_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block3_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block3_1_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block3_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block3_2_conv (Conv2  (None, 10, 10, 256)          590080    ['conv4_block3_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block3_2_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block3_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block3_2_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block3_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block3_3_conv (Conv2  (None, 10, 10, 1024)         263168    ['conv4_block3_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block3_3_bn (BatchNo  (None, 10, 10, 1024)         4096      ['conv4_block3_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block3_add (Add)      (None, 10, 10, 1024)         0         ['conv4_block2_out[0][0]',    
                                                                     'conv4_block3_3_bn[0][0]']   
                                                                                                  
 conv4_block3_out (Activati  (None, 10, 10, 1024)         0         ['conv4_block3_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv4_block4_1_conv (Conv2  (None, 10, 10, 256)          262400    ['conv4_block3_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv4_block4_1_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block4_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block4_1_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block4_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block4_2_conv (Conv2  (None, 10, 10, 256)          590080    ['conv4_block4_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block4_2_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block4_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block4_2_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block4_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block4_3_conv (Conv2  (None, 10, 10, 1024)         263168    ['conv4_block4_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block4_3_bn (BatchNo  (None, 10, 10, 1024)         4096      ['conv4_block4_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block4_add (Add)      (None, 10, 10, 1024)         0         ['conv4_block3_out[0][0]',    
                                                                     'conv4_block4_3_bn[0][0]']   
                                                                                                  
 conv4_block4_out (Activati  (None, 10, 10, 1024)         0         ['conv4_block4_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv4_block5_1_conv (Conv2  (None, 10, 10, 256)          262400    ['conv4_block4_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv4_block5_1_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block5_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block5_1_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block5_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block5_2_conv (Conv2  (None, 10, 10, 256)          590080    ['conv4_block5_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block5_2_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block5_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block5_2_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block5_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block5_3_conv (Conv2  (None, 10, 10, 1024)         263168    ['conv4_block5_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block5_3_bn (BatchNo  (None, 10, 10, 1024)         4096      ['conv4_block5_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block5_add (Add)      (None, 10, 10, 1024)         0         ['conv4_block4_out[0][0]',    
                                                                     'conv4_block5_3_bn[0][0]']   
                                                                                                  
 conv4_block5_out (Activati  (None, 10, 10, 1024)         0         ['conv4_block5_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv4_block6_1_conv (Conv2  (None, 10, 10, 256)          262400    ['conv4_block5_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv4_block6_1_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block6_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block6_1_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block6_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block6_2_conv (Conv2  (None, 10, 10, 256)          590080    ['conv4_block6_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block6_2_bn (BatchNo  (None, 10, 10, 256)          1024      ['conv4_block6_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block6_2_relu (Activ  (None, 10, 10, 256)          0         ['conv4_block6_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv4_block6_3_conv (Conv2  (None, 10, 10, 1024)         263168    ['conv4_block6_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv4_block6_3_bn (BatchNo  (None, 10, 10, 1024)         4096      ['conv4_block6_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv4_block6_add (Add)      (None, 10, 10, 1024)         0         ['conv4_block5_out[0][0]',    
                                                                     'conv4_block6_3_bn[0][0]']   
                                                                                                  
 conv4_block6_out (Activati  (None, 10, 10, 1024)         0         ['conv4_block6_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv5_block1_1_conv (Conv2  (None, 5, 5, 512)            524800    ['conv4_block6_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv5_block1_1_bn (BatchNo  (None, 5, 5, 512)            2048      ['conv5_block1_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block1_1_relu (Activ  (None, 5, 5, 512)            0         ['conv5_block1_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv5_block1_2_conv (Conv2  (None, 5, 5, 512)            2359808   ['conv5_block1_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv5_block1_2_bn (BatchNo  (None, 5, 5, 512)            2048      ['conv5_block1_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block1_2_relu (Activ  (None, 5, 5, 512)            0         ['conv5_block1_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv5_block1_0_conv (Conv2  (None, 5, 5, 2048)           2099200   ['conv4_block6_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv5_block1_3_conv (Conv2  (None, 5, 5, 2048)           1050624   ['conv5_block1_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv5_block1_0_bn (BatchNo  (None, 5, 5, 2048)           8192      ['conv5_block1_0_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block1_3_bn (BatchNo  (None, 5, 5, 2048)           8192      ['conv5_block1_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block1_add (Add)      (None, 5, 5, 2048)           0         ['conv5_block1_0_bn[0][0]',   
                                                                     'conv5_block1_3_bn[0][0]']   
                                                                                                  
 conv5_block1_out (Activati  (None, 5, 5, 2048)           0         ['conv5_block1_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv5_block2_1_conv (Conv2  (None, 5, 5, 512)            1049088   ['conv5_block1_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv5_block2_1_bn (BatchNo  (None, 5, 5, 512)            2048      ['conv5_block2_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block2_1_relu (Activ  (None, 5, 5, 512)            0         ['conv5_block2_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv5_block2_2_conv (Conv2  (None, 5, 5, 512)            2359808   ['conv5_block2_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv5_block2_2_bn (BatchNo  (None, 5, 5, 512)            2048      ['conv5_block2_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block2_2_relu (Activ  (None, 5, 5, 512)            0         ['conv5_block2_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv5_block2_3_conv (Conv2  (None, 5, 5, 2048)           1050624   ['conv5_block2_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv5_block2_3_bn (BatchNo  (None, 5, 5, 2048)           8192      ['conv5_block2_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block2_add (Add)      (None, 5, 5, 2048)           0         ['conv5_block1_out[0][0]',    
                                                                     'conv5_block2_3_bn[0][0]']   
                                                                                                  
 conv5_block2_out (Activati  (None, 5, 5, 2048)           0         ['conv5_block2_add[0][0]']    
 on)                                                                                              
                                                                                                  
 conv5_block3_1_conv (Conv2  (None, 5, 5, 512)            1049088   ['conv5_block2_out[0][0]']    
 D)                                                                                               
                                                                                                  
 conv5_block3_1_bn (BatchNo  (None, 5, 5, 512)            2048      ['conv5_block3_1_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block3_1_relu (Activ  (None, 5, 5, 512)            0         ['conv5_block3_1_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv5_block3_2_conv (Conv2  (None, 5, 5, 512)            2359808   ['conv5_block3_1_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv5_block3_2_bn (BatchNo  (None, 5, 5, 512)            2048      ['conv5_block3_2_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block3_2_relu (Activ  (None, 5, 5, 512)            0         ['conv5_block3_2_bn[0][0]']   
 ation)                                                                                           
                                                                                                  
 conv5_block3_3_conv (Conv2  (None, 5, 5, 2048)           1050624   ['conv5_block3_2_relu[0][0]'] 
 D)                                                                                               
                                                                                                  
 conv5_block3_3_bn (BatchNo  (None, 5, 5, 2048)           8192      ['conv5_block3_3_conv[0][0]'] 
 rmalization)                                                                                     
                                                                                                  
 conv5_block3_add (Add)      (None, 5, 5, 2048)           0         ['conv5_block2_out[0][0]',    
                                                                     'conv5_block3_3_bn[0][0]']   
                                                                                                  
 conv5_block3_out (Activati  (None, 5, 5, 2048)           0         ['conv5_block3_add[0][0]']    
 on)                                                                                              
                                                                                                  
 flatten (Flatten)           (None, 51200)                0         ['conv5_block3_out[0][0]']    
                                                                                                  
 dense (Dense)               (None, 512)                  2621491   ['flatten[0][0]']             
                                                          2                                       
                                                                                                  
 dropout (Dropout)           (None, 512)                  0         ['dense[0][0]']               
                                                                                                  
 dense_1 (Dense)             (None, 1)                    513       ['dropout[0][0]']             
                                                                                                  
==================================================================================================
Total params: 49803137 (189.98 MB)
Trainable params: 26215425 (100.00 MB)
Non-trainable params: 23587712 (89.98 MB)
__________________________________________________________________________________________________
