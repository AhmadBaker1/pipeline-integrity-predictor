const ModelSummaryPanel = () => {
  return (
    <div className="relative rounded-2xl p-6 bg-gradient-to-br from-[#101624] to-[#0c0f1c] shadow-xl ring-1 ring-cyan-500/20 hover:ring-cyan-400/40 transition-all overflow-hidden group">

      {/* Glowing background shimmer */}
      <div className="absolute inset-0 bg-gradient-to-br from-cyan-800/10 to-transparent blur-xl opacity-30 group-hover:opacity-50 transition"></div>

      <h2 className="text-xl font-extrabold text-cyan-300 mb-4 flex items-center gap-2 z-10 relative">
        ⚙️ Model Engine
        <span className="text-xs bg-cyan-800/30 text-cyan-200 px-2 py-0.5 rounded-md ml-auto">
          v1.3.0
        </span>
      </h2>

      <div className="space-y-4 text-sm text-gray-300 z-10 relative">
        <div className="flex justify-between items-center">
          <div className="flex gap-2 items-center">
            🌲 <span className="text-gray-400">Regressor</span>
          </div>
          <span className="font-semibold text-yellow-300">RandomForest</span>
        </div>

        <div className="flex justify-between items-center">
          <div className="flex gap-2 items-center">
            🧠 <span className="text-gray-400">Classifier</span>
          </div>
          <span className="font-semibold text-pink-400">RandomForest</span>
        </div>

        <div className="flex justify-between items-center">
          <div className="flex gap-2 items-center">
            ⚡ <span className="text-gray-400">GenAI</span>
          </div>
          <span className="font-semibold text-purple-400">LLaMA 3 Turbo</span>
        </div>

        <div className="flex justify-between items-center">
          <span className="text-gray-400">Last Trained</span>
          <span className="text-green-300">May 31, 2025</span>
        </div>

        <div className="flex justify-between items-center">
          <span className="text-gray-400">Status</span>
          <span className="flex items-center gap-2 text-green-400 font-medium">
            <span className="h-2 w-2 bg-green-400 rounded-full animate-ping inline-block"></span>
            Online
          </span>
        </div>
      </div>
    </div>
  );
};

export default ModelSummaryPanel;
