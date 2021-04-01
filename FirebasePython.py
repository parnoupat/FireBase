import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('helloworldfirebase-2d4d6-firebase-adminsdk-smhcc-ad5a1fd93f.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://helloworldfirebase-2d4d6-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('')


hopper_ref = ref.child('Users/-MXB7-grSifADtja01tn')
hopper_ref.delete()

print(ref.get())