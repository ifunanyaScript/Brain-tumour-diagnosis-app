# Brain-tumour-diagnosis-app

#### The Data
The dataset consist of 3000 images of Brain MRI scans; 1500 images each for tumour and no-tumour.  
Due to Github's 1000 files policy, I did not upload the entire dataset in this repository. However if you wish to procure the dataset you can find it [here](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection)


#### Model building
It's a normal custom when buillding CNN models, to build and train several versions for quality and testing purposes. In this case I created two versions of the model.<br>
The first model was built as a binary classification. The output layer has one neuron activated by a sigmoid function. I stacked 6 concolution layers, one fully connected dense layer and a final output layer. The model achieved a 97.70% testing accuracy.<br>
The second model was built as a multiclass classification. The output layer has 2 neurons activated by a softmax function. I stacked 6 concolution layers, two fully connected dense layer and a final output layer. The model achieved a 98.50% testing accuracy.<br> 

Web app building in progress....
Using react js to build somthing beautiful
