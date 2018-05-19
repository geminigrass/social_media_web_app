window.onload=function() {
	var btn = document.getElementById("btn");
	btn.addEventListener('click',getFortune);

    function getFortune() {

        var req;

        if (window.XMLHttpRequest) {
            req = new XMLHttpRequest();
        } else {
            req = new ActiveXObject('Microsoft.XMLHTTP');
        }

        console.log(req);

        req.onreadystatechange = function () {

            // if(req.readyState != 4 || req.readyState != 200){
            //     return;
            // }
            //
            // var content = document.getElementById("content");
            // var items = JSON.parse(req.responseText);
            // // var newItem = document.createElement("li");
            // // newItem.innerHTML = items["fortune"];
            // // content.appendChild(newItem);
            // content.innerHTML = items;


            if (req.readyState !== 4 || req.status !== 200) {
                return;
            }
            alert(req.readyState);
            var content = document.getElementById('content');
            var fortune = JSON.parse(req.responseText);
            console.log(fortune["Meta Data"].length);
            // content.innerHTML = fortune[0]['name'];

        };
        req.open('GET', 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo', true);
        req.send();
    }
}

