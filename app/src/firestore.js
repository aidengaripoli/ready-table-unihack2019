import firebase from 'firebase/app'
import 'firebase/firestore'

// initialize your firebase app
const config = {
  apiKey: 'AIzaSyBflZzr3fTH6xS5nbs6_wfP8vDSegZre3Y',
  authDomain: 'midyear-reactor-233903.firebaseapp.com',
  databaseURL: 'https://midyear-reactor-233903.firebaseio.com',
  projectId: 'midyear-reactor-233903',
  storageBucket: 'midyear-reactor-233903.appspot.com',
  messagingSenderId: '972737790618'
}
firebase.initializeApp(config)

// save a reference to the firestore database
// to access it in the future
export default firebase.firestore()
