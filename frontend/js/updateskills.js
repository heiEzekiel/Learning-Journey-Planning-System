backendUrl = "http://127.0.0.1:5000";
skill_id = 1; // hard code for now, JY or me will change later on
updateSkill = "updateSkill/" + skill_id;
getSkills = "getSkills";

const skillID = document.getElementById("skill_ID").value;
const skill_Name = document.getElementById("skill_Name");
const skill_Description = document.getElementById("skill_Description");
const btn = document.getElementById("btn");

// const myData = function (data) {
// 	skillID = data.data.skill;
// 	console.log(skillID);
// 	return skillID;
// };

const myData = function (getAllSkills) {
	getid = 1;
	for (const listskills of getAllSkills) {
		// if(skillID.value )
		console.log(listskills["skill_id"]);
	}
	console.log("id:", getid);
	return getid;
};

async function getAllSkills() {
	const response = await fetch(`${backendUrl}/${getSkills}`)
		.then((response) => response.json())
		.then((data) => {
			// console.log(JSON.parse(JSON.stringify(data.data)));
			result = JSON.parse(JSON.stringify(data.data.skill));
			message_str = `
		<thead>
		<tr class="bg-light">
		<th scope="col">Skill ID</th>
		<th scope="col">Skill Name</th>
		<th scope="col">Skill Description</th>
		</tr>
		</thead>`;
			for (const skill of result) {
				if (skill["skill_status"] == 0) {
					message_str += `
				<tbody>
				<tr>
				<th scope="row">${skill["skill_id"]}</th>
				<td>${skill["skill_name"]}</td>
				<td class="text-wrap w-50">${skill["skill_desc"]}</td>
				</tr>
				</tbody>
				`;
				}
			}
			document.getElementById("table").innerHTML = message_str;
			// console.log(data.data.skill["skill_id"]);
			return data.data.skill;
		})
		.then(myData)
		.catch((error) => {
			// Errors when calling the service; such as network error,
			// service offline, etc
			console.log(error);
		});
}

getAllSkills();

async function updateSkills() {
	fetch(`${backendUrl}/${updateSkill}`, {
		method: "PUT",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			skill_name: document.getElementById("skill_Name").value,
			skill_desc: document.getElementById("skill_Description").value,
		}),
	})
		.then((response) => response.json())
		.then((data) => {
			console.log("Success:", data);
			if (data.code == 200) {
				location.reload();
			}
		})
		.catch((error) => {
			console.error("Error:", error);
		});
}
