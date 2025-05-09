document.getElementById("energyForm").addEventListener("submit", async function(e) {
    e.preventDefault();
  
    const power = document.getElementById("power").value;
    const hours = document.getElementById("hours").value;
    const cost = document.getElementById("cost").value;
  
    const response = await fetch("/calculate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ power, hours, cost })
    });
  
    const data = await response.json();
  
    document.getElementById("result").innerHTML = `
      <p><strong>Energy Consumed:</strong> ${data.energy_kwh} kWh</p>
      <p><strong>Estimated Cost:</strong> ₹${data.cost}</p>
    `;
  });

  
  