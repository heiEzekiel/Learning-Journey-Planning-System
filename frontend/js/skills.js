var backendUrl = 'http://testforljps-blqi.vercel.app';
var getskills = 'getskills';
var deleteSkill = 'deleteSkill';

async function removeSkill(id) {
    console.log(`${backendUrl}/${deleteSkill}/${id}`);
    fetch(`${backendUrl}/${deleteSkill}/${id}`, {
            method: 'DELETE'
        })
        .then((response) => response.json())
        .then((data) => {
            alert("Deleted skill successfully");
            location.reload();

        })
        .catch((error) => {
            // Errors when calling the service; such as network error,
            // service offline, etc
            console.log(error);
        });
}

async function getAllSkills(){
    const response =
        await fetch(`${backendUrl}/${getskills}`)
            .then(response => response.json())
            .then(data => {
                result =JSON.parse(JSON.stringify(data.data.skill))
                message_str =  `
                <thead>
                    <tr class="bg-light">
                    <th scope="col">Skill Name</th>
                    <th scope="col">Skill Description</th>
                    <th scope="col">Action</th>
                    </tr>
                </thead>`
                for (const skill of result) {
                    if (skill['skill_status']==0){
                        message_str += `
                        <tbody>
                            <tr>
                                <th scope="row">${skill['skill_name']}</th>
                                <td class="text-wrap w-50">${skill['skill_desc']}
                                <td class="text-wrap w-25"> 
                                <button type="button" class="btn btn-primary" >View Course</button>
                                <button type="button" class="btn btn-success" onClick="location.href='./updateskills.html?id=${skill['skill_id']}'">Edit</button>
                                <button type="button" class="btn btn-danger" onClick="removeSkill(${skill['skill_id']})" >Delete</button>
                                </td>
                            </tr>
                        </tbody>
                        `
                    }
                }
                document.getElementById('table').innerHTML = message_str
                return data.data.skill
            })
            .catch(error => {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                console.log(error);
            });
}

getAllSkills()
