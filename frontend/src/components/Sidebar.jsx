const Sidebar = () => {
  return (
    <aside className="w-64 bg-gray-900 p-6 shadow-xl h-screen flex flex-col justify-between">
      <div>
        <h1 className="text-2xl font-bold mb-8 text-white">🛢 Integrity AI</h1>
        <nav className="flex flex-col space-y-4 text-sm text-gray-300">
          <a href="#" className="hover:text-blue-400">📊 Dashboard</a>
          <a href="#" className="text-gray-500 cursor-not-allowed">📁 Anomaly Logs (coming soon)</a>
          <a href="#" className="text-gray-500 cursor-not-allowed">📄 Reports</a>
        </nav>
      </div>
      <footer className="text-xs text-gray-500 mt-10">
        © {new Date().getFullYear()} Ahmad Baker
      </footer>
    </aside>
  );
};

export default Sidebar;
