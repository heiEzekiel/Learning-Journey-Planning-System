var backendUrl = 'http://127.0.0.1:5000';
var getJourney = 'getJourney';
var deleteJourney = 'deleteJourney';
var getCourse = 'getCourseReg'
var getSkillStaff = 'getSkillStaff'
var getRole = 'getAllJobRole'
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

      if (data.code == 404) {
        document.getElementById("no_lj").innerHTML = " <span class=\"text-danger\">No ongoing Learning Journey </span>"
      } else {


        result = JSON.parse(JSON.stringify(data.data))
        getLJstatus(result)
      }
    })
    .catch(error => {
      // Errors when calling the service; such as network error, 
      // service offline, etc
      console.log(error);
    });
}

async function getLJstatus(journey) {
  var count = 0
  var lj_c = 0
  var message_str = ""

  const response =
    await fetch(`${backendUrl}/${getRole}`)
    .then(response => response.json())
    .then(data => {
      result = JSON.parse(JSON.stringify(data.data))
      console.log(result)
      var count = 0
      var lj_c = 0
      var message_str = ""





      for (lj of journey) {

        if (lj.journey_status == 'Completed') {
          count += 1
        } else {
          lj_c += 1
          for (r of result) {
            if(r.job_role_id==lj.j_fk_job_role_id){
            console.log(r.job_role_id)
            if (r.job_role_status == 0) { //active
              message_str += `                      
              <div class="card mt-3">
<div class="card-body">
<h5 class="card-title fs-6 fw-bold">${lj.journey_name}    
<span  onClick="removeJourney(${lj.journey_id})" class="mt-1 mx-1 btn btn-danger text-white float-end" style="font-size:10px;" >
Remove learning journey
</span>
<span onClick="location.href='./update_lj.html?id=${lj.journey_id}&name=${lj.journey_name}'" class="mt-1 btn btn-primary text-white float-end" style="font-size:10px;"> View Learning Journey </span>


</h5>

</div>
</div>`
            } else {
              message_str += `                      
              <div class="card mt-3">
<div class="card-body">
<h5 class="card-title fs-6 fw-bold">${lj.journey_name} <span class="text-danger">(Inactive)</span>   
<span  onClick="removeJourney(${lj.journey_id})" class="mt-1 mx-1 btn btn-danger text-white float-end" style="font-size:10px;" >
Remove learning journey
</span>
<span onClick="location.href='./update_lj.html?id=${lj.journey_id}&name=${lj.journey_name}'" class="mt-1 btn btn-primary text-white float-end" style="font-size:10px;"> View Learning Journey </span>


</h5>

</div>
</div>`
            }}
          }

        }


      }
      document.getElementById("countlj").innerText = lj_c
      document.getElementById("completedlj").innerText = count
      document.getElementById("lj").innerHTML += message_str
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