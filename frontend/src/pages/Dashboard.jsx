import SensorForm from '../components/SensorForm';
import PredictionPanel from '../components/PredictionPanel';
import AISummaryPanel from '../components/AISummaryPanel';
import DownloadReportButton from '../components/DownloadReportButton';
import { useState } from 'react';
import ModelSummaryPanel from '../components/ModelSummaryPanel';

const Dashboard = () => {
    const [prediction, setPrediction] = useState(null);
    const [summary, setSummary] = useState("");

    return (
    <div className="min-h-screen  text-white px-8 py-10">
      <h1 className="text-4xl font-bold mb-10 tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-blue-500">
        🧠 Integrity AI Predictor
      </h1>

      {/* Grid Layout */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-10">
        <SensorForm setPrediction={setPrediction} setSummary={setSummary} />
        <ModelSummaryPanel />
      </div>

      {/* Prediction and AI Summary */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="rounded-xl p-6 bg-gradient-to-br from-[#1e293b] to-[#0f172a] shadow-xl ring-1 ring-cyan-700/30 backdrop-blur">
          <PredictionPanel prediction={prediction} />
        </div>

        <div className="rounded-xl p-6 bg-gradient-to-br from-[#1e293b] to-[#0f172a] shadow-xl ring-1 ring-purple-700/30 backdrop-blur">
          <AISummaryPanel summary={summary} />
        </div>
      </div>
    </div>
  );
};

export default Dashboard;