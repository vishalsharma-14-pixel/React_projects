import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import { RouterProvider, createBrowserRouter, createRoutesFromElements ,Route } from 'react-router-dom'
import Root from './Root.jsx'
import {About,ContactUs,User,Home,Github,gitInfoLoader} from './components'
// import Home from './components/Home/Home.jsx'
// import About from './components/About/About.jsx'
// import ContactUs from './components/ContactUs/ContactUs.jsx'
// import User from './components/User/User.jsx'
// import Github, { gitInfoLoader } from './components/Github/Github.jsx'

// const router = createBrowserRouter([
//   {
//     path:'/',
//     element: <Root/>,
//     children: [
//       {
//         path:'',
//         element:<Home/>
//       },
//       {
//         path:'/about',
//         element:<About/>
//       },
//       {
//         path:'/contact',
//         element:<ContactUs/>
//       },
//       {
//         path:'/user/userid',
//         element:<User/>
//       }
//     ]
//   }
// ])
const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path='/' element={<Root/>}>
      <Route index element={<Home/>} />
      <Route path='about' element={<About/>} />
      <Route path='contact' element={<ContactUs/>} />
      <Route path='user/:userid' element={<User/>}/>
      <Route 
      loader = {gitInfoLoader}
      path='github' 
      element={<Github/>}/>
    </Route>
  )
)

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router ={router}/>
  </StrictMode>,
)
