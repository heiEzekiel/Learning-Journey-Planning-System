backendUrl = 'http://127.0.0.1:5000';
getskills = 'getskills';

async function getAllSkills(){
    const response =
                await fetch(`${backendUrl}/${getskills}`)
                    .then(response => response.json())
                    .then(data => {
                        result =JSON.parse(JSON.stringify(data.data.skill))
                        message_str =  `
                        <thead>
                            <tr class="bg-light">
                            <th scope="col">Skill ID</th>
                            <th scope="col">Skill Name</th>
                            <th scope="col">Skill Description</th>
                            </tr>
                        </thead>`
                        for (const skill of result) {
                            if (skill['skill_status']==0){
                                message_str += `
                                <tbody>
                                    <tr>
                                        <th scope="row">${skill['skill_id']}</th>
                                        <td>${skill['skill_name']}</td>
                                        <td class="text-wrap w-50">${skill['skill_desc']}</td>
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