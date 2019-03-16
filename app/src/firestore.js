import firebase from 'firebase/app'
import 'firebase/firestore'

// initialize your firebase app
const config = {
  apiKey: "AIzaSyA-miydMjsqhzzQQwZ5rjMy5EiLgFnadnY",
  authDomain: "readytable.firebaseapp.com",
  databaseURL: "https://readytable.firebaseio.com",
  projectId: "readytable",
  storageBucket: "readytable.appspot.com",
  messagingSenderId: "1086666026006"
}
firebase.initializeApp(config)

// save a reference to the firestore database
// to access it in the future
export default firebase.firestore()
