export default async function apiCall(endpoint, params = null) {
  const headers = {};
  const method = params ? "POST" : "GET";
  let body = null;
  if (method == "POST") {
    headers["Content-Type"] = "application/json";
    body = JSON.stringify(params);
  }
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
