'use strict'

// C library API
const ffi = require('ffi');

let dynamicLib = ffi.Library('./dynamicLib', {
  'createGEDCOMjson': [ 'string', ['string'] ],
  'createSimpleGEDCOM': [ 'void', ['string', 'string'] ],
});

const mySQL = require('mysql');

var connection;

// Express App (Routes)
const express = require("express");
const app     = express();
const path    = require("path");
const fileUpload = require('express-fileupload');

app.use(fileUpload());

// Minimization
const fs = require('fs');
const JavaScriptObfuscator = require('javascript-obfuscator');

// Important, pass in port as in `npm run dev 1234`, do not change
const portNum = process.argv[2];

// Send HTML at root, do not change
app.get('/',function(req,res){
  res.sendFile(path.join(__dirname+'/public/index.html'));
});

// Send Style, do not change
app.get('/style.css',function(req,res){
  //Feel free to change the contents of style.css to prettify your Web app
  res.sendFile(path.join(__dirname+'/public/style.css'));
});

// Send obfuscated JS, do not change
app.get('/index.js',function(req,res){
  fs.readFile(path.join(__dirname+'/public/index.js'), 'utf8', function(err, contents) {
    const minimizedContents = JavaScriptObfuscator.obfuscate(contents, {compact: true, controlFlowFlattening: true});
    res.contentType('application/javascript');
    res.send(minimizedContents._obfuscatedCode);
  });
});

//Respond to POST requests that upload files to uploads/ directory
app.post('/upload', function(req, res) {
  if(!req.files) {
    return res.status(400).send('No files were uploaded.');
  }
 
  let uploadFile = req.files.uploadFile;
 
  // Use the mv() method to place the file somewhere on your server
  uploadFile.mv('uploads/' + uploadFile.name, function(err) {
    if(err) {
      return res.status(500).send(err);
    }

    res.redirect('/');
  });
});

//Respond to GET requests for files in the uploads/ directory
app.get('/uploads/:name', function(req , res){
  fs.stat('uploads/' + req.params.name, function(err, stat) {
    console.log(err);
    if(err == null) {
      res.sendFile(path.join(__dirname+'/uploads/' + req.params.name));
    } else {
      res.send('');
    }
  });
});

//******************** Your code goes here ******************** 

//Sample endpoint
app.get('/getUploads', function(req , res){
	let fileInfoArray = [];
	let jsonStr = "";
	fs.readdirSync('./uploads/').forEach(file => {
		jsonStr = dynamicLib.createGEDCOMjson('uploads/' + file);
		fileInfoArray.push(jsonStr);
	});
    res.json(fileInfoArray);
});

app.get('/createSimpleGEDCOM', function(req , res){
	dynamicLib.createSimpleGEDCOM(req.query.json, req.query.fileName);
    res.send("");
});

app.get('/logIn', function(req, res) {
	connection = mySQL.createConnection({
		host	  :	  'dursley.socs.uoguelph.ca',
		user	  :	  req.query.ID,
		password  :	  req.query.pass,
		database  :	  req.query.DB
	});
	connection.connect();
	connection.query("SELECT * FROM FILE", function(err, rows, fields) {
		if(err)
		{
			res.send(err);
		}
	});
});

