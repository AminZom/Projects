// Put all onload AJAX calls here, and event listeners
$(document).ready(function() {
    // On page-load AJAX Example
    $("#loginModal").modal("show");
    $.ajax({
        type: 'get',            //Request type
        dataType: 'json',       //Data type - we will use JSON for almost everything 
        url: '/getUploads',     //The server endpoint we are connecting to
        success: function (data) {
            for(fileInfoJSON of data)
            {
				fileInfo = JSON.parse(fileInfoJSON);
				let fileLogPanel = document.getElementById("fileLogTable");
				let viewPanel = document.getElementById("viewPanelTable");
				let row = fileLogPanel.insertRow(-1);
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
				cell7.innerHTML = fileInfo.indivsNum;
				cell8.innerHTML = fileInfo.famsNum;
				document.getElementById("storeFiles").disabled = false;
				
				individuals = fileInfo.indivs;
				if(individuals != "none")
				{
					for(indiv of individuals)
					{
						let givenName = indiv.givenName;
						let surname = indiv.surname;
						let sex = indiv.sex;
						let row = viewPanel.insertRow(-1);
						let cell1=row.insertCell(0);
						let cell2=row.insertCell(1);
						let cell3=row.insertCell(2);
						let cell4=row.insertCell(3);
						let cell5=row.insertCell(4);
						cell1.innerHTML = givenName;
						cell2.innerHTML = surname;
						cell3.innerHTML = sex;
						cell4.innerHTML = "0";
						cell5.innerHTML = fileInfo.fileName.replace("uploads/","");
					}
				}
			}
        },
        fail: function(error) {
            console.log(error); 
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
	$("#loginButton").click(function(e){
		e.preventDefault();
		username = document.getElementById("username").value;
		password = document.getElementById("password").value;
		database = document.getElementById("database").value
		checkAccess = true;
        $.ajax({
			type: 'get',            //Request type
			dataType: 'json',       //Data type - we will use JSON for almost everything 
			data: {ID:username,pass:password,DB:database},
			url: '/logIn',   //The server endpoint we are connecting to
			success: function (data) {
				if(data.code == "ER_ACCESS_DENIED_ERROR" || data.code == "ER_NO_DB_ERROR" || data.code == "ER_DBACCESS_DENIED_ERROR")
				{
					$("#loginModal").modal("show");
					$("#loginNotif").html("Invalid username/password/database!");
				}
			},
			fail: function(error) {
				console.log("Something went wrong with the query: " + error);
			}
		});
		if(checkAccess == true)
		{
			$("#loginModal").modal("hide");
		}
		
        document.getElementById("username").value = "";
		document.getElementById("password").value = "";
		document.getElementById("database").value = "";
		$("#loginNotif").html("");
		$("#statusText").html("Successfully Logged in!<br />");
	});
	$("#storeFiles").click(function(e) {
		e.preventDefault();
		let fileLogTable = document.getElementById("fileLogTable");
		let viewTable = document.getElementById("viewPanelTable");
		let fileTableArray = [];
		let indivTableArray = [];
		for(let i = 1; i < fileLogTable.rows.length; i++)
		{
			let rowArray = [];
			for(let j = 0; j < 8; j++)
			{
				rowArray.push(fileLogTable.rows[i].cells[j].innerText);
			}
			fileTableArray.push(rowArray);
		}
		for(let x = 1; x < viewTable.rows.length; x++)
		{
			let rowArray2 = [];
			for(let k = 0; k < 5; k++)
			{
				rowArray2.push(viewTable.rows[x].cells[k].innerText);
			}
			indivTableArray.push(rowArray2);
		}
		$.ajax({
			type: 'get',             //Request type
			dataType: 'json',       //Data type - we will use JSON for almost everything 
			data: {fileTable:fileTableArray,indivTable:indivTableArray},
			url: '/storeAllFiles',   //The server endpoint we are connecting to
			success: function (data) {
			},
			fail: function(error) {
				console.log("Something went wrong with the query: " + error);
			}
		});
	});
	$("#clearData").click(function(e){
		e.preventDefault();
		$.ajax({
			type: 'get',             //Request type
			url: '/clearAllData',   //The server endpoint we are connecting to
			success: function (data) {
			},
			fail: function(error) {
				console.log("Something went wrong with the query: " + error);
			}
		});
	});
	$("#displayDB").click(function(e){
		e.preventDefault();
		$.ajax({
			type: 'get',             //Request type
			url: '/displayDBstatus',   //The server endpoint we are connecting to
			success: function (data) {
				$("#statusText").append(data + "<br />");
			},
			fail: function(error) {
				console.log("Something went wrong with the query: " + error);
			}
		});
	});
	$("#submitQuery").click(function(e){
		e.preventDefault();
		let menu = document.getElementById("querySubmit");
		let selection = menu.options[menu.selectedIndex].value;
		if(selection == 1)
		{
			let queryText = document.getElementById("selectQuery").value;
			$.ajax({
				type: 'get',             //Request type
				url: '/submitSimpleQuery',   //The server endpoint we are connecting to
				dataType: "json",
				data: {command:queryText},
				success: function (results) {
					$("#queryResultsTable tr").remove();
					for(let row of results)
					{
						console.log(row);
					}
				},
				fail: function(error) {
					console.log("Something went wrong with the query: " + error);
				}
			});
			document.getElementById("selectQuery").value = "SELECT";
		}
		else if(selection == 2)
		{
			let queryText = "select * from INDIVIDUAL ORDER BY \"surname\"";
			$.ajax({
				type: 'get',             //Request type
				url: '/submitSimpleQuery',   //The server endpoint we are connecting to
				dataType: "json",
				data: {command:queryText},
				success: function (results) {
					$("#queryResultsTable tr").remove();
					let resultsTable = document.getElementById("queryResultsTable");
					console.log(results);
					for(let row of results)
					{
						let newIndiv = resultsTable.insertRow(-1);
						let cell1=newIndiv.insertCell(0);
						let cell2=newIndiv.insertCell(1);
						let cell3=newIndiv.insertCell(2);
						let cell4=newIndiv.insertCell(3);
						let cell5=newIndiv.insertCell(4);
						let cell6=newIndiv.insertCell(5);
						cell1.innerHTML = row.ind_id;
						cell2.innerHTML = row.surname;
						cell3.innerHTML = row.given_name;
						cell4.innerHTML = row.sex;
						cell5.innerHTML = row.fam_size;
						cell6.innerHTML = row.source_file;
					}
					let headerRow = resultsTable.insertRow(0);
					let cell1=headerRow.insertCell(0);
					let cell2=headerRow.insertCell(1);
					let cell3=headerRow.insertCell(2);
					let cell4=headerRow.insertCell(3);
					let cell5=headerRow.insertCell(4);
					let cell6=headerRow.insertCell(5);
					cell1.innerHTML = "<strong>Individual ID</strong>";
					cell2.innerHTML = "<strong>Surname</strong>";
					cell3.innerHTML = "<strong>Given Name</strong>";
					cell4.innerHTML = "<strong>Sex</strong>";
					cell5.innerHTML = "<strong>Family Size</strong>";
					cell6.innerHTML = "<strong>Source File</strong>";
				},
				fail: function(error) {
					console.log("Something went wrong with the query: " + error);
				}
			});
		}
		else if(selection == 3)
		{
			let fileName = document.getElementById("fileQuery").value;
			console.log(fileName);
			if(fileName != "")
			{
				$.ajax({
					type: 'get',             //Request type
					url: '/submitFileQuery',   //The server endpoint we are connecting to
					dataType: "json",
					data: {command:fileName},
					success: function (results) {
						$("#queryResultsTable tr").remove();
						let resultsTable = document.getElementById("queryResultsTable");
						console.log(results);
						for(let row of results)
						{
							let newIndiv = resultsTable.insertRow(-1);
							let cell1=newIndiv.insertCell(0);
							let cell2=newIndiv.insertCell(1);
							let cell3=newIndiv.insertCell(2);
							let cell4=newIndiv.insertCell(3);
							let cell5=newIndiv.insertCell(4);
							let cell6=newIndiv.insertCell(5);
							cell1.innerHTML = row.ind_id;
							cell2.innerHTML = row.surname;
							cell3.innerHTML = row.given_name;
							cell4.innerHTML = row.sex;
							cell5.innerHTML = row.fam_size;
							cell6.innerHTML = row.source_file;
						}
						let headerRow = resultsTable.insertRow(0);
						let cell1=headerRow.insertCell(0);
						let cell2=headerRow.insertCell(1);
						let cell3=headerRow.insertCell(2);
						let cell4=headerRow.insertCell(3);
						let cell5=headerRow.insertCell(4);
						let cell6=headerRow.insertCell(5);
						cell1.innerHTML = "<strong>Individual ID</strong>";
						cell2.innerHTML = "<strong>Surname</strong>";
						cell3.innerHTML = "<strong>Given Name</strong>";
						cell4.innerHTML = "<strong>Sex</strong>";
						cell5.innerHTML = "<strong>Family Size</strong>";
						cell6.innerHTML = "<strong>Source File</strong>";
					},
					fail: function(error) {
						console.log("Something went wrong with the query: " + error);
					}
				});
				document.getElementById("fileQuery").value = "";
			}
		}
		else if(selection == 4)
		{
			let lastName = document.getElementById("myQuery1LastName").value;
			let sex = "";
			if(document.getElementById("radioMale").checked)
				sex = "M";
			else if(document.getElementById("radioFemale").checked)
				sex = "F";
			$.ajax({
				type: 'get',             //Request type
				url: '/submitQuery1',   //The server endpoint we are connecting to
				dataType: "json",
				data: {surname:lastName,Sex:sex},
				success: function (results) {
					$("#queryResultsTable tr").remove();
					let resultsTable = document.getElementById("queryResultsTable");
					console.log(results);
					for(let row of results)
					{
						let newIndiv = resultsTable.insertRow(-1);
						let cell1=newIndiv.insertCell(0);
						let cell2=newIndiv.insertCell(1);
						let cell3=newIndiv.insertCell(2);
						let cell4=newIndiv.insertCell(3);
						let cell5=newIndiv.insertCell(4);
						let cell6=newIndiv.insertCell(5);
						cell1.innerHTML = row.ind_id;
						cell2.innerHTML = row.surname;
						cell3.innerHTML = row.given_name;
						cell4.innerHTML = row.sex;
						cell5.innerHTML = row.fam_size;
						cell6.innerHTML = row.source_file;
					}
					let headerRow = resultsTable.insertRow(0);
					let cell1=headerRow.insertCell(0);
					let cell2=headerRow.insertCell(1);
					let cell3=headerRow.insertCell(2);
					let cell4=headerRow.insertCell(3);
					let cell5=headerRow.insertCell(4);
					let cell6=headerRow.insertCell(5);
					cell1.innerHTML = "<strong>Individual ID</strong>";
					cell2.innerHTML = "<strong>Surname</strong>";
					cell3.innerHTML = "<strong>Given Name</strong>";
					cell4.innerHTML = "<strong>Sex</strong>";
					cell5.innerHTML = "<strong>Family Size</strong>";
					cell6.innerHTML = "<strong>Source File</strong>";
				},
				fail: function(error) {
					console.log("Something went wrong with the query: " + error);
				}
			});
			document.getElementById("myQuery1LastName").value = "";
		}
		else if(selection == 5)
		{
			let indivNum = document.getElementById("myQuery2Indivs").value;
			let encoding = "";
			if(document.getElementById("queryRadioASCII").checked)
				encoding = "ASCII";
			else if(document.getElementById("queryRadioANSEL").checked)
				encoding = "ANSEL";
			else if(document.getElementById("queryRadioUTF8").checked)
				encoding = "UTF8";
			else if(document.getElementById("queryRadioUNICODE").checked)
				encoding = "UNICODE";
			$.ajax({
				type: 'get',             //Request type
				url: '/submitQuery2',   //The server endpoint we are connecting to
				dataType: "json",
				data: {num_individuals:indivNum,Encoding:encoding},
				success: function (results) {
					$("#queryResultsTable tr").remove();
					let resultsTable = document.getElementById("queryResultsTable");
					console.log(results);
					for(let row of results)
					{
						let newFile = resultsTable.insertRow(-1);
						let cell1=newFile.insertCell(0);
						let cell2=newFile.insertCell(1);
						let cell3=newFile.insertCell(2);
						let cell4=newFile.insertCell(3);
						let cell5=newFile.insertCell(4);
						let cell6=newFile.insertCell(5);
						let cell7=newFile.insertCell(6);
						let cell8=newFile.insertCell(7);
						let cell9=newFile.insertCell(8);
						cell1.innerHTML = row.file_id;
						cell2.innerHTML = row.file_Name;
						cell3.innerHTML = row.source;
						cell4.innerHTML = row.version;
						cell5.innerHTML = row.encoding;
						cell6.innerHTML = row.sub_name;
						cell7.innerHTML = row.sub_addr;
						cell8.innerHTML = row.num_individuals;
						cell9.innerHTML = row.num_families;
					}
					let headerRow = resultsTable.insertRow(0);
					let cell1=headerRow.insertCell(0);
						let cell2=headerRow.insertCell(1);
						let cell3=headerRow.insertCell(2);
						let cell4=headerRow.insertCell(3);
						let cell5=headerRow.insertCell(4);
						let cell6=headerRow.insertCell(5);
						let cell7=headerRow.insertCell(6);
						let cell8=headerRow.insertCell(7);
						let cell9=headerRow.insertCell(8);
						cell1.innerHTML = "<strong>file_id</strong>";
						cell2.innerHTML = "<strong>file_Name</strong>";
						cell3.innerHTML = "<strong>source</strong>";
						cell4.innerHTML = "<strong>version</strong>";
						cell5.innerHTML = "<strong>encoding</strong>";
						cell6.innerHTML = "<strong>sub_name</strong>";
						cell7.innerHTML = "<strong>sub_addr</strong>";
						cell8.innerHTML = "<strong>num_individuals</strong>";
						cell9.innerHTML = "<strong>num_families</strong>";
				},
				fail: function(error) {
					console.log("Something went wrong with the query: " + error);
				}
			});
			document.getElementById("myQuery2Indivs").value = "";
		}
		else if(selection == 6)
		{
			let fileName = document.getElementById("myQuery3FileName").value;
			let firstName = document.getElementById("myQuery3FirstName").value;
			$.ajax({
				type: 'get',             //Request type
				url: '/submitQuery3',   //The server endpoint we are connecting to
				dataType: "json",
				data: {filename:fileName,firstname:firstName},
				success: function (results) {
					$("#queryResultsTable tr").remove();
					let resultsTable = document.getElementById("queryResultsTable");
					console.log(results);
					for(let row of results)
					{
						let newIndiv = resultsTable.insertRow(-1);
						let cell1=newIndiv.insertCell(0);
						let cell2=newIndiv.insertCell(1);
						let cell3=newIndiv.insertCell(2);
						let cell4=newIndiv.insertCell(3);
						let cell5=newIndiv.insertCell(4);
						let cell6=newIndiv.insertCell(5);
						cell1.innerHTML = row.ind_id;
						cell2.innerHTML = row.surname;
						cell3.innerHTML = row.given_name;
						cell4.innerHTML = row.sex;
						cell5.innerHTML = row.fam_size;
						cell6.innerHTML = row.source_file;
					}
					let headerRow = resultsTable.insertRow(0);
					let cell1=headerRow.insertCell(0);
					let cell2=headerRow.insertCell(1);
					let cell3=headerRow.insertCell(2);
					let cell4=headerRow.insertCell(3);
					let cell5=headerRow.insertCell(4);
					let cell6=headerRow.insertCell(5);
					cell1.innerHTML = "<strong>Individual ID</strong>";
					cell2.innerHTML = "<strong>Surname</strong>";
					cell3.innerHTML = "<strong>Given Name</strong>";
					cell4.innerHTML = "<strong>Sex</strong>";
					cell5.innerHTML = "<strong>Family Size</strong>";
					cell6.innerHTML = "<strong>Source File</strong>";
				},
				fail: function(error) {
					console.log("Something went wrong with the query: " + error);
				}
			});
			document.getElementById("myQuery3FileName").value = "";
			document.getElementById("myQuery3FirstName").value = "";
		}
		else
			$("#statusText").append("Invalid selection!<br />");
	});
});
