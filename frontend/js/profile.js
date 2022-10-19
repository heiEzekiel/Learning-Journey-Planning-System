var backendUrl = 'http://127.0.0.1:5000';
var getJourney = 'getJourney';
var deleteJourney = 'deleteJourney';
staff_id = 140001 // dynamic later

async function removeJourney(id) {
  fetch(`${backendUrl}/${deleteJourney}/${id}`, {
      method: 'DELETE'
    })
    .then((response) => response.json())
    .then((data) => {
      alert("Deleted journey successfully");
      location.reload();

    })
    .catch((error) => {
      // Errors when calling the service; such as network error,
      // service offline, etc
      console.log(error);
    });
}

async function getLJ(staff_id) {
    const response =
        await fetch(`${backendUrl}/${getJourney}/${staff_id}`)
        .then(response => response.json())
        .then(data => {
            result = JSON.parse(JSON.stringify(data.data))
            console.log(result)
            var message_str=""
            for (lj of result) {
                message_str += `                      
                <div class="card mt-3">
<div class="card-body">
  <h5 class="card-title fs-6 fw-bold">${lj.journey_name}    
  <span  onClick="removeJourney(${lj.journey_id})" class="mt-1 mx-1 btn btn-danger text-white float-end" style="font-size:10px;" >
  Remove learning journey
  </span>
  <span  class="mt-1 btn btn-primary text-white float-end" style="font-size:10px;">
    View Learning Journey
  </span>
  

</h5>
  
<h6 class="text-start"> Skills needed: A,B,C (static)

</h6>

</div>
</div>`
            }

            document.getElementById("lj").innerHTML+= message_str
        })
        .catch(error => {
            // Errors when calling the service; such as network error, 
            // service offline, etc
            console.log(error);
        });
}


getLJ(staff_id);