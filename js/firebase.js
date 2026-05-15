// Firebase Imports
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-storage.js";

// Firebase Config
const firebaseConfig = {
  apiKey: "AIzaSyAyhf2xeg-DjNH8PReAIj9HoDCweuMfW_0",
  authDomain: "saudagar-farms.firebaseapp.com",
  projectId: "saudagar-farms",
  storageBucket: "saudagar-farms.appspot.com",
  messagingSenderId: "117290987720",
  appId: "1:117290987720:web:360aee5ab98af6e273b5fd",
  measurementId: "G-KYF7RJJ99P"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Services
const auth = getAuth(app);
const db = getFirestore(app);
const storage = getStorage(app);

// Export ONLY ONCE (IMPORTANT FIX)
export { auth, db, storage };