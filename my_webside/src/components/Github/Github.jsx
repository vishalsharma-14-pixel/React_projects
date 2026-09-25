import React, { useEffect } from 'react'
import { useState } from 'react'
import { useLoaderData } from 'react-router-dom'



function Github() {

    const data = useLoaderData()  // preloads the api call on hover to avoid delay 
//     const [data,setData]= useState([])

// useEffect(()=>{
//     fetch('https://api.github.com/users/vishalsharma-14-pixel')
//     .then(response => response.json())
//     .then(data => {
//         console.log(data)
//         setData(data)
//     })
// },[])

  return (
    <div className='text-center text-2xl text-white bg-orange-700 m-3 p-4 ' > Github Followes: {data.followers}
    <img src={data.avatar_url} alt='git picture' width={300}></img>
     </div>
  )
}

export default Github

export const gitInfoLoader = async () => {
    const response = await fetch('https://api.github.com/users/vishalsharma-14-pixel')
    return response.json()
}