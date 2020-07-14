//-----------------tab links----------------

function openProduct(evt, ProductName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(ProductName).style.display = "block";
    evt.currentTarget.className += " active";
}//openProduct

// Get the element with id and click on it (opens the id by default)
document.getElementById("defaultOpen").click();

//---------------data-base--------------------------

let slideNum = 1;

const modalsDiv = document.querySelector('.modal-content');

// --------------fetch-iceCreams----------------
const iceCreamsDiv= document.querySelector('.iceCreams')

async function fetchData() {
    await fetch('/order/ice_cream').then(response => response.json())
        .then(data => {
            displayCookieFilling(data);
            displayFlavours(data,iceCreamsDiv,"ice_cream");
        })
        .catch(error => console.error(error));

    await fetch('/order/topping').then(response => response.json()).then(data => displayToppings(data)).catch(error => console.error(error));
    await fetch('/order/cookie').then(response => response.json()).then(data => displayCookies(data)).catch(error => console.error(error));
    await fetch('/order/yogurt').then(response => response.json()).then(data => displayFlavours(data,yogurtsDiv,"yogurt")).catch(error => console.error(error));
}
fetchData();

// --------------fetch-yogurts----------------
const yogurtsDiv= document.querySelector('.yogurts');

// --------------flavours function----------------

function displayFlavours(data, generalDiv, type) {
    if (data.success){
        const flavours = data.flavours;
        let newTrio;
        for(let flavour of flavours) {
            let newDiv = document.createElement('div');
            newDiv.innerHTML=`
                <img src="/static/media/img/flavours/${flavour.SmallImage}" alt="${flavour.Flavour}" onclick="openModal();currentSlide(${slideNum})" class="taste-image hover-shadow cursor"><br>
                <input type="checkbox" id="${flavour.FlavourID}" name="${type}_tastes" value="${flavour.FlavourID}" >
                <label for="${flavour.FlavourID}">${flavour.Flavour}</label>
            `;
            if((slideNum-1)%3===0){
                newTrio = document.createElement('div');
                newTrio.className = 'tastes-wrapper';
            }
            newTrio.appendChild(newDiv);
            if((slideNum)%3===0){
                generalDiv.appendChild(newTrio);
            }
            let newSlideDiv = document.createElement('div');
            newSlideDiv.className = 'mySlides';
            newSlideDiv.innerHTML=`
                <img src="/static/media/img/flavours/${flavour.BigImage}" alt="${flavour.Flavour}" class="demo">
                <div>${flavour.Description}</div>
            `;
            modalsDiv.appendChild(newSlideDiv);
            slideNum++;
        }
    }
}//display flavours
// --------------fetch-cookies----------------

const cookiesDiv = document.querySelector('.cookies');

function displayCookies(data) {
    if (data.success){
        const objects = data.cookies;
        let newTrio;
        for(let object of objects) {
            let newDiv = document.createElement('div');
            newDiv.innerHTML=`
                <img src="/static/media/img/cookie/${object.SmallImage}" alt="${object.CookieType}" onclick="openModal();currentSlide(${slideNum})" class="taste-image hover-shadow cursor"><br>
                <input type="radio" id="${object.CookieID}" name="cookie_chosen" value="${object.CookieID}" >
                <label for="${object.CookieID}">${object.CookieType}</label>
            `;
            if((slideNum-1)%3===0){
                newTrio = document.createElement('div');
                newTrio.className = 'tastes-wrapper';
            }
            newTrio.appendChild(newDiv);
            if((slideNum)%3===0){
                cookiesDiv.appendChild(newTrio);
            }
            let newSlideDiv = document.createElement('div');
            newSlideDiv.className = 'mySlides';
            newSlideDiv.innerHTML=`
                <img src="/static/media/img/cookie/${object.BigImage}" alt="${object.CookieType}" class="demo">
            `;
            modalsDiv.appendChild(newSlideDiv);
            slideNum++;
        }
    }
}//display Cookies

const fillingDiv = document.querySelector('.icecreams-filling')
let fillingID = 100;
function displayCookieFilling(data) {
    if (data.success){
        const flavours = data.flavours;
        let newTrio;
        for(let flavour of flavours) {
            let newDiv = document.createElement('div');
            newDiv.innerHTML=`
                <img src="/static/media/img/flavours/${flavour.SmallImage}" alt="${flavour.Flavour}" onclick="openModal();currentSlide(${slideNum})" class="taste-image hover-shadow cursor"><br>
                <input type="radio" id="${fillingID}" name="cookie_filling" value="${flavour.FlavourID}" >
                <label for="${fillingID}">${flavour.Flavour}</label>
            `;
            if((slideNum-1)%3===0){
                newTrio = document.createElement('div');
                newTrio.className = 'tastes-wrapper';
            }
            newTrio.appendChild(newDiv);
            if((slideNum)%3===0){
                fillingDiv.appendChild(newTrio);
            }
            let newSlideDiv = document.createElement('div');
            newSlideDiv.className = 'mySlides';
            newSlideDiv.innerHTML=`
                <img src="/static/media/img/flavours/${flavour.BigImage}" alt="${flavour.Flavour}" class="demo">
                <div>${flavour.Description}</div>
            `;
            modalsDiv.appendChild(newSlideDiv);
            slideNum++;
            fillingID++;
        }
    }
}//displayCookieFilling

