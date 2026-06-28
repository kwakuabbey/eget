const brands = {
    "Toyota": [
        "Corolla","Camry","Yaris","Hilux","Land Cruiser",
        "Prado","RAV4","Highlander","Fortuner","Vitz"
    ],

    "Honda": [
        "Accord","Civic","CR-V","HR-V","Pilot","Fit"
    ],

    "Nissan": [
        "Altima","Almera","Patrol","Navara","Qashqai",
        "X-Trail","Sentra"
    ],

    "Mercedes-Benz":[
        "C-Class","E-Class","S-Class","GLA","GLC",
        "GLE","GLS","G-Class"
    ],

    "BMW":[
        "1 Series","3 Series","5 Series","7 Series",
        "X1","X3","X5","X7"
    ]
};

const brand = document.getElementById("brand");
const model = document.getElementById("model");
const year = document.getElementById("year");

for (let b in brands){
    let option = document.createElement("option");
    option.text = b;
    option.value = b;
    brand.add(option);
}

brand.addEventListener("change", function(){

    model.innerHTML = "<option>Select Model</option>";

    brands[this.value].forEach(function(m){

        let option = document.createElement("option");

        option.text = m;

        option.value = m;

        model.add(option);

    });

});

for(let i=2026;i>=1990;i--){

    let option=document.createElement("option");

    option.text=i;

    option.value=i;

    year.add(option);

}