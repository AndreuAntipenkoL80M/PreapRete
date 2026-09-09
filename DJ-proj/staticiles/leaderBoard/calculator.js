const operators = new Set (["+","-","*","/"]);

function calculatorStart() {
	document.getElementById("snakeStartButton").remove();
	document.getElementById("calculatorStartButton").remove()

	let expressionNode = document.createElement("p");
	document.getElementById("actionField").appendChild(expressionNode);
	expressionNode.innerHTML = "";
	expressionNode.id = "expression";
	//expression = document.getElementById("expression");





	let calculationButton = document.createElement("button");
	document.getElementById("actionField").appendChild(calculationButton);
	calculationButton.innerHTML = "Calculate";
	calculationButton.type = "button";
	calculationButton.onclick = function () {parenthesisSettler(expression)};

	let plusButton = document.createElement("button");
	document.getElementById("actionField").appendChild(plusButton);
	plusButton.innerHTML = "+";
	plusButton.type = "button";
	plusButton.onclick = plus;

	let minusButton = document.createElement("button");
	document.getElementById("actionField").appendChild(minusButton);
	minusButton.innerHTML = "-";
	minusButton.type = "button";
	minusButton.onclick = minus;

	let multiplicationButton = document.createElement("button");
	document.getElementById("actionField").appendChild(multiplicationButton);
	multiplicationButton.innerHTML = "*";
	multiplicationButton.type = "button";
	multiplicationButton.onclick = multiplication;

	let divisionButton = document.createElement("button");
	document.getElementById("actionField").appendChild(divisionButton);
	divisionButton.innerHTML = "/";
	divisionButton.type = "button";
	divisionButton.onclick = division;

	let openParenthesisButton = document.createElement("button");
	document.getElementById("actionField").appendChild(openParenthesisButton);
	openParenthesisButton.innerHTML = "(";
	openParenthesisButton.type = "button";
	openParenthesisButton.onclick = openParenthesis;

	let closeParenthesisButton = document.createElement("button");
	document.getElementById("actionField").appendChild(closeParenthesisButton);
	closeParenthesisButton.innerHTML = ")";
	closeParenthesisButton.type = "button";
	closeParenthesisButton.onclick = closeParenthesis;

	for (let i = 1; i<10; i++) {
		let num = document.createElement("button");
		document.getElementById("actionField").appendChild(num);
		num.innerHTML = i;
		num.id = "num"+i;
		num.type = "button";
		num.onclick = function(){
			expression += i;
			document.getElementById('expression').innerHTML = expression
		};
	}
	let num = document.createElement("button");
		document.getElementById("actionField").appendChild(num);
		num.innerHTML = 0;
		num.id = "num"+"0";
		num.type = "button";
		num.onclick = function(){
			expression += 0;
			document.getElementById('expression').innerHTML = expression
		};




	let clearButton = document.createElement("button");
	document.getElementById("actionField").appendChild(clearButton);
	clearButton.innerHTML = "clear";
	clearButton.type = "button";
	clearButton.onclick = function(){
		expression = '';
		document.getElementById('expression').innerHTML = expression;
		document.getElementById('result').innerHTML = ''
	};

	let stepBackButton = document.createElement("button");
	document.getElementById("actionField").appendChild(stepBackButton);
	stepBackButton.innerHTML = "'<<<'";
	stepBackButton.type = "button";
	stepBackButton.onclick = function(){
		expression = expression.slice(0,expression.length-1);
		document.getElementById('expression').innerHTML = expression;
	};



}


function plus (){
	expression = expression + "+";
	document.getElementById("expression").innerHTML = expression
}
function minus (){
	expression = expression + "-";
	document.getElementById("expression").innerHTML = expression		
}
function multiplication (){
	expression = expression + "*";
	document.getElementById("expression").innerHTML = expression		
}
function division (){
	expression = expression + "/";
	document.getElementById("expression").innerHTML = expression		
}
function openParenthesis (){
	expression = expression + "(";
	document.getElementById("expression").innerHTML = expression		
}
function closeParenthesis (){
	expression = expression + ")";
	document.getElementById("expression").innerHTML = expression		
}
function clear (){
	expression = '';
	document.getElementById('expression').innerHTML = expression;
	document.getElementById('result').innerHTML = ''
}








function parenthesisSettler(calculation) {
	if (operators.has(calculation[0])) {
			stop();
			return;
	}
	
	if (operators.has(calculation[calculation.length-1])) {
			stop();
			return;
	}
	
	
	let openp = 0;
	let closep = 0;
	for (let i = 0; i < calculation.length; i++) {
		if((operators.has(calculation[i]) && operators.has(calculation[i+1])) || ((calculation[i] == "(") && (calculation[i+1] == ")"))) {
			stop();
			return;
		}
		
		if (calculation[i] == "(") {
		//console.log("[qwevvcd");
			openp += 1
		}
		
		if (calculation[i] == ")") {
			closep += 1
		}
		
	}
	
	if (openp>=closep){
		for (i = 0; i < openp-closep; i++) {
			calculation += ")";
		}
	} else {
		stop();
		return;
	}
	
	
	
	
	
	let exp;
	if (calculation.indexOf('(') != -1) {
		if (calculation.lastIndexOf(')') != -1)  {
			if (calculation.indexOf('(') < calculation.lastIndexOf(')')) {
				exp = calculation.slice  (calculation.indexOf('(')+1    ,     calculation.lastIndexOf(')'));
				window.alert(exp);
				calculation = calculation.slice(0, calculation.indexOf('(')) + parenthesisSettler(exp) + calculation.slice(calculation.lastIndexOf(')')+1);
				window.alert(calculation+'vottakvot');
			} else {
				stop();
				return;
			}
		} else{
			stop();
			return;
		}
	}
	else{
		if (calculation.indexOf(')') != -1) {
			stop();
			return;
		}
		
	}
	window.alert('solution' + calculation);
	resulttt = solution (calculation);
	document.getElementById("result").innerHTML = resulttt
	return resulttt;
}

function stop(){
	//expression = '';
	//document.getElementById("expression").innerHTML = "";
	document.getElementById("result").innerHTML = "";
	window.alert('Хуйню написал');
}

























function solution(equasion){                //equasion - сторока без скобок
	window.alert('pochalosya');

	for (let i = equasion.length-1; i>=0; i--) {
		
			if (equasion[i] == '+' || equasion[i] == '-'){
				let a = equasion.slice(0,i);
				window.alert(a);
				let b = equasion.slice(i+1,equasion.length);
				window.alert(b);
				switch (equasion[i]){
					case "+":
						window.alert('a');
						let first = solution(a);
						let second = solution(b);
						window.alert(first+second);
						equasion = first+second;
						break;		
					case "-":
						window.alert('b');
						equasion = solution(a)-solution(b);
						break;
					
				} 
			}
	
	}
	for (i = 0; i < equasion.length; i++) {
		if (equasion[i] == '*' || equasion[i] == '/'){
			let a = equasion.slice(0,i);
			let b = equasion.slice(i+1,equasion.length);
			switch (equasion[i]){
				case "*":
					window.alert('c');
					equasion = solution(a)*solution(b);
					break;		
				case "/":
					window.alert('d');
					equasion = solution(a)/solution(b);
					break;

				
				
			} 
		}
	
	}
	let res = Number(equasion);
	window.alert(res + typeof(res));
	return res;
}







	window.alert(typeof(calculation));
