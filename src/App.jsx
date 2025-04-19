
import React from 'react';
import Plot from 'react-plotly.js';

const mockData = [
  { id: 'H1', energy: 420, co2: 110 },
  { id: 'H2', energy: 310, co2: 85 },
  { id: 'H3', energy: 278, co2: 65 },
];

export default function App() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">DSM+SAT Dashboard (v1)</h1>
      <div className="grid grid-cols-2 gap-6">
        <Plot
          data={[{ type: 'bar', x: mockData.map(d => d.id), y: mockData.map(d => d.energy), name: 'Energy' }]}
          layout={{ title: 'Top Energy Consumers', paper_bgcolor: '#0f0f0f', plot_bgcolor: '#0f0f0f', font: { color: 'white' } }}
        />
        <Plot
          data={[{ type: 'bar', x: mockData.map(d => d.id), y: mockData.map(d => d.co2), name: 'CO2' }]}
          layout={{ title: 'Top CO₂ Emitters', paper_bgcolor: '#0f0f0f', plot_bgcolor: '#0f0f0f', font: { color: 'white' } }}
        />
      </div>
    </div>
  );
}
