export default async function apiCallDelete(endpoint) {
  const headers = {};
  const method = "DELETE";
  let body = null;
  const res = await fetch(import.meta.env.VITE_API_BASE_URL + "/" + endpoint, {
    method,
    headers: {
      "Content-Type": "application/json",
    },
    body,
  });
  const data = await res.json();
  const isSuccess = res.ok;
  const status = res.status;
  return {
    data,
    isSuccess,
    status,
  };
}
