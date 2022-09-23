This web app was built using __React JS__.  
The folder structure is emulated from [Create React App](https://github.com/facebook/create-react-app).
<br>
<br>
All the code required to succesfully run the web app is provided in this folder.  
However, there is a caveat; There are packages and dependencies that must be installed to run the web app.  
These packages are contained in the [package.json](https://github.com/ifunanyaScript/Brain-tumour-diagnosis-app/blob/main/client/package.json) and [package-lock.json](https://github.com/ifunanyaScript/Brain-tumour-diagnosis-app/blob/main/client/package-lock.json) files.  

###### Install Node JS
Search "Installing Node JS on _name of your machine, e.g Windows 10_" on google.  
Follow the resulting page intuitively.  
__NB:___ If you install Node JS using the package installer, it comes directly with npm.
###### Install npm
Search "Installing npm on _name of your machine, e.g Windows 10_" on google.  
Follow the resulting page intuitively.  

###### `npm install --from-lock.json`
After you have installed Node JS and npm, run Mac Terminal or Windows Command Prompt.  
Change your present working directory to the client folder, then run `npm install --from-lock.json`. 

###### `npm audit fix`
After all the packages and dependencies have been installed, run `npm audit fix` to fix all vulnerabilities.

###### `npm start`
After vulnerabilities have been fixed, run `npm start`.  
The web app will be hosted on localhost:3000 on your machine.  
<br>
<br>
<br>
<br>
__NB:__ Start the backend main_server provided [here](https://github.com/ifunanyaScript/Brain-tumour-diagnosis-app/blob/main/server/main_server.py) to get diagnosis results.

