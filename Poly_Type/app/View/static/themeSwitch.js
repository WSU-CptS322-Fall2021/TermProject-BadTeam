const themes = ["solarized_dark", "insolate_dusk", "strawberry", "monochrome" ];
var currentTheme = localStorage['currentTheme'] || "solarized_dark";

function switchThemes() {
	let index = themes.indexOf(currentTheme);
	if(index == themes.length - 1){
		index = 0;
	}else{
		index = index + 1;
	}
	currentTheme = themes[index];
	let element = document.getElementById("themeContainer");
	element.setAttribute("class", currentTheme);
	document.getElementById("themeName").innerHTML = currentTheme;
	localStorage['currentTheme'] = currentTheme;
}

function initThemes() {
	
}

window.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM fully loaded and parsed');
	document.getElementById("themeContainer").setAttribute("class", currentTheme);
	document.getElementById("themeName").onclick = switchThemes;
	document.getElementById("themeName").innerHTML = currentTheme;
});