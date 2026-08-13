import { useState } from "react";
import { createApplication } from "../api";

function ApplicationForm({ onSaved }) {
  const [form, setForm] = useState({
    company: "",
    role: "",
    status: "Applied",
    date_applied: "",
    notes: "",
    link: "",
  });

  async function handleSubmit(e) {
    e.preventDefault();
    await createApplication(form);
    onSaved();
    setForm({
      company: "",
      role: "",
      status: "Applied",
      date_applied: "",
      notes: "",
      link: "",
    });
  }

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-3 bg-slate-800 p-4 rounded-lg">
      <h2 className="text-lg font-semibold text-white">Add Application</h2>

      <input
        value={form.company}
        onChange={(e) => setForm({ ...form, company: e.target.value })}
        placeholder="Company"
        required
        className="bg-slate-700 text-white p-2 rounded"
      />

      <input
        value={form.role}
        onChange={(e) => setForm({ ...form, role: e.target.value })}
        placeholder="Role"
        required
        className="bg-slate-700 text-white p-2 rounded"
      />

      <select
        value={form.status}
        onChange={(e) => setForm({ ...form, status: e.target.value })}
        className="bg-slate-700 text-white p-2 rounded"
      >
        <option value="Applied">Applied</option>
        <option value="Interview">Interview</option>
        <option value="Offer">Offer</option>
        <option value="Rejected">Rejected</option>
      </select>

      <input
        type="date"
        value={form.date_applied}
        onChange={(e) => setForm({ ...form, date_applied: e.target.value })}
        className="bg-slate-700 text-white p-2 rounded"
      />

      <input
        value={form.link}
        onChange={(e) => setForm({ ...form, link: e.target.value })}
        placeholder="Job link (optional)"
        className="bg-slate-700 text-white p-2 rounded"
      />

      <textarea
        value={form.notes}
        onChange={(e) => setForm({ ...form, notes: e.target.value })}
        placeholder="Notes (optional)"
        className="bg-slate-700 text-white p-2 rounded"
      />

      <button className="bg-blue-600 hover:bg-blue-700 text-white p-2 rounded font-medium">
        Save
      </button>
    </form>
  );
}

export default ApplicationForm;