var backendUrl = 'http://127.0.0.1:5000';
var getJourney = 'getJourney';
var deleteJourney = 'deleteJourney';
var getCourse = 'getCourseReg'
var getSkillStaff = 'getSkillStaff'
staff_id = 140001 // dynamic later

async function getCoursesRegistration(id) {
  await fetch(`${backendUrl}/${getCourse}/${id}`)
    .then(response => response.json())
    .then(data => {
      records = data.data
      var complete = 0
      var ongoing = 0
      for (c of records) {
        if (c.completion_status == 'Completed') {
          complete += 1
        } else if (c.completion_status == 'Ongoing') {
          ongoing += 1
        }
      }
      document.getElementById("completedC").innerText = complete;
      document.getElementById("ongoingC").innerText = ongoing;
    })
    .catch(error => {
      // Errors when calling the service; such as network error, 
      // service offline, etc
      console.log(error);
    });
}

async function getStaffSkill(id) {
  await fetch(`${backendUrl}/${getSkillStaff}/${id}`)
    .then(response => response.json())
    .then(data => {
      records = data.data
      var count = (records.length)
      document.getElementById("skillsattained").innerText = count;

    })
    .catch(error => {
      // Errors when calling the service; such as network error, 
      // service offline, etc
      console.log(error);
    });
}

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
      console.log(data)
      if (data.code ==404){
        document.getElementById("no_lj").innerHTML=" <span class=\"text-danger\">No ongoing Learning Journey </span>"
      }

      else{

     
      result = JSON.parse(JSON.stringify(data.data))
      var count=0
      var message_str = ""
      
  

      for (lj of result) {

        if (lj.journey_status == 'Completed') {
          count+= 1
        } else {
          message_str += `                      
                <div class="card mt-3">
<div class="card-body">
  <h5 class="card-title fs-6 fw-bold">${lj.journey_name}    
  <span  onClick="removeJourney(${lj.journey_id})" class="mt-1 mx-1 btn btn-danger text-white float-end" style="font-size:10px;" >
  Remove learning journey
  </span>
  <span  onClick="location.href='./update_lj.html?id=${lj.journey_id}&name=${lj.journey_name}'" class="mt-1 btn btn-primary text-white float-end" style="font-size:10px;">
    View Learning Journey
  </span>
  

</h5>

</div>
</div>`
        }


      }
      document.getElementById("completedlj").innerText = count
      document.getElementById("lj").innerHTML += message_str }
    })
    .catch(error => {
      // Errors when calling the service; such as network error, 
      // service offline, etc
      console.log(error);
    });
}


getLJ(staff_id);
getCoursesRegistration(staff_id);
getStaffSkill(staff_id);