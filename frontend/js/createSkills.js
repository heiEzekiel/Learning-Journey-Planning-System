var backendUrl = 'http://127.0.0.1:5000/';
var create_skills = 'createSkills';
async function postAjax(url, method, data){
    return $.ajax({
        url: url,
        type: method || 'POST',
        crossDomain: true,
        data: JSON.stringify(data),
        dataType: "json"      
    });
};
async function createSkills() {
    var skillName = document.getElementById("skillName").value
    var skillStatus = document.getElementById("skillStatus").value
    var skillDescription = document.getElementById("skillDescription").value

    const website = backendUrl + create_skills;
    var data = {
        "skill_name":skillName,
        "skill_desc":skillDescription,
        "skill_status":skillStatus
    };
    const result = await postAjax(website, 'POST', data);
    console.log(result);
    alert("pasue");
    if (result.code === 200) {
        console.log(result)
        alert("Done");
    }

};