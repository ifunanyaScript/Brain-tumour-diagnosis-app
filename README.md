# Brain-tumour-diagnosis-app

### The Data
The dataset consist of 3000 images of Brain MRI scans; 1500 images each for tumour and no-tumour.  
Due to Github's 1000 files policy, I did not upload the entire dataset in this repository. However if you wish to procure the dataset you can find it [here](https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection)


### Model building
A norm when training machine learning models is to train several versions of the model for quality and testing purposes.  
For this purpose, I trained three CNNs for brain tumour classification.<br>
The first model was built as a binary classification. The output layer has one neuron activated by a sigmoid function. I stacked 6 concolution layers, one fully connected dense layer and a final output layer. The model achieved 97.70% testing accuracy.<br>
The second model was built as a multiclass classification. The output layer has 2 neurons activated by a softmax function. I stacked 6 concolution layers, two fully connected dense layer and a final output layer. The model achieved 98.50% testing accuracy.<br> 
The third CNN was modelled employing __transfer learning__. I employed the __VGG16__ pretrained model weights and designed a new model as a multiclass classification. This model achieved 99% testing accuracy.<br>  
The notebooks for training these models are available [here](https://github.com/ifunanyaScript/Brain-tumour-diagnosis-app/tree/main/notebooks). The trained models were saved and exported and are available [here](https://github.com/ifunanyaScript/Brain-tumour-diagnosis-app/tree/main/saved_models).


### React JS web app
A react web app for brain tumour diagnosis was developed using these pretrained models.  
The web is a drag and drop architecture: One can drag and drop and image of a Brain MRI scan, and readily get a diagnosis result, i.e tumour classification and classification probabilty.<br>. 
![brain3](https://user-images.githubusercontent.com/91638505/196010443-b3be66f9-dc87-4bb3-acc0-685cbc3ff77e.png)

The entire source code used to develop this React web app is available [here](https://github.com/ifunanyaScript/Brain-tumour-diagnosis-app/tree/main/client).


### React Native mobile app
A fully functional react native app for brain tumour diagnosis.
This mobile app is a step up of the web app. It also adopts a similar architecture with a caveat: 
Using the mobile phone's camera, one can take a picture of a brain MRI scan and readily get a diagnosis result. Alternatively, one can select a picture of a brain MRI from the phone's file manager and also get a diagnosis result.<br>  
The source codes used to develop this React Native mobile app is available [here]().<br>  
<br>

Feel free to fork this repo and drop a ⭐star on your way out. Thanks! 😀.
