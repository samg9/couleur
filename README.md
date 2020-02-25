# Couleur API 
- Scrapes public instagram profiles for posts(images), generates color palettes for each post, returns hex values and image source 
- Backend for https://github.com/samg9/couleur_frontend/ (live at https://couleur.herokuapp.com/)
### Example request and response 
GET request from the command line:
```
curl -i https://couleur-be.herokuapp.com/api/palettes?user="plum"&pal_size="8"
```
Response: 
```
{"result":[{"hexes":["#193e75","#2a7dbc","#023d79","#111c3d","#175a98","#041839","#010d23","#01224e"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/85175189_208149403666326_2378185589647977750_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=106&_nc_ohc=HeX_urgOi68AX_jWQQi&oh=be565f2bc667da9749a42158efeca966&oe=5E81B559"},{"hexes":["#597dbf","#c39ab5","#845a52","#f495ad","#ab8ebd","#42484c","#eda7b0","#cd81ab"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/87338227_1413841528777495_2359507853452161634_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=107&_nc_ohc=x7Vi0yDyMWoAX-aYg1Z&oh=7fcfc9d93853b3fe57091b11d5422439&oe=5E89A631"},{"hexes":["#7a3f75","#b57ec0","#7378ba","#4674ad","#ac73c8","#1a0d28","#090b27","#09020c"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/84469624_1911320349000051_3675963258838501105_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=103&_nc_ohc=KiUIi5mnvG4AX9EWIHQ&oh=05778959e1b9b13729e2178fc4db6fd0&oe=5E880451"},{"hexes":["#251a43","#55317b","#272f78","#ce6c7b","#0e0a25","#45225c","#50419d","#08215c"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/84632466_2676142479168801_155963818699721266_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=sSg1fQg5ehsAX9PXzvp&oh=f10060bdd2043574c1b2e185e219838c&oe=5E853158"},{"hexes":["#795f65","#3c3a40","#281a21","#e72b56","#cf8382","#ed4264","#fb6172","#e3a19e"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/83097065_2697529113697655_8184432991780215203_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=111&_nc_ohc=wilVD-zb0-oAX-ZgM9W&oh=279ddea8a6ed25d1c5682a39cd29b390&oe=5E819C7D"},{"hexes":["#d874b1","#5b315b","#32304a","#221024","#794e83","#e08aa4","#5e87e1","#9084da"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/82672794_212506933138214_1668858630413342606_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=102&_nc_ohc=WyGTJhv8Q9AAX-8Hg_c&oh=2c980ed137351dd3d3e36296524e8344&oe=5E8A62D3"},{"hexes":["#c37ebf","#c1bdb5","#c65aa4","#415391","#2c103b","#352e6b","#67265f","#b0236f"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/84356664_2279088255725558_1459938266392369140_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=102&_nc_ohc=lgGduUGX8YEAX_ldd5Q&oh=b31c590dceb8039f58027c44ed844085&oe=5E85A9C7"},{"hexes":["#f979b6","#eb6fbe","#1f0f38","#d56ec6","#a568c9","#2b285e","#63276d","#5c469e"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/83191352_605994729969149_579870818525328984_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=105&_nc_ohc=sdHzkyTl7gEAX9URRkR&oh=8f74b5150ffaf289fe8f24b1543ad64f&oe=5E7FF423"},{"hexes":["#fb97a3","#8457a9","#ff96a6","#0c156d","#fbb49d","#f4d4aa","#000c62","#ff809b"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/s1080x1080/81715078_580434212512929_4953313026011501362_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=109&_nc_ohc=TTi11kkEbPgAX-SEl7s&oh=6734797b5dbac7e55f19478f08edca80&oe=5E830B9B"},{"hexes":["#643d74","#211845","#171235","#ce6e8f","#482a58","#0c0919","#382759","#37204a"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/82824721_174521130316889_2663620137761752031_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=105&_nc_ohc=quneCBoXWdcAX-sNjX7&oh=bd1dbf93a3a9f42d7b4df65245f49a08&oe=5E83529A"},{"hexes":["#eb783c","#893420","#ff913f","#ffaf52","#2c2f25","#faac62","#626757","#c1a379"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/80625580_2780063102050795_7801652361009939931_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=107&_nc_ohc=WN95V7YkgWAAX-11Dzr&oh=308b19464d356f8ecbf004ba9037af6d&oe=5E83BB83"},{"hexes":["#fa9e91","#9493a7","#328fac","#756e8b","#1e2b4a","#f7848d","#1b6488","#584059"],"source":"https://scontent-iad3-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/80889131_204015484078153_4057153056574821763_n.jpg?_nc_ht=scontent-iad3-1.cdninstagram.com&_nc_cat=101&_nc_ohc=gEHImprrp00AX9wS27x&oh=69ca8f2eadd786c946750e84f2f6cf46&oe=5E80FEC0"}]}

```


## Install & run locally

Install:
```
git clone https://github.com/samg9/couleur.git  
cd couleur
```  
Create a virtualenv:  
```
python3 -m venv couleur   
```  
Activate it on Linux:
```
. couleur/bin/activate  
```  
Or on Windows cmd:  
```
couleur\Scripts\activate.bat  
```  
Install requirements:
```
pip install -r requirements.txt  
```  

export variables
```
export FLASK_APP=routes.py
```

Run app 
```
FLASK run
```

or via the Procfile with Gunicorn
```
gunicorn routes:app
```


View on [localhost:5000](http://127.0.0.1:5000)

