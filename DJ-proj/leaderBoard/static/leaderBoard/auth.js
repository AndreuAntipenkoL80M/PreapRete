const data = document.currentScript.dataset;
const addr = data.adrr; 

	function checkUsersAuth(){
		fetch(`http://${addr}/profile_handler`, {
			method: 'GET',
		}).then(
			response => {
				console.log(response)
				dialogOptions = response.text();
				let dialog = document.createElement("div");
				document.body.appendChild(dialog);
				dialog.id = "dialog_div";
				dialog.classList.add("dialog_div");
				return dialogOptions
		}).then(
			response => {
				document.getElementById("dialog_div").innerHTML = response

		})
	}


	function processUsersAuth(link) {
		document.getElementById("dialog_div").remove()	
		fetch(link,{
			method: 'GET',
		}).then(
			response => {
			const typeofaction = response.headers.get('typeOfAction');
			const contentType = response.headers.get('Content-Type');
			backAddress = response.headers.get('back_address')
			if (typeofaction == "goodbye" || typeofaction == "farewell"){
				return Promise.reject(typeofaction);
			}
			myform = response.text();
			///console.log(myform)
			let form = document.createElement("div");
			document.body.appendChild(form);
			form.id = "form_div";
			form.classList.add("form_div");
			return myform
			}
		).then(
			form => {
				document.getElementById("form_div").innerHTML = form;
				form = document.getElementById("submitor").parentElement
                form.addEventListener('submit', (e) => {
                    e.preventDefault()
                    const data = new FormData(form)
					fetch(`http://${addr}:8080${backAddress}`, {
						method: "POST",
						headers:{
							'X-CSRFToken': csrftoken,
							'charset': 'utf-8',
						},
						body: data
					})
					.then(firstUnknownProm => {
						type = firstUnknownProm.headers.get("typeofaction")
						feedbackMessage = firstUnknownProm.json()
						return feedbackMessage
					})
					.then(secondUnknownProm => {
						console.log(secondUnknownProm, type)
						document.getElementById("dialog_with_user").innerHTML = reciveAnswer(type, secondUnknownProm.text)
					})
					document.getElementById("form_div").remove()	
                })
			},
			plainResponse => {
				console.log(plainResponse)
				document.getElementById("dialog_with_user").innerHTML = reciveAnswer(plainResponse, '')
				document.getElementById("form_div").remove()	

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
			case "greet":
				ans = `Привет ${name}, чё забыл?`
				break
			case "goodbye":
				ans = `Встал, вышел`
				break
			case "farewell":
				ans = `Прощай, скучать не будем (allegedly)`
				break
			case "updated":
				ans = `Изменения приняты, но нужны ли они были?`
				break
			case "wrongCredentials":
				ans = `Таких не знаем`
				break
			default:
				ans = "Ошибка, Ошибка, Ошибка."
		}
		return ans
    }
