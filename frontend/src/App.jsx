import Sidebar from "./components/Sidebar";
import Dashboard from "./pages/Dashboard";

import './index.css';

const App = () => {
  return (
    <div className="flex h-screen bg-gray-950 text-white">
      <Sidebar />
      <main className="flex-1 overflow-y-auto p-8">
        <Dashboard />
      </main>
    </div>
  );
};

export default App;