app.get('/storeAllFiles', function(req, res) {
	connection.query("create table FILE (file_id INT AUTO_INCREMENT PRIMARY KEY, file_Name VARCHAR(60) NOT NULL, source VARCHAR(250) NOT NULL, version VARCHAR(10) NOT NULL, encoding VARCHAR(10) NOT NULL, sub_name VARCHAR(62) NOT NULL, sub_addr VARCHAR(256), num_individuals INT, num_families INT);", function(err, rows, fields) {});
	connection.query("create table INDIVIDUAL (ind_id INT AUTO_INCREMENT PRIMARY KEY, surname VARCHAR(256) NOT NULL, given_name VARCHAR(256) NOT NULL, sex VARCHAR(1), fam_size INT, source_file INT, FOREIGN KEY(source_file) REFERENCES FILE (file_id) ON DELETE CASCADE);", function(err, rows, fields) {});
	let fileTable = req.query.fileTable;
	let indivTable = req.query.indivTable;
	for(let row of fileTable)
	{
		let file_Name = row[0];
		let source = row[1];
		let version = row[2];
		let encoding = row[3];
		let sub_name = row[4];
		let sub_addr = row[5];
		let num_individuals = row[6];
		let num_families = row[7];
		
		connection.query("insert into FILE values (null,\"" + file_Name + "\", \"" + source + "\", \"" + version + "\", \"" + encoding + "\", \"" + sub_name + "\", \"" + sub_addr + "\", \"" + num_individuals + "\", \"" + num_families + "\")", function(err, rows, fields) {
			if(err)
			{
				console.log(err);
			}
		});
	}
	for(let row2 of Object.keys(indivTable))
	{
		let givenName = `${indivTable[row2][0]}`;
		let surname = `${indivTable[row2][1]}`;
		let sex = `${indivTable[row2][2]}`;
		let famSize = `${indivTable[row2][3]}`;
		let fileName = `${indivTable[row2][4]}`;
		connection.query("select file_id from FILE where file_Name = \"" + fileName + "\"", function(err, rows, fields) {
			if(err)
			{
				console.log(err);
			}
			connection.query("insert into INDIVIDUAL values (null, \"" + surname + "\", \"" + givenName + "\", \"" + sex + "\", \"" + famSize + "\", \"" + rows[0].file_id + "\")", function(err, rows, fields) {
				if(err)
				{
					console.log(err);
				}
			});
		});
	}
	res.send("");
});

app.get('/clearAllData', function(req, res) {
	connection.query("delete from INDIVIDUAL", function(err, rows, fields) {
		if(err)
		{
			console.log(err);
		}
		else
		{
			connection.query("delete from FILE", function(err, rows, fields) {
				if(err)
				{
					console.log(err);
				}
			});
		}
	});
	res.send("");
});

app.get('/displayDBstatus', function(req, res) {
	var fileNum = 0;
	var indivNum = 0;
	connection.query("select * from INDIVIDUAL", function(err, rows, fields) {
		if(err)
		{
			console.log(err);
		}
		for(let row of rows)
		{
			indivNum++;
		}
		connection.query("select * from FILE", function(err, rows, fields) {
			if(err)
			{
				console.log(err);
			}
			for(let row of rows)
			{
				fileNum++;
			}
			res.send("Database has " + fileNum + " files and " + indivNum + " individuals.");
		});
	});
});

app.get('/submitSimpleQuery', function(req, res) {
	connection.query(req.query.command, function(err, rows, fields) {
		if(err)
		{
			console.log(err);
		}
		res.send(rows);
	});
});
app.get('/submitFileQuery', function(req, res) {
	let fileName = req.query.command;
	connection.query("select file_id from FILE where file_Name = \"" + fileName + "\"", function(err, rows, fields) {
		if(err)
		{
			console.log(err);
		}
		let queryText = "select * from INDIVIDUAL where source_file = \"" + rows[0].file_id + "\"";
		connection.query(queryText, function(err, rows, fields) {
			if(err)
			{
				console.log(err);
			}
			res.send(rows);
		});
	});
});
app.get('/submitQuery1', function(req, res) {
	let surname = req.query.surname;
	let sex = req.query.Sex;
	connection.query("select * from INDIVIDUAL where surname = \"" + surname + "\" AND sex = \"" + sex + "\"", function(err, rows, fields) {
		if(err)
		{
			console.log(err);
		}
		res.send(rows);
	});
});
app.get('/submitQuery2', function(req, res) {
	let indivNum = req.query.num_individuals;
	let encoding = req.query.Encoding;
	connection.query("select * from FILE where num_individuals < " + indivNum + " AND encoding = \"" + encoding + "\"", function(err, rows, fields) {
		if(err)
		{
			console.log(err);
		}
		res.send(rows);
	});
});
app.get('/submitQuery3', function(req, res) {
	let fileName = req.query.filename;
	let givenName = req.query.firstname
	connection.query("select file_id from FILE where file_Name = \"" + fileName + "\"", function(err, rows, fields) {
		if(err)
		{
			console.log(err);
		}
		let queryText = "select * from INDIVIDUAL where source_file = \"" + rows[0].file_id + "\" AND given_name = \"" + givenName + "\"";
		connection.query(queryText, function(err, rows, fields) {
			if(err)
			{
				console.log(err);
			}
			res.send(rows);
		});
	});
});
app.listen(portNum);
console.log('Running app at localhost: ' + portNum);
