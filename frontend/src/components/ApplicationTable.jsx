import { deleteApplication } from "../api";

const statusColors = {
  Applied: "bg-yellow-500",
  Interview: "bg-blue-500",
  Offer: "bg-green-500",
  Rejected: "bg-red-500",
};

function ApplicationTable({ applications, onChanged }) {
  async function handleDelete(id) {
    await deleteApplication(id);
    onChanged();
  }

  if (applications.length === 0) {
    return (
      <p className="text-slate-400 italic">
        No applications yet — add your first one.
      </p>
    );
  }

  return (
    <table className="w-full text-left text-white">
      <thead>
        <tr className="border-b border-slate-700 text-slate-400 text-sm">
          <th className="py-2">Company</th>
          <th>Role</th>
          <th>Status</th>
          <th>Date Applied</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        {applications.map((app) => (
          <tr key={app.id} className="border-b border-slate-800">
            <td className="py-2">{app.company}</td>
            <td>{app.role}</td>
            <td>
              <span
                className={`text-xs px-2 py-1 rounded ${statusColors[app.status]}`}
              >
                {app.status}
              </span>
            </td>
            <td>{app.date_applied || "—"}</td>
            <td>
              <button
                onClick={() => handleDelete(app.id)}
                className="text-red-400 hover:text-red-300 text-sm"
              >
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ApplicationTable;