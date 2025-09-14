function getPredictionUsingAxios() {
    // Create an object to hold input data
    let inputData = {};
    
    for (let i = 1; i <= 11; i++) {
        let value = document.querySelector(`.feature${i}`);
        
        if (value) {
            let parsedValue = parseFloat(value.value);
            if (!isNaN(parsedValue)) {
                // Add each feature to the inputData object
                inputData[`feature${i}`] = parsedValue;
            } else {
                alert(`Feature ${i} is not a valid number.`);
                return;
            }
        } else {
            alert(`Feature ${i} element not found.`);
            return;
        }
    }

    // Send the inputData object to the API
    axios.post('http://127.0.0.1:5000/predict', inputData)
    .then((response) => {
        let result = response.data;
        if (result.prediction !== undefined) {
            result.prediction = result.prediction == 1 ? "positive" : "Congratulations ,Your Sample Is Negative";
            document.getElementById("prediction").innerHTML = `
                <div id="result">
                    <h3> Result:</h3>
                    <h4>${result.prediction}</h4>
                </div>
            `;
        } else {
            alert("No prediction received.");
        }
    })
    .catch((error) => {
        alert("Error: " + (error.response?.data?.detail || error.message));
    });
}