// --------------fetch-toppings----------------
const toppingsDiv= document.querySelector('.toppings');

function displayToppings(data) {
    if (data.success){
        const objects = data.toppings;
        let newTrio;
        for(let object of objects) {
            let newDiv = document.createElement('div');
            newDiv.innerHTML=`
                <img src="/static/media/img/yogurt_toppings/${object.SmallImage}" alt="${object.ToppingName}" onclick="openModal();currentSlide(${slideNum})" class="taste-image hover-shadow cursor"><br>
                <input type="checkbox" id="${object.ToppingID}" name="toppings_chosen" value="${object.ToppingID}" >
                <label for="${object.ToppingID}">${object.ToppingName}</label>
            `;
            if((slideNum-1)%3===0){
                newTrio = document.createElement('div');
                newTrio.className = 'tastes-wrapper';
            }
            newTrio.appendChild(newDiv);
            if((slideNum)%3===0){
                toppingsDiv.appendChild(newTrio);
            }
            let newSlideDiv = document.createElement('div');
            newSlideDiv.className = 'mySlides';
            newSlideDiv.innerHTML=`
                <img src="/static/media/img/yogurt_toppings/${object.BigImage}" alt="${object.ToppingName}" class="demo">
            `;
            modalsDiv.appendChild(newSlideDiv);
            slideNum++;
        }
    }
}//display Toppings

// --------------select amount and check number of checkboxes----------------

function amountSelect() {
    if (document.getElementById("half").selected) {
        document.getElementById("half-text").style.display = "block";
        document.getElementById("one-text").style.display = "none";
    } else {
        document.getElementById("half-text").style.display = "none";
        document.getElementById("one-text").style.display = "block";
    }
}

function checkStatusIceCream(){
    const submitIceCream = document.getElementById("submitIceCream");
    const countCheckSelected = document.querySelectorAll('input[name=ice_cream_tastes]:checked').length;

    if (countCheckSelected == 0){
        alert("לא נבחרו טעמי גלידה רצויים, יש לבחור לפחות טעם אחד");
    } else {
        if (document.getElementById("half").selected) {
            if(countCheckSelected>3){
                alert("נא לבחור שלושה טעמי גלידה לכל היותר");
            } else {
                submitIceCream.click();
                AlertAddedItem();
            }
        } else {
            if(countCheckSelected>5){
                alert("נא לבחור חמישה טעמי גלידה לכל היותר");
            } else {
                submitIceCream.click();
                AlertAddedItem();
            }
        }
    }
}//checkStatusIceCream

function checkStatusYogurt(){
    const submitYogurt = document.getElementById("submitYogurt");
    const countCheckSelectedYogurt = document.querySelectorAll('input[name=yogurt_tastes]:checked').length;
    const countCheckSelectedTopping = document.querySelectorAll('input[name=toppings_chosen]:checked').length;
    if (countCheckSelectedYogurt == 0){
        alert("לא נבחרו טעמי יוגורט רצויים, יש לבחור לפחות טעם אחד");
    } else if(countCheckSelectedYogurt>3){
        alert("נא לבחור שלושה טעמי יוגורט לכל היותר");
    } else if(countCheckSelectedTopping>10) {
        alert("נא לבחור עשר תוספות לכל היותר");
    } else {
        submitYogurt.click();
        AlertAddedItem();
    }
}//checkStatusYogurt

function checkStatusCookie(){
    const submitCookie = document.getElementById("submitCookie");
    const countCheckSelectedCookie = document.querySelectorAll('input[name=cookie_chosen]:checked').length;
    const countCheckSelectedFilling = document.querySelectorAll('input[name=cookie_filling]:checked').length;
    if (countCheckSelectedCookie == 0){
        alert("לא נבחר סוג העוגיה");
    } else if(countCheckSelectedFilling == 0){
        alert("לא נבחר סוג המילוי");
    } else {
        submitCookie.click();
        AlertAddedItem();
    }
}//checkStatusCookie

function AlertAddedItem(){
    alert("המוצר נוסף לסל בהצלחה");
}


// --------------lightBox code----------------

// Open the Modal
function openModal() {
    document.getElementById("myModal").style.display = "block";
}

// Close the Modal
function closeModal() {
    document.getElementById("myModal").style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("demo");
    var captionText = document.getElementById("caption");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
    captionText.innerHTML = dots[slideIndex-1].alt;
}

