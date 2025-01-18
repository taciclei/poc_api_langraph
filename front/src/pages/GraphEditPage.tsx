import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { graphService } from '../services/api'
import { GraphData } from '../types/graph'

const GraphEditPage = () => {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [graph, setGraph] = useState<GraphData | null>(null)

  useEffect(() => {
    if (id) {
      loadGraph(id)
    }
  }, [id])

  const loadGraph = async (graphId: string) => {
    try {
      const data = await graphService.getGraph(graphId)
      setGraph(data)
    } catch (error) {
      console.error('Error loading graph:', error)
      navigate('/')
    }
  }

  const handleSave = async () => {
    if (graph && id) {
      try {
        await graphService.updateGraph(id, graph)
        navigate('/')
      } catch (error) {
        console.error('Error updating graph:', error)
      }
    }
  }

  if (!graph) {
    return <div>Loading...</div>
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Edit Graph</h1>
      
      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">Name</label>
        <input
          type="text"
          value={graph.name}
          onChange={(e) => setGraph({ ...graph, name: e.target.value })}
          className="w-full px-3 py-2 border rounded"
        />
      </div>

      <div className="flex gap-2">
        <button
          onClick={handleSave}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Save
        </button>
        <button
          onClick={() => navigate('/')}
          className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
        >
          Cancel
        </button>
      </div>
    </div>
  )
}

export default GraphEditPage
