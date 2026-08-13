import { useEffect, useState } from "react";
import { getSummary } from "../api";

function Dashboard({ refreshTrigger }) {
  const [summary, setSummary] = useState({});

  useEffect(() => {
    getSummary().then((res) => setSummary(res.data));
  }, [refreshTrigger]);

  const statuses = ["Applied", "Interview", "Offer", "Rejected"];

  return (
    <div className="grid grid-cols-4 gap-4 mb-6">
      {statuses.map((status) => (
        <div key={status} className="bg-slate-800 p-4 rounded-lg text-center">
          <p className="text-slate-400 text-sm">{status}</p>
          <p className="text-2xl font-bold text-white">{summary[status] || 0}</p>
        </div>
      ))}
    </div>
  );
}

export default Dashboard;