import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { graphService } from '../services/api'
import { GraphData } from '../types/graph'

const GraphListPage = () => {
  const [graphs, setGraphs] = useState<GraphData[]>([])

  useEffect(() => {
    loadGraphs()
  }, [])

  const loadGraphs = async () => {
    try {
      const data = await graphService.listGraphs()
      setGraphs(data)
    } catch (error) {
      console.error('Error loading graphs:', error)
    }
  }

  const handleDeleteGraph = async (id: string) => {
    try {
      await graphService.deleteGraph(id)
      await loadGraphs()
    } catch (error) {
      console.error('Error deleting graph:', error)
    }
  }

  const handleExportGraph = async (id: string) => {
    try {
      await graphService.exportToFile(id, `graph-${id}.json`)
    } catch (error) {
      console.error('Error exporting graph:', error)
    }
  }

  const handleImportGraph = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0]
    if (file) {
      try {
        await graphService.importFromFile(file)
        await loadGraphs()
      } catch (error) {
        console.error('Error importing graph:', error)
      }
    }
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Graphs</h1>
      
      <div className="mb-4">
        <input
          type="file"
          accept=".json"
          onChange={handleImportGraph}
          className="hidden"
          id="import-file"
        />
        <label
          htmlFor="import-file"
          className="bg-blue-500 text-white px-4 py-2 rounded cursor-pointer hover:bg-blue-600"
        >
          Import Graph
        </label>
      </div>

      <div className="grid grid-cols-1 gap-4">
        {graphs.map((graph) => (
          <div
            key={graph.id}
            className="border p-4 rounded shadow flex justify-between items-center"
          >
            <div>
              <h2 className="text-xl font-semibold">{graph.name}</h2>
            </div>
            <div className="flex gap-2">
              <Link
                to={`/graphs/${graph.id}`}
                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
              >
                Edit
              </Link>
              <button
                onClick={() => handleExportGraph(graph.id)}
                className="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
              >
                Export
              </button>
              <button
                onClick={() => handleDeleteGraph(graph.id)}
                className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default GraphListPage
