fetch('data.json')
  .then(response => response.json()) // Parse the response as JSON
  .then(data => {
    // Do something with the JSON data
    console.log(data);
     
    
    
  const tableBody = document.getElementById('table-body');
  const row = tableBody.insertRow();
  const col = tableBody.insertRow()

  const nameCell = row.insertCell();
  const ageCell = row.insertCell();
  const cityCell = row.insertCell();

  console.log(data + "kdfjdkfjl");

  nameCell.innerHTML = data.Silo1;
  ageCell.innerHTML = data.Silo2;
  cityCell.innerHTML = data.Silo3;


  // Get the progress bar cell
const progress = document.getElementById("progress");

// Generate a random height between 0 and 100
const height = Math.floor(Math.random() * 101);

// Set the height of the progress bar
progress.style.height = `${height}%`;

// Display the height in the progress bar cell
progress.textContent = height;

  })
  .catch(error => {
    // Handle any errors that occur
    console.error(error); 
   

  });
 
