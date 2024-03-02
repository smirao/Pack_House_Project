const createBar = (title, denomerator, id) => {
    let d1 = document.createElement("div");
    d1.className = "outline-div";
    let outerp = document.createElement("p");
    outerp.className = "progress-text";
    outerp.innerHTML = `${title}: 0/${denomerator}`;
    outerp.id = `${id}_percent`;
    let d2 = document.createElement("div");
    d2.className = "center-div";
    let d3 = document.createElement("div");
    d3.className = "progress-in";
    d3.id = `${id}_comments`;

    let p = document.createElement("p");
    p.className = "outer-text";
    p.innerHTML = `${Math.round(0*100/denomerator)}%`
    
    d3.appendChild(p);
    d2.appendChild(d3);
    d1.appendChild(d2);
    d1.appendChild(outerp);

    return d1;
}

const editBar = (id, numerator, denomerator) => {
    let percent = Math.round(numerator*100/denomerator)
    let innerdiv = document.getElementById(`${id}_comments`);
    let outerp = document.getElementById(`${id}_percent`);

    if (percent <= 5){
        innerdiv.style.width = "5%";
        outerp.innerHTML = `${outerp.innerHTML.split(" ")[0]} ${numerator}/${denomerator}`;
    } else {
        innerdiv.style.width = `${percent}%`;
        innerdiv.innerHTML = `<p class="outer-text">${percent}%</p>`
        outerp.innerHTML = `${outerp.innerHTML.split(" ")[0]} ${numerator}/${denomerator}`;

    }
}

const createBars = (dict) => {
    let index = 0
    for (let key in dict){
        document.getElementById("bin").appendChild(createBar(key, Number(dict[key][1]), ++index));
    }
}

const updateBars = (dict) => {
    let index = 0
    for (let key in dict){
        editBar(++index, Number(dict[key][0]), Number(dict[key][1]));
    }
}

let dict = {
    // name : [numerator, denominator]
    "VSG":[0, 443]
}

window.addEventListener("load", (event) => {
    fetch('http:data').then(function (response) {
        return response.json();
    }).catch(function (err) {
        console.warn('Something went wrong.', err);
    }).then((data) => {
        createBars(data)
    }); 
    setInterval(function() {
        fetch('http:data').then(function (response) {
	        return response.json();
        }).catch(function (err) {
            console.warn('Something went wrong.', err);
        }).then((data) => {
            updateBars(data)
        });
    }, 2000);
});
