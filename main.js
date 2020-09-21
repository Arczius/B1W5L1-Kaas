//Damian Vaartmans
//99061149
//software development

var ycheese = prompt("is de kaas geel?");
ycheese = ycheese.toLowerCase();
if(ycheese == "ja"){
	var gcheese = prompt("zitten er gaten in?");
	gcheese = gcheese.toLowerCase();
	if(gcheese == "ja"){
		var bdcheese = prompt("is de kaas belachelijk duur?");
		bdcheese = bdcheese.toLowerCase();
		if( bdcheese == "ja"){
			document.write("het is emmenthaler");
		}
		else{
			document.write("het is leerdammer");
		}
	}
	else{
		var hcheese = prompt("is de kaas hard als steen?");
		hcheese = hcheese.toLowerCase();
		if( hcheese	== "ja"){
			document.write("het is Parmigiano Reggiano");
		}
		else{
			document.write("het is goudse kaas");
		}
	}
}
else{
	var sccheese = prompt("heeft de kaas blauwe schimmel?");
	sccheese = sccheese.toLowerCase();
	if(sccheese == "ja"){
		var kkcheese = prompt("heeft de kaas een korst?")
		kkcheese = kkcheese.toLowerCase();
		if( kkcheese == "ja"){
			document.write("het is bleu de rochbaron")
		}
		else{
			document.write("het is foumme d'Ambert")
		}
	}
	else{
		var kcheese = prompt("heeft de kaas een korst?");
		kcheese = kcheese.toLowerCase();
		if(kcheese == "ja"){
			document.write("het is camembert");
		}
		else{
			document.write("het is mozzarella");
		}
	}
}