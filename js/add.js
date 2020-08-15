//http://127.0.0.1:5000/add/cn=%22456%22&ed=%222020-08-09&fr=1&cc=%22123%22&ui=0

function SubmitData() {

    var cn = document.getElementById("TicketName").value;
    var ed = document.getElementById("ExpireTime").value;
    var fu = document.getElementById("FromUser").value;
    var cc = document.getElementById("TicketContent").value;
    var ui = cn ? 0 : 1;

    var theUrl = new URL('/add/cn=' + cn + "&ed=" + ed + "&fu=" + fu + "&cc=" + cc + "&ui=" + ui, Config["ApiServer"]);
    
    console.log(theUrl)
    //HTTP GET
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", theUrl, false); // false for synchronous request
    xmlHttp.send(null);
    return xmlHttp.responseText;
}

function dothis() {

}

