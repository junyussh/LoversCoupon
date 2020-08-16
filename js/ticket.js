function AddCard(CardName, FromUser, ExpireDate, CardContent) {
    var cardList = document.getElementById("cardList");

    var newCard = document.createElement("div");                 // Create a <li> node
    newCard.className = "ts primary card";

    var innerDiv1 = document.createElement('div');
    innerDiv1.className = "content";

    var innerDiv11 = document.createElement('div');
    innerDiv11.className = "header";

    var innerDiv12 = document.createElement('div');
    innerDiv12.className = "description";

    var innerDiv121 = document.createElement("p");
    innerDiv121.innerHTML = "From: " + FromUser + "  |  到期日：" + ExpireDate;

    var innerDiv122 = document.createElement("p");
    innerDiv122.innerHTML = CardContent
    innerDiv11.innerHTML = CardName;

    innerDiv12.appendChild(innerDiv121);
    innerDiv12.appendChild(innerDiv122);
    innerDiv1.appendChild(innerDiv11);
    innerDiv1.appendChild(innerDiv12);
    newCard.appendChild(innerDiv1);                         // Append the text to <li>
    cardList.appendChild(newCard);     // Append <li> to <ul> with id="myList"
}

function SearchParams() {
    var url = location.href;

    //再來用去尋找網址列中是否有資料傳遞(QueryString)
    if (url.indexOf('?') != -1) {
        var user = "";
        //在此直接將各自的參數資料切割放進ary中
        var ary = url.split('?')[1].split('&');
        user = ary[0].split('=')[1];
        return user;
    }
}

function GetUserData(userId) {
    let target = new URL('/get/user=' + userId, Config["ApiServer"]);
    let ReturnData = {};

    fetch(target, {})
        .then((response) => {

            //console.log(response);

            ReturnData = response.json();
            return response.json();
        }).then((data) => {
            console.log(data)
            //ReturnData = data;
        }).catch((err) => {
            console.log('錯誤:', err);
        });

    return ReturnData;
}

function SetUserName(UserId){
    document.getElementById("username").innerHTML = Config["UserId"][UserId];
}

function SetCookie(UserId){
    document.cookie = "userId=UserId"
}
function dothis() {
    let UserId = SearchParams()
    let target = Config["ApiServer"] + '/get/user=' + UserId;

    SetUserName(UserId);
    SetCookie(UserId);
    
    fetch(target, {})
        .then((response) => {
            return response.json();
        }).then((data) => {
            console.log(data)

            data["card"].forEach(function(element){
                AddCard(element["CouponName"], Config["UserId"][element["FromUser"]], element["ExpireDate"], element["CouponContent"])});
        }).catch((err) => {
            console.log('錯誤:', err);
        });

    //console.log(UserData["user"]);
    //UserData.card.forEach(element => console.log(element));
}