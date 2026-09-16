import {useState} from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  console.log(count)

  const addValue = () => {
    setCount(count + 1)
  }

  const subValue = () => {
    setCount(count - 1)
  }

  return (
    <>
      <h1>Counter App</h1>
      <h2>Count: {count}</h2>
      <h3>
      <button 
      onClick = {addValue}>
        Increase
      </button>
      </h3>
      <h3>
      <button
      onClick = {subValue}>
        Decrease 
      </button>
      </h3>
    </>
  )
}

export default App
