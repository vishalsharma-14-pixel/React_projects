import React from 'react'
import Header from './components/Header/Header'
import Footer from './components/Footer/Footer'
import { Outlet } from 'react-router-dom'
 
//this is for Outlet that keeps Header and Footer same if it is in between them

function Root() {
  return (
    <>
        <Header/>
        <Outlet/>  
        <Footer/>
    </>
  )
}

export default Root