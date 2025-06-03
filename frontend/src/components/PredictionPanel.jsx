const PredictionPanel = ({ prediction }) => {
  return (
    <div className="rounded-2xl bg-gradient-to-br from-[#1c1f2b] to-[#12141c] shadow-xl p-6 ring-1 ring-cyan-500/30 hover:ring-cyan-400/50 transition">
      <h2 className="text-xl font-bold mb-4 text-cyan-400 flex items-center gap-2">
        📊 Prediction Result
      </h2>

      {prediction ? (
        <div className="space-y-4 text-gray-200">
          <div className="flex justify-between items-center">
            <span className="text-sm text-gray-400">Risk Score:</span>
            <span className="text-lg font-semibold text-yellow-300">{prediction.risk_score}</span>
          </div>

          <div className="flex justify-between items-center">
            <span className="text-sm text-gray-400">Detected Issue:</span>
            <span className="text-lg font-semibold text-red-400">{prediction.detected_issue}</span>
          </div>

          <hr className="border-gray-700" />

          <div>
            <p className="text-sm text-gray-400 mb-2">Sensor Snapshot:</p>
            <pre className="bg-[#0d1117] p-3 rounded-md text-sm border border-gray-700 text-gray-300 overflow-x-auto">
              {JSON.stringify(prediction.input, null, 2)}
            </pre>
          </div>
        </div>
      ) : (
        <p className="text-gray-500 italic">No prediction yet. Submit sensor data above.</p>
      )}
    </div>
  );
};

export default PredictionPanel;
