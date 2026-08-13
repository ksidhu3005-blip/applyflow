import { useEffect, useState } from "react";
import { listApplications } from "./api";
import ApplicationForm from "./components/ApplicationForm";
import ApplicationTable from "./components/ApplicationTable";
import Dashboard from "./components/Dashboard";

function App() {
  const [applications, setApplications] = useState([]);
  const [refreshTrigger, setRefreshTrigger] = useState(0);

  function refresh() {
    listApplications().then((res) => setApplications(res.data));
    setRefreshTrigger((n) => n + 1);
  }

  useEffect(() => {
    refresh();
  }, []);

  return (
    <div className="min-h-screen bg-slate-900 p-8">
      <h1 className="text-3xl font-bold text-white mb-6">ApplyFlow</h1>

      <Dashboard refreshTrigger={refreshTrigger} />

      <div className="grid grid-cols-3 gap-6">
        <div className="col-span-1">
          <ApplicationForm onSaved={refresh} />
        </div>
        <div className="col-span-2 bg-slate-800 p-4 rounded-lg">
          <ApplicationTable applications={applications} onChanged={refresh} />
        </div>
      </div>
    </div>
  );
}

export default App;