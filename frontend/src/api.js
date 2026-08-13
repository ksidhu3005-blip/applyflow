import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const listApplications = (status = null, sortBy = "date_applied") =>
  api.get("/applications", { params: { status, sort_by: sortBy } });

export const createApplication = (data) =>
  api.post("/applications", data);

export const updateApplication = (id, data) =>
  api.patch(`/applications/${id}`, data);

export const deleteApplication = (id) =>
  api.delete(`/applications/${id}`);

export const getSummary = () =>
  api.get("/applications/summary");

export default api;