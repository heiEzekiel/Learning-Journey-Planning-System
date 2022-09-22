backendUrl = "http://127.0.0.1:5000";
createJobRole = "createJobRole";

const role_name = document.getElementById("role_name");
const role_desc = document.getElementById("role_desc");
const btn = document.getElementById("btn");

btn.addEventListener("click", () => {
	const name = role_name.value;
	const desc = role_desc.value;

	if ((name == "") & (desc == "")) {
		alert("Input Role Name and Description!");
	} else if (name == "") {
		alert("Input Role Name!");
	} else if (desc == "") {
		alert("Input Role Description!");
	} else {
		axios
			.post(`${backendUrl}/${createJobRole}`, {
				job_role_name: name,
				job_role_desc: desc,
			})
			.then((response) => console.log(response))
			.catch((err) => console.log(err));
	}
});
