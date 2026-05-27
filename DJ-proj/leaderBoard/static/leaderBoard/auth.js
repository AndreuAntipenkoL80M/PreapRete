	function checkUsersAuth(){
		fetch('http://0.0.0.0:8000/profile_handler', {
			method: 'GET',
		})
		.then(
			response => {
			myform = response.text();
			///console.log(myform)
			let form = document.createElement("div");
			document.body.appendChild(form);
			form.id = "form_div"
			form.classList.add("form_div");
            const typeofaction = response.headers.get('typeOfAction')
			const contentType = response.headers.get('Content-Type');
			return myform
			}
		).then(
			form => {
				document.getElementById("form_div").innerHTML = form;
				form = document.getElementById("submitor").parentElement
                form.addEventListener('submit', (e) => {
                    e.preventDefault()
                    const data = new FormData(form)
					fetch("http://0.0.0.0:8000/req_user", {
						method: "POST",
						headers:{
							'X-CSRFToken': csrftoken,
							'charset': 'utf-8',
						},
						body: data
					})
					.then(r => {
						type = r.headers.get("typeofaction")
						feedbackMessage = r.json()
						return feedbackMessage
					})
					.then(f => {
						console.log(f, type)
						document.getElementById("dialog_with_user").innerHTML = reciveAnswer(type, f.text)
					})
					document.getElementById("form_div").remove()	
                })
			}
		)
	}
    function reciveAnswer(type, name){
		switch (type){
			case "login_occupied":
				ans = "Пользователь с таким именем уже существует"
				break;
			case "welcome":
				ans = `Привет ${name}, чё надо?`
				break
			default:
				ans = "Ошибка, Ошибка, Ошибка."

		}
		return ans
    }
