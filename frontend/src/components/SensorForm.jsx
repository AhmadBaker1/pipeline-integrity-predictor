import { useState } from "react";
import axios from "axios";

const SensorForm = ({ setPrediction, setSummary }) => {
    const [formData, setFormData] = useState({
        pressure: "",
        flow_rate: "",
        temperature: "",
        vibration: "",
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prev) => ({
            ...prev,
            [name]: value,  // keep as string
        }));
        
    };
    

    const handleSubmit = async (e) => {
        e.preventDefault();

        const payload = {
            pressure: parseFloat(formData.pressure),
            flow_rate: parseFloat(formData.flow_rate),
            temperature: parseFloat(formData.temperature),
            vibration: parseFloat(formData.vibration),
        };

        try {
            // Make the prediction
            const predictRes = await axios.post("http://localhost:8000/predict", payload);
            setPrediction(predictRes.data);

            // const reportRes = await axios.post("http://localhost:8000/generate-report", parsed, {
            //     responseType: "blob",
            // });

            // // Convert the PDF blob to a URL
            // const pdfBlob = new Blob([reportRes.data], { type: "application/pdf" });
            // const url = URL.createObjectURL(pdfBlob);
            // setReportUrl(url);

            // Generate AI summary from the prediction
            const summaryRes = await axios.post("http://localhost:8000/generate-summary", payload);
            const aiSummary = summaryRes?.data?.summary;
            if (aiSummary && typeof aiSummary === "string") {
                setSummary(aiSummary.trim());
            } else {
                setSummary("No summary generated or response was invalid.");
            }
        } catch (err) {
            console.error("Error during prediction or summary:", err);
            setPrediction(null);
            setSummary("An error occurred while processing your request. Please try again.");
        }
    };

    return (
    <form
      onSubmit={handleSubmit}
      className="rounded-2xl p-6 bg-gradient-to-br from-[#101624] to-[#0c0f1c] shadow-xl ring-1 ring-blue-500/20 hover:ring-blue-400/30 transition-all space-y-5"
    >
      <h2 className="text-xl font-bold text-cyan-400 mb-2 flex items-center gap-2">
        🧪 Sensor Input Panel
      </h2>

      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {[
          { label: "Pressure (psi)", name: "pressure", step: "0.01" },
          { label: "Flow Rate (m³/s)", name: "flow_rate", step: "0.01" },
          { label: "Temperature (°C)", name: "temperature", step: "0.1" },
          { label: "Vibration (g)", name: "vibration", step: "0.001" },
        ].map(({ label, name, step }) => (
          <div key={name}>
            <label className="block text-sm text-gray-400 mb-1">{label}</label>
            <input
              type="number"
              name={name}
              value={formData[name]}
              onChange={handleChange}
              step={step}
              required
              className="w-full px-3 py-2 rounded-md bg-gray-900 text-white placeholder-gray-500 border border-gray-700 focus:ring-2 focus:ring-cyan-500 focus:outline-none transition"
            />
          </div>
        ))}
      </div>

      <button
        type="submit"
        className="w-full py-3 mt-4 bg-cyan-600 hover:bg-cyan-500 text-white text-lg font-semibold rounded-lg shadow-md transition duration-200"
      >
        Run Integrity Check
      </button>
    </form>
  );
};

export default SensorForm;