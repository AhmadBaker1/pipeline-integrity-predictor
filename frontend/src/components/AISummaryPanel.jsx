import { useEffect, useState } from "react";

const AISummaryPanel = ({ summary }) => {
  const [displayed, setDisplayed] = useState("");

  useEffect(() => {
  if (!summary || typeof summary !== "string") {
    setDisplayed("");
    return;
  }

  let i = 0;
  setDisplayed("");

  const interval = setInterval(() => {
    if (i < summary.length) {
      setDisplayed((prev) => prev + summary.charAt(i));
      i++;
    } else {
      clearInterval(interval);
    }
  }, 10);

  return () => clearInterval(interval);
}, [summary]);


  return (
    <div className="rounded-2xl bg-gradient-to-br from-[#1c1b2d] to-[#141122] shadow-xl p-6 ring-1 ring-purple-500/30 hover:ring-purple-400/50 transition">
      <h2 className="text-xl font-bold mb-4 text-purple-300 flex items-center gap-2">
        🧠 AI-Generated Summary
      </h2>

      {summary ? (
        <p className="text-gray-200 whitespace-pre-line leading-relaxed tracking-wide">
          {displayed}
        </p>
      ) : (
        <p className="text-gray-500 italic">No summary yet. Submit data to generate.</p>
      )}
    </div>
  );
};

export default AISummaryPanel;
