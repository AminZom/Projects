// Put all onload AJAX calls here, and event listeners
$(document).ready(function() {
    // On page-load AJAX Example
    /*$.ajax({
        type: 'get',            //Request type
        dataType: 'json',       //Data type - we will use JSON for almost everything 
        url: '/getUploads',   //The server endpoint we are connecting to
        success: function (data) {
            //fileInfoArray = JSON.parse(data);
            for(fileInfoJSON of data)
            {
				fileInfo = JSON.parse(fileInfoJSON);
				console.log(fileInfo.gedcVersion);
				let fileLogPanel = document.getElementById("fileLogTable");
				let row = fileLogPanel.insertRow(1);
				let cell1=row.insertCell(0);
				let cell2=row.insertCell(1);
				let cell3=row.insertCell(2);
				let cell4=row.insertCell(3);
				let cell5=row.insertCell(4);
				let cell6=row.insertCell(5);
				let cell7=row.insertCell(6);
				let cell8=row.insertCell(7);
				cell1.innerHTML = "<a href=\"/uploads/" + fileInfo.fileName.replace("uploads/", "") + "\">" + fileInfo.fileName.replace("uploads/", "") + "</a>";
				cell2.innerHTML = fileInfo.source;
				cell3.innerHTML = fileInfo.gedcVersion;
				cell4.innerHTML = fileInfo.encoding;
				cell5.innerHTML = fileInfo.submitterName;
				cell6.innerHTML = fileInfo.submitterAddress;
			}
        },
        fail: function(error) {
            console.log(error); 
        }
    });*/

    // Event listener form replacement example, building a Single-Page-App, no redirects if possible
    $('#fileForm').submit(function(e){
        e.preventDefault();
        let file = document.getElementById("fileInput").value.replace("C:\\fakepath\\", "");
        if(file.split('.').pop() != "ged")
			$("#statusText").append("Not a valid GEDCOM file!<br />");
		else
		{
			$.ajax({
				type: 'post',       
				data: new FormData(document.getElementById("fileForm")),
				url: '/upload',   //The server endpoint we are connecting to
				processData: false,
				contentType: false,
				success: function (data) {
					//We write the object to the console to show that the request was successful
					$("#statusText").append("Uploaded file " + document.getElementById("fileInput").value.replace("C:\\fakepath\\", "") + "<br />");
					let fileLogPanel = document.getElementById("fileLogTable");
					let row = fileLogPanel.insertRow(-1);
					let cell1=row.insertCell(0);
					let cell2=row.insertCell(1);
					let cell3=row.insertCell(2);
					let cell4=row.insertCell(3);
					let cell5=row.insertCell(4);
					let cell6=row.insertCell(5);
					let cell7=row.insertCell(6);
					let cell8=row.insertCell(7);
					cell1.innerHTML = "<a href=\"/uploads/" + document.getElementById("fileInput").value.replace("C:\\fakepath\\", "") + "\">" + document.getElementById("fileInput").value.replace("C:\\fakepath\\", "") + "</a>";
				},
				fail: function(error) {
					alert(error); 
				}
			});
		}
    });
    $('#refresh').click(function(e){
		e.preventDefault();
		$.ajax({
			type: 'get',            //Request type
			dataType: 'json',       //Data type - we will use JSON for almost everything 
			url: '/getUploads',   //The server endpoint we are connecting to
			success: function (data) {
				console.log("Success!");
				//fileInfoArray = JSON.parse(data);
				for(fileInfoJSON of data)
				{
					fileInfo = JSON.parse(fileInfoJSON);
					let fileLogPanel = document.getElementById("fileLogTable");
					let row = fileLogPanel.insertRow(1);
					let cell1=row.insertCell(0);
					let cell2=row.insertCell(1);
					let cell3=row.insertCell(2);
					let cell4=row.insertCell(3);
					let cell5=row.insertCell(4);
					let cell6=row.insertCell(5);
					let cell7=row.insertCell(6);
					let cell8=row.insertCell(7);
					cell1.innerHTML = "<a href=\"/uploads/" + fileInfo.fileName.replace("uploads/", "") + "\">" + fileInfo.fileName.replace("uploads/", "") + "</a>";
					cell2.innerHTML = fileInfo.source;
					cell3.innerHTML = fileInfo.gedcVersion;
					cell4.innerHTML = fileInfo.encoding;
					cell5.innerHTML = fileInfo.submitterName;
					cell6.innerHTML = fileInfo.submitterAddress;
				}
			},
			fail: function(error) {
				console.log("ERROR!"); 
			}
		});
	});
    $('#clearStatus').click(function(e){
		e.preventDefault();
		$("#statusText").html("");
	});
    $('#uploadButton').click(function(e){
		e.preventDefault();
		$("#fileInput").trigger("click");
	});
	$("#fileInput").change(function(e){
		e.preventDefault();
		$("#fileForm").trigger("submit");
	});
	$('#createSimpleGEDCOM').click(function(e){
		e.preventDefault();
		let checkValid = true;
		if(document.getElementById("fileName").value == "")
		{
			checkValid = false;
			$("#statusText").append("File name cannot be empty!<br />");
		}
		if(document.getElementById("source").value == "")
		{
			checkValid = false;
			$("#statusText").append("Source cannot be empty!<br />");
		}
		if(document.getElementById("gedcVersion").value == "")
		{
			checkValid = false;
			$("#statusText").append("Gedc Version cannot be empty!<br />");
		}
		if(document.getElementById("submitterName").value == "")
		{
			checkValid = false;
			$("#statusText").append("Submitter name cannot be empty!<br />");
		}
		if(checkValid == true)
		{
			$("#GEDCOMform").trigger("submit");
			document.getElementById("fileName").value = "";
			document.getElementById("source").value = "PAF";
			document.getElementById("gedcVersion").value = 5.5;
			document.getElementById("submitterName").value = "";
			document.getElementById("submitterAddress").value = "";
		}
	});
	$("#GEDCOMform").submit(function(e){
		e.preventDefault();
		$("#statusText").append("Saved a new file " + document.getElementById("fileName").value + "<br />");
		let fileLogPanel = document.getElementById("fileLogTable");
		let row = fileLogPanel.insertRow(1);
		let cell1=row.insertCell(0);
		let cell2=row.insertCell(1);
		let cell3=row.insertCell(2);
		let cell4=row.insertCell(3);
		let cell5=row.insertCell(4);
		let cell6=row.insertCell(5);
		let cell7=row.insertCell(6);
		let cell8=row.insertCell(7);
        cell1.innerHTML = "<a href=\"/uploads/" + document.getElementById("fileName").value + "\">" + document.getElementById("fileName").value + "</a>";
        cell2.innerHTML = document.getElementById("source").value;
        cell3.innerHTML = document.getElementById("gedcVersion").value;
        if(document.getElementById("radioASCII").checked)
			cell4.innerHTML = "ASCII";
		else if(document.getElementById("radioUTF8").checked)
			cell4.innerHTML = "UTF-8";
		else if(document.getElementById("radioANSEL").checked)
			cell4.innerHTML = "ANSEL";
		else if(document.getElementById("radioUNICODE").checked)
			cell4.innerHTML = "UNICODE";
        cell5.innerHTML = document.getElementById("submitterName").value;
        cell6.innerHTML = document.getElementById("submitterAddress").value;
        cell7.innerHTML = 0;
        cell8.innerHTML = 0;
        
        let GEDCOMobj = new Object();
        GEDCOMobj.source = document.getElementById("source").value;
        GEDCOMobj.gedcVersion = document.getElementById("gedcVersion").value;
        if(document.getElementById("radioASCII").checked)
			GEDCOMobj.encoding = "ASCII";
		else if(document.getElementById("radioUTF8").checked)
			GEDCOMobj.encoding = "UTF8";
		else if(document.getElementById("radioANSEL").checked)
			GEDCOMobj.encoding = "ANSEL";
		else if(document.getElementById("radioUNICODE").checked)
			GEDCOMobj.encoding = "UNICODE";
		GEDCOMobj.submitterName = document.getElementById("submitterName").value;
		GEDCOMobj.submitterAddress = document.getElementById("submitterAddress").value;
		let GEDCOMjson = JSON.stringify(GEDCOMobj);
		let file = "uploads/" + document.getElementById("fileName").value
		$.ajax({
			type: 'get',            //Request type
			dataType: 'json',       //Data type - we will use JSON for almost everything 
			data: {json:GEDCOMjson,fileName:file},
			url: '/createSimpleGEDCOM',   //The server endpoint we are connecting to
			success: function (data) {
				console.log("success!");
			},
			fail: function(error) {
				console.log(error); 
			}
		});
	});
	
	$('#addIndividual').click(function(e){
		e.preventDefault();
		$("#addIndividualForm").trigger("submit");
        
        document.getElementById("givenName").value = "";
		document.getElementById("surname").value = "";
	});
	$("#addIndividualForm").submit(function(e){
		e.preventDefault();
		$("#statusText").append("Added a new Individual: " + document.getElementById("givenName").value + " " + document.getElementById("surname").value + "<br />");
		let fileLogPanel = document.getElementById("viewPanelTable");
		let row = fileLogPanel.insertRow(1);
		let cell1=row.insertCell(0);
		let cell2=row.insertCell(1);
		let cell3=row.insertCell(2);
		let cell4=row.insertCell(3);
		cell1.innerHTML = document.getElementById("givenName").value;
		cell2.innerHTML = document.getElementById("surname").value;
	});
	$('#getDescendants').click(function(e){
		e.preventDefault();
		$("#getDescendantsForm").trigger("submit");
        
        document.getElementById("givenNameDec").value = "";
		document.getElementById("surnameDec").value = "";
	});
	$("#getDescendantsForm").submit(function(e){
		e.preventDefault();
		/*let fileLogPanel = document.getElementById("viewPanelTable");
		let row = fileLogPanel.insertRow(1);
		let cell1=row.insertCell(0);
		let cell2=row.insertCell(1);
		let cell3=row.insertCell(2);
		let cell4=row.insertCell(3);
		cell1.innerHTML = document.getElementById("givenNameDec").value;
		cell2.innerHTML = document.getElementById("surnameDec").value;*/
	});
	$('#getAnscestors').click(function(e){
		e.preventDefault();
		$("#getAnscestorsForm").trigger("submit");
        
        document.getElementById("givenNameAns").value = "";
		document.getElementById("surnameAns").value = "";
	});
	$("#getAnscestorsForm").submit(function(e){
		e.preventDefault();
		/*let fileLogPanel = document.getElementById("viewPanelTable");
		let row = fileLogPanel.insertRow(1);
		let cell1=row.insertCell(0);
		let cell2=row.insertCell(1);
		let cell3=row.insertCell(2);
		let cell4=row.insertCell(3);
		cell1.innerHTML = document.getElementById("givenNameAns").value;
		cell2.innerHTML = document.getElementById("surnameAns").value;*/
	});
});
