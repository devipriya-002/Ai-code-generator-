async function generateCode(){

    let language = document.getElementById("language").value;
    let prompt = document.getElementById("prompt").value;

    if(prompt.trim()==""){
        alert("Please enter a prompt");
        return;
    }

    document.getElementById("output").textContent = "Generating...";

    const response = await fetch("/generate",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            language:language,
            prompt:prompt
        })
    });

    const data = await response.json();

    document.getElementById("output").textContent = data.result;
}
