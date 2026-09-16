import { createRoot } from 'react-dom/client'
import React from 'react'
import App from './App.jsx'

const name = 'Vishal'

const ReactElement = React.createElement(
  'a',
  {href: 'https://google.com', target: '_blank'},
  'Click me!',
  ' ',
  name
)


createRoot(document.getElementById('root')).render(
  
//    ReactElement
  <App/>

)
