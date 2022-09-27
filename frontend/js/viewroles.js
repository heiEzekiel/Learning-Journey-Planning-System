backendUrl = "http://127.0.0.1:5000";
getAllJobRole = "getAllJobRole";

async function getAllRole() {
	const response = await fetch(`${backendUrl}/${getAllJobRole}`)
		.then((response) => response.json())
		.then((data) => {
			// console.log(JSON.parse(JSON.stringify(data.data)));
			result = JSON.parse(JSON.stringify(data.data));
			message_str = `
						<thead>
							<tr class="bg-light">
							<th>Job Role Id</th>
							<th>Job Role Name</th>
							<th>Job Role Description</th>
							<th>Click for more info</th>
							</tr>
						</thead>`;
			for (const role of result) {
				if (role["job_role_status"] == 0) {
					message_str += `
						<tbody>
							<tr>
								<th scope="row">${role["job_role_id"]}</th>
								<td>${role["job_role_name"]}</td>
								<td class="text-wrap w-50">${role["job_role_desc"]}</td>
								<td> <button type="button" class="btn btn-primary">View skills</button> </td>

							</tr>
						</tbody>
						`;
				}
			}
			document.getElementById("table").innerHTML = message_str;
			return data.roles;
		})
		.catch((error) => {
			// Errors when calling the service; such as network error,
			// service offline, etc
			console.log(error);
		});
}

getAllRole();
