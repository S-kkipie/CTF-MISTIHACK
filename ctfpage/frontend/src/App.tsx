// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import { useEffect, useRef, useState } from 'react'
import './App.css'
import Overworld from './entyties/Overworld'
function App() {
  // const [count, setCount] = useState(0)
  const element = useRef<HTMLDivElement>(null)
  const [world, setWorld] = useState<Overworld | null>(null)
  const pending = useRef(false)

  useEffect(() => {
    if(pending.current) return
    pending.current = true
    setTimeout(() => {
      if (element.current) {
        const overworld = new Overworld({
          element: element.current,
        })
        setWorld(overworld)
        overworld.init()
      }
    }, 1000)
  },[])

  return (
    <>
      <div ref={element} className="game-container">
        <canvas className="game-canvas" width="352" height="198"></canvas>
      </div>
    </>
  )
}

export default App
