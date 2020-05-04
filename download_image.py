import pyrebase
config={
    "apiKey": "AIzaSyC4QalF52ELPBVdwLWuWQ2mk90S26UFH6c",
    "authDomain": "texttoimagetosummarizer.firebaseapp.com",
    "databaseURL": "https://texttoimagetosummarizer.firebaseio.com",
    "projectId": "texttoimagetosummarizer",
    "storageBucket": "texttoimagetosummarizer.appspot.com",
    "messagingSenderId": "231918504038",
    "appId": "1:231918504038:web:034d292e20137e5d9d45a7",
    "measurementId": "G-R1VVRYPNFQ"
}

firebase=pyrebase.initialize_app(config)
storage=firebase.storage()

path_on_cloud="/cloud1.jpg"
#path_local="sample1.png"

storage.child(path_on_cloud).download("download1.jpg")