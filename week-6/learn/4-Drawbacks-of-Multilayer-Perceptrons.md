# Drawbacks of MultiLayer Perceptrons (MLP)

One of the main disadvantages of MultiLayer Perceptrons is that the number of parameters to be learned could be exceedingly large. 
With each parameter being fed forward into each neuron of the next layer the number of parameters grows quadratically. 
This means the computation of these parameters can be extremely innefficient once the parameter count grows large enough, due to the necessity for extensive training of these types of systems. 

## More Drawbacks 

Another drawback of multilayer perceptrons is their inherent sensitivity to input varitions. This can even be small input variations. 
There is a diagram on this slde which demonstrates this by shifing the letter A by two units causes a large amount of input nodes to light up and vice vera if the opposite is performed. (See diagram for clear example)

A 154-input change from two shifts left results in 77 pixels changing from black to white and 77 pixels from white to black. 

Other forms or pertubation such as rotation, scaling, writing style and digitization can change the input considerably, even though they do not alter the perceived meaning of the written letter, in this circumstance A.
To recognize this an MLP would be need to be trained in all forms of these perbutations which feeds back into the issue of computational intensity required to train an MLP on these kinds of classification tasks.   
