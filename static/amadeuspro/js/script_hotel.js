
let pays = document.getElementById("pays");
let ville = document.getElementById("ville");


pays.addEventListener('change',function(){

    let pays_select = pays.value;
    console.log("jai changer la valeur");
    console.log(pays_select);
    // données à envoyer
    const data = {
        pays_selected : pays_select,
    };
    // configuration de la requéte
    const url = "";
    const options = { 
        method : 'POST',
        headers : {
            'content-Type' : 'application/json',
        },
        // body : JSON.stringify(data),
    };
    // Envoi de la requète
    fetch(url,options)
        .then(response => response.json())
        .then(result =>{
            console.log(result.message);
            

        })
        .catch(error => {
            // gestion des erreurs
            console.log(error);
        })
})


