from firebase import firebase


firebase = firebase.FirebaseApplication("https://athena-s-traffic.firebaseio.com/", None)
data = {
    'Name':'Parwiz Forogh',
    'Email':'par@gmail.com',
    'Phone':7149110000

}

result = firebase.post()