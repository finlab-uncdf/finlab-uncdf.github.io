

$.getJSON("https://spreadsheets.google.com/feeds/list/1tgGaSMLodQz7kXkqDUPf_WOC02VYpHS-B7jYDT7AE1U/od6/public/values?alt=json", function(data) {
	var sheetData = data.feed.entry;
	var i;
	for (i = 0; i < sheetData.length; i++) {
		var name = data.feed.entry[i]['gsx$_cn6ca']['$t'];
		var age = data.feed.entry[i]['gsx$_cokwr']['$t'];
		var email = data.feed.entry[i]['gsx$_cpzh4']['$t'];
		console.log(name);
		console.log(age);
		console.log(email);
		console.log("hello");
		
		//        document.getElementById('demo').innerHTML += ('<tr>'+'<td>'+name+'</td>'+'<td>'+age+'</td>'+'<td>'+email+'</td>'+'</tr>');
	}
});

