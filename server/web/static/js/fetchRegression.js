async function Regression(child) {
  const data = await fetch(`localhost:${PORT}/api/regression-graph`).then(
    (data) => {
      return data.json();
    }
  );
}
