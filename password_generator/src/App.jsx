import { useState ,useCallback , useEffect , useRef} from 'react'



function App() {
  const [length, setLength]=useState(10)
  const [number, setNumber]=useState(false)
  const [character,setCharacter]=useState(false)
  const [password,setPassword]=useState()

  const passwordRef = useRef(null)

  const copyPasswordToClipboard = useCallback(() => {
    passwordRef.current?.select();
    passwordRef.current?.setSelectionRange(0, length); 
    navigator.clipboard.writeText(password);
  }, [password, length]);

  const passwordGenerator = useCallback( () => {
    let pass=""
    let str = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    if(number) str+="0123456789"
    if(character) str+="!@#$%^&*()~`<>:,./;"

    for(let i =1 ;i<= length ; i++){
        let char= Math.floor(Math.random()*str.length) +1
        pass += str.charAt(char)
    }
    setPassword(pass)

  } , [number,length,character,setPassword])


  useEffect( () => {
    passwordGenerator()
  } , [length,number,character,passwordGenerator])

  return (
    <>
     <div className="w-full min-h-screen flex my-2 flex-col items-center">

  <h1 className="text-4xl text-center my-2 text-white">
    Password Generator
  </h1>
    <br></br>
  <div className="w-full max-w-md rounded-xl text-red-600 text-center bg-gray-700 px-4 m-8">

    <div className="flex shadow rounded-2xl bg-white overflow-hidden mb-4 my-3">

      <input
        type="text"
        value={password}
        className="outline-none w-full py-1 px-3"
        placeholder="password"
        readOnly
        ref={passwordRef}
      />
       <button
        onClick={copyPasswordToClipboard}
        className='outline-none bg-blue-700 text-white px-3 py-0.5 shrink-0'
        >copy</button>

    </div>
    <div className='flex text-sm gap-x-2'>
      <div className='flex items-center gap-x-1'>
        <input 
          type="range"
          min={6}
          max={20}
          value={length}
          className='cursor-pointer'
          onChange={ (e) => {setLength(e.target.value)}}
        />
        <label>lenght:{length}</label>
      </div>
      <div className="flex items-center gap-x-1">
      <input
          type="checkbox"
          defaultChecked={number}
          id="numberInput"
          onChange={() => {
              setNumber((prev) => !prev);
          }}
      />
      <label htmlFor="numberInput">Numbers</label>
      </div>
      <div className="flex items-center gap-x-1">
      <input
          type="checkbox"
          defaultChecked={character}
          id="numberInput"
          onChange={() => {
              setCharacter((prev) => !prev);
          }}
      />
      <label htmlFor="characterInput">characters</label>
      </div>

    </div>
  </div>

</div>
    </>
  )
}

export default App
