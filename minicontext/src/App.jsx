import UserContextProvider from './context/UseContextProvider'
import Login from './components/Login'
import Profile from './components/Profile'
import './App.css'

function App() {
  
 

  return (
    <UserContextProvider >
      <h1>Hello this is the login page</h1>
      
      <Login />
      <Profile />
    </UserContextProvider>
  )
}

export default App